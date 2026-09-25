#!/usr/bin/env python3
"""Regenerate logos-data.js from manifest.json.

The gallery's Copy buttons read each SVG's source text out of logos-data.js, so this has to
be re-run whenever artwork is added, replaced or removed. From the repository root:

    python3 tools/build-data.py

Each entry in manifest.json may carry an explicit "form" ("icon" or "wordmark"). Without one
the form is inferred from the artwork's aspect ratio, which is right for most files but wrong
for a stacked lockup -- square, yet carrying the bank's name. Pin those.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SHORT_CODES = "codes.json"        # optional: {"BANK NAME": "CODE"}; absent is fine


def artbox(path):
    head = open(path, encoding="utf8", errors="ignore").read(4000)
    vb = re.search(r'viewBox\s*=\s*["\']\s*[-\d.]+[ ,]+[-\d.]+[ ,]+([\d.]+)[ ,]+([\d.]+)', head)
    if vb:
        return float(vb.group(1)), float(vb.group(2))
    w = re.search(r'\bwidth\s*=\s*["\']([\d.]+)', head)
    h = re.search(r'\bheight\s*=\s*["\']([\d.]+)', head)
    return (float(w.group(1)), float(h.group(1))) if w and h else (1.0, 1.0)


def infer_form(path):
    w, h = artbox(path)
    return "icon" if h and w / h <= 1.6 else "wordmark"


def hint(src):
    if src.startswith("extracted"):
        return None
    f = os.path.basename(src).lower()
    if re.search(r'[-_]bn[-_.]|_bn\.svg|-_bn', f):
        return "Bengali"
    if "icon" in f:
        return "Icon only"
    if "horizontal" in f or "horz" in f:
        return "Horizontal"
    return None


def entry(bank, group, codes):
    name = bank["display"].split(" — ")[0]
    variants = [{
        "path": o["path"], "kb": o["kb"],
        "form": o.get("form") or infer_form(o["path"]),
        "quality": "traced" if o["kind"] == "traced" else "vector",
        "h": hint(o["from"]),
    } for o in bank["originals"]]

    # Guarantee both lockups where the repo can, falling back to the traced packs only for a
    # form that is otherwise missing entirely.
    for want, key in (("icon", "icon"), ("wordmark", "full")):
        if any(v["form"] == want for v in variants):
            continue
        p = bank.get(key)
        if p and os.path.exists(p) and not any(v["path"] == p for v in variants):
            variants.append({"path": p, "kb": max(1, bank[f"{key}_bytes"] // 1024),
                             "form": want, "quality": "traced", "h": None})

    # Card default is the recognisable full logo; the icon is one click or one filter away.
    variants.sort(key=lambda v: (v["quality"] != "vector", v["form"] != "wordmark"))
    best = next((i for i, v in enumerate(variants) if v["quality"] == "vector"),
                0 if variants else -1)

    seen = {}
    for v in variants:
        base = {"icon": "Icon", "wordmark": "With text"}[v["form"]]
        seen[base] = seen.get(base, 0) + 1
        v["label"] = v.pop("h") or (base if seen[base] == 1 else f"{base} {seen[base]}")

    return {"name": name, "code": codes.get(bank.get("bank_name") or "", ""),
            "group": group, "best": best, "variants": variants}


def main():
    manifest = json.load(open("manifest.json"))
    codes = json.load(open(SHORT_CODES)) if os.path.exists(SHORT_CODES) else {}

    banks = ([entry(b, "bd", codes) for b in manifest["banks"]] +
             [entry(b, "intl", codes) for b in manifest["extras"]])
    banks.sort(key=lambda b: b["name"].lower())

    missing = [v["path"] for b in banks for v in b["variants"] if not os.path.exists(v["path"])]
    if missing:
        sys.exit("manifest references files that do not exist:\n  " + "\n  ".join(missing))

    src = {}
    for b in banks:
        for v in b["variants"]:
            s = open(v["path"], encoding="utf8", errors="ignore").read()
            s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
            s = re.sub(r'<metadata[^>]*>.*?</metadata>', '', s, flags=re.S)
            src[v["path"]] = re.sub(r'\n{2,}', '\n', s).strip()

    with open("logos-data.js", "w") as fh:
        fh.write("window.BANKS=")
        json.dump(banks, fh, separators=(",", ":"), ensure_ascii=False)
        fh.write(";\nwindow.LOGO_SRC=")
        json.dump(src, fh, separators=(",", ":"), ensure_ascii=False)
        fh.write(";\n")

    variants = sum(len(b["variants"]) for b in banks)
    vi = sum(1 for b in banks for v in b["variants"]
             if v["form"] == "icon" and v["quality"] == "vector")
    print(f"{len(banks)} banks, {variants} variants, {vi} crisp vector icons "
          f"-> logos-data.js ({os.path.getsize('logos-data.js') // 1024} KB)")


if __name__ == "__main__":
    main()

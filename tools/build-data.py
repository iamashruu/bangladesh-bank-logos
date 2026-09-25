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


# A trace of a favicon is mush at any size; a trace of a large source is not. Judge each file by the
# bitmap it was traced FROM -- tracers record that as the SVG's width/height -- rather than by the
# folder it happens to sit in. Anything below this on its shortest edge is dropped from the gallery.
MIN_TRACE_EDGE = 120


def trace_info(path):
    """(is_traced, source_shortest_edge). Shortest edge is None when it cannot be read."""
    head = open(path, encoding="utf8", errors="ignore").read(900)
    if "VTracer" not in head and "ezgif" not in head:
        return False, None            # no tracer signature: real vector, wherever it lives
    m = re.search(r'\bwidth="([\d.]+)"\s*height="([\d.]+)"', head)
    return True, (min(float(m.group(1)), float(m.group(2))) if m else None)


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
    def make(path, kb, form=None, hint_from=""):
        traced, edge = trace_info(path)
        return {"path": path, "kb": kb, "form": form or infer_form(path),
                "quality": "traced" if traced else "vector", "edge": edge,
                "h": hint(hint_from)}

    variants = [make(o["path"], o["kb"], o.get("form"), o["from"]) for o in bank["originals"]]

    # Guarantee both lockups where the repo can, falling back to the traced packs only for a
    # form that is otherwise missing entirely.
    for want, key in (("icon", "icon"), ("wordmark", "full")):
        if any(v["form"] == want for v in variants):
            continue
        p = bank.get(key)
        if p and os.path.exists(p) and not any(v["path"] == p for v in variants):
            variants.append(make(p, max(1, bank[f"{key}_bytes"] // 1024), want))

    # Drop traces made from a source too small to hold its own detail.
    variants = [v for v in variants
                if v["quality"] != "traced"
                or (v["edge"] is not None and v["edge"] >= MIN_TRACE_EDGE)]
    for v in variants:
        v.pop("edge", None)

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
    traced = sum(1 for b in banks for v in b["variants"] if v["quality"] == "traced")
    empty = [b["name"] for b in banks if not b["variants"]]
    print(f"{len(banks)} banks, {variants} variants ({traced} traced, all from sources "
          f">= {MIN_TRACE_EDGE}px), {vi} crisp vector icons "
          f"-> logos-data.js ({os.path.getsize('logos-data.js') // 1024} KB)")
    if empty:
        print("banks with no artwork: " + ", ".join(empty))


if __name__ == "__main__":
    main()

"""Text-overflow check: render only text, on a canvas padded 150px each side; count ink outside the 600x900 poster."""
import io, re, subprocess
from PIL import Image
PAD = 150
STYLE = "<style>*{fill:none!important;stroke:none!important;filter:none!important;opacity:1!important;clip-path:none!important;mask:none!important} text,text *{fill:#000!important;fill-opacity:1!important}</style>"
def overflow_px(svg):
    s = re.sub(r'viewBox="[^"]*"', f'viewBox="{-PAD} {-PAD} {600+2*PAD} {900+2*PAD}"', svg, count=1)
    s = re.sub(r'(<svg[^>]*?)\s(width|height)="[^"]*"', r"\1", s, count=2)
    s = re.sub(r"(<svg[^>]*>)", r"\1" + STYLE, s, count=1)
    png = subprocess.run(["rsvg-convert", "-w", str(600 + 2 * PAD)], input=s.encode(), capture_output=True).stdout
    if not png: return None
    a = Image.open(io.BytesIO(png)).convert("RGBA").getchannel("A")
    w, h = a.size; m = 4  # tolerance in px
    total = sum(a.point(lambda v: 255 if v > 64 else 0).tobytes()) // 255
    inner = sum(a.crop((PAD - m, PAD - m, w - PAD + m, h - PAD + m)).point(lambda v: 255 if v > 64 else 0).tobytes()) // 255
    return total - inner
if __name__ == "__main__":
    import json, sys
    rows = json.load(open(sys.argv[1]))
    for r in rows:
        if r["svg"]: print(r["brief"], r["model"][:8], r["arm"], r["sample"], overflow_px(r["svg"]))

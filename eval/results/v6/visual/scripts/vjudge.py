"""Blind multi-way vision judge: show N posters as a numbered grid, ask for the top 3 to put up."""
import base64, io, json, random, re, subprocess, sys
from pathlib import Path
sys.path.insert(0, "eval")
from lib.llm import chat
from PIL import Image, ImageDraw, ImageFont

FONT = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
PROMPT = ("These are {n} candidate posters for the same brief: \"{brief}\"\n\n"
          "You are the art director. Rank the three you would actually print and put up: each must be great at its job "
          "(lands at a glance, legible, every fact clear, well made) and stand out from the others on a wall. "
          "Being unusual is worth nothing if the poster is not great.\n"
          "Reply on the first line with the three numbers, best first, like: 4, 7, 1. Then one sentence on why your first pick wins.")

def render(svg, w=300):
    png = subprocess.run(["rsvg-convert", "-w", str(w)], input=svg.encode(), capture_output=True).stdout
    if not png:  # invalid SVG: a browser would show nothing either
        im = Image.new("RGB", (w, int(w * 1.5)), "#dddddd"); ImageDraw.Draw(im).text((20, 20), "failed to render", fill="black", font=FONT); return im
    im = Image.open(io.BytesIO(png)).convert("RGB"); im.thumbnail((w, int(w * 1.5))); return im

def grid(images, cols=4, w=300):
    h = int(w * 1.5); band = 44; rows = (len(images) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (w + 12) + 12, rows * (h + band + 12) + 12), "white"); d = ImageDraw.Draw(sheet)
    for i, im in enumerate(images):
        x = 12 + (i % cols) * (w + 12); y = 12 + (i // cols) * (h + band + 12)
        d.text((x, y + 6), str(i + 1), fill="black", font=FONT)
        sheet.paste(im, (x, y + band))
    buf = io.BytesIO(); sheet.save(buf, "PNG"); return base64.b64encode(buf.getvalue()).decode()

def judge(judge_model, brief, items, shuffle_seed, w=300):
    """items: list of (id, svg). Returns ranked ids (top 3) and the raw text."""
    order = items[:]; random.Random(shuffle_seed).shuffle(order)
    img = grid([render(svg, w) for _, svg in order], w=w)
    content = [{"type": "text", "text": PROMPT.format(n=len(order), brief=brief)},
               {"type": "image_url", "image_url": {"url": "data:image/png;base64," + img}}]
    raw, _ = chat(judge_model, None, content, temperature=0.0, max_tokens=300, seed_index=shuffle_seed, tag="vjudge")
    nums = [int(x) for x in re.findall(r"\d+", raw.splitlines()[0] if raw else "")][:3]
    return [order[k - 1][0] for k in nums if 1 <= k <= len(order)], raw

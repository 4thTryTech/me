#!/usr/bin/env python3
"""Makes the favicons and the 1200x630 link-preview image into static/. Run after changing the name or title.

Needs fonttools (outlines the lettering so icons need no font) and playwright with Chromium (rasterizes).
python3 make_images.py
"""
import asyncio, base64, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from content import SITE

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = TTFont(os.path.join(HERE, "static/source/share-tech-mono-400.woff"))
SHEET, LINE, MINT, AMBER = "#0F3D73", "#E4F0FF", "#8CF2C0", "#FFD166"


def outline(text, size, x, y, anchor="middle", tracking=0.0):
    gs, cmap, hmtx = FONT.getGlyphSet(), FONT.getBestCmap(), FONT["hmtx"]
    s = size / FONT["head"].unitsPerEm
    names = [cmap[ord(c)] for c in text]
    width = sum(hmtx[g][0] * s for g in names) + tracking * (len(names) - 1)
    x0 = x - (width / 2 if anchor == "middle" else width if anchor == "end" else 0)
    pen = SVGPathPen(gs)
    adv = 0
    for g in names:
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x0 + adv, y)))
        adv += hmtx[g][0] * s + tracking
    return pen.getCommands()


def icon(size=512, full=True):
    grid = "".join(f'<path d="M{i} 0V512M0 {i}H512" stroke="#fff" stroke-opacity=".08"/>' for i in range(64, 512, 64)) if full else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}">'
            f'<rect width="512" height="512" rx="{0 if full else 96}" fill="{SHEET}"/>{grid}'
            f'<circle cx="256" cy="256" r="196" fill="none" stroke="{MINT}" stroke-width="18"/>'
            f'<circle cx="256" cy="256" r="168" fill="none" stroke="{MINT}" stroke-width="8" stroke-opacity=".6"/>'
            f'<path d="{outline("ML", 200, 256, 326, tracking=6)}" fill="{LINE}"/></svg>')


def og():
    name = outline(SITE["name"], 92, 80, 250)
    title = outline(SITE["title"], 36, 82, 318)
    site = outline("michaellehman.me", 26, 82, 548)
    grid = "".join(f'<path d="M{i} 0V630" stroke="#fff" stroke-opacity="{.09 if i % 100 == 0 else .035}"/>' for i in range(0, 1200, 20))
    grid += "".join(f'<path d="M0 {i}H1200" stroke="#fff" stroke-opacity="{.09 if i % 100 == 0 else .035}"/>' for i in range(0, 630, 20))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">'
            f'<rect width="1200" height="630" fill="{SHEET}"/>{grid}'
            f'<rect x="24" y="24" width="1152" height="582" fill="none" stroke="{LINE}" stroke-opacity=".5" stroke-width="2"/>'
            f'<path d="{name}" fill="{LINE}"/><path d="{title}" fill="{MINT}"/>'
            f'<line x1="82" y1="380" x2="700" y2="380" stroke="{AMBER}" stroke-width="2"/>'
            f'<path d="M82 372V388M700 372V388" stroke="{AMBER}" stroke-width="2"/>'
            f'<path d="{site}" fill="{AMBER}"/>'
            f'<g transform="translate(860 150)"><circle cx="150" cy="150" r="140" fill="none" stroke="{MINT}" stroke-width="6"/>'
            f'<circle cx="150" cy="150" r="118" fill="none" stroke="{MINT}" stroke-width="3" stroke-opacity=".6"/>'
            f'<path d="{outline("ML", 130, 150, 196, tracking=4)}" fill="{LINE}"/></g></svg>')


async def main():
    from playwright.async_api import async_playwright
    os.makedirs("static/icons", exist_ok=True); os.makedirs("static/images", exist_ok=True)
    with open("static/icons/favicon.svg", "w") as f:
        f.write(icon(512, full=False))
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        async def shot(svg, w, h, path):
            await pg.set_viewport_size({"width": w, "height": h})
            await pg.set_content(f'<body style="margin:0"><img style="display:block;width:{w}px;height:{h}px" src="data:image/svg+xml;base64,{base64.b64encode(svg.encode()).decode()}">')
            await pg.screenshot(path=path, omit_background=True)
        for s, name, full in ((32, "favicon-32.png", False), (180, "apple-touch-icon.png", True), (512, "icon-512.png", True)):
            await shot(icon(s, full), s, s, f"static/icons/{name}")
        await shot(og(), 1200, 630, "static/images/og.png")
        await b.close()
    print("images written")

if __name__ == "__main__":
    os.chdir(HERE)
    asyncio.run(main())

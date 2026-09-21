#!/usr/bin/env python3
"""Builds michaellehman.me into docs/ (GitHub Pages serves that folder).

usage: python3 build.py [path to a checkout of the brand repo, default ../brand]

Plain Python 3, no dependencies. Nunito Sans comes from the 4th Try Tech brand repo at build time; Share Tech Mono,
the favicons and the link-preview image live in static/. Copy lives in content.py, styles in src/site.css.
The look is the blueprint theme variant of the 4th Try Tech brand (art-direction style A5): the page is a drawing sheet.
"""
import html, os, shutil, sys
from content import SITE, INTRO, ABOUT, ROLE, EXPERIENCE, SKILLS, LINKS

BRAND = sys.argv[1] if len(sys.argv) > 1 else "../brand"
OUT = "docs"
HERE = os.path.dirname(os.path.abspath(__file__))
e = html.escape

COPY = {  # brand repo path -> site path
    "fonts/web/nunito-sans-400.woff2": "assets/fonts/nunito-sans-400.woff2",
    "fonts/web/nunito-sans-600.woff2": "assets/fonts/nunito-sans-600.woff2",
    "fonts/Nunito_Sans/OFL.txt": "assets/fonts/OFL-nunito-sans.txt",
}

# The rocket as an engineering drawing: the 4th Try Tech rocket in blueprint style (brand scripts/build.py, style A5,
# variation B), with Michael's initials in the porthole. Colors come from CSS classes so print can re-ink it.
BODY = "M200 40 C236 82 250 132 250 182 V330 H150 V182 C150 132 164 82 200 40 Z"
FIN_L = "M150 236 C118 268 102 312 104 356 L150 326 Z"
FIN_R = "M250 236 C282 268 298 312 296 356 L250 326 Z"
NOZZLE = "M172 328 H228 L234 348 H166 Z"
FLAME = "M176 346 C166 388 188 412 200 446 C212 412 234 388 224 346 Z"


def drawing():
    n = lambda x, y, s, a="start", c="": f'<text x="{x}" y="{y}" text-anchor="{a}" class="note{c}">{s}</text>'
    return f"""<svg class="drawing" viewBox="0 0 400 500" role="img" aria-labelledby="dwg-t">
<title id="dwg-t">Line drawing of a rocket with the initials ML in its porthole, annotated like an engineering drawing.</title>
<defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9" class="ln" fill="none" stroke-width="1.4"/></marker></defs>
<line x1="200" y1="18" x2="200" y2="486" class="ln faint" stroke-dasharray="14 4 3 4"/>
<g class="part" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
<path d="{FLAME}" class="am" fill="none" stroke-dasharray="6 4"/>
<path d="{FIN_L}" class="am fin"/><path d="{FIN_R}" class="am fin"/>
<path d="{NOZZLE}" class="ln sheet"/><path d="{BODY}" class="ln hull"/></g>
<path d="M150 182 H250 M150 300 H250" class="ln faint"/>
<circle cx="200" cy="205" r="36" class="mn sheet" stroke-width="2"/><circle cx="200" cy="205" r="30" class="mn" fill="none" stroke-width="1.4"/>
<text x="200" y="206" text-anchor="middle" dominant-baseline="central" class="ml">ML</text>
<path d="M256 40 H352 M256 330 H352" class="ln faint"/>
<line x1="344" y1="42" x2="344" y2="328" class="ln" stroke-width="1.2" marker-start="url(#arw)" marker-end="url(#arw)"/>
<text transform="translate(362 185) rotate(90)" text-anchor="middle" class="note">BODY 290</text>
<path d="M122 300 L70 262 H24" class="ln lead"/><circle cx="122" cy="300" r="2.4" class="dot"/>{n(24, 256, "FIN X2", c=" amber")}
<path d="M188 396 L90 430 H24" class="ln lead"/><circle cx="188" cy="396" r="2.4" class="dot"/>{n(24, 424, "EXHAUST", c=" amber")}
<path d="M236 205 L300 132 H388" class="ln lead"/><circle cx="236" cy="205" r="2.4" class="dot"/>{n(388, 126, "PILOT", "end", " mint")}
<path d="M104 362 V476 M296 362 V476" class="ln faint"/>
<line x1="106" y1="470" x2="294" y2="470" class="ln" stroke-width="1.2" marker-start="url(#arw)" marker-end="url(#arw)"/>
<rect x="156" y="462" width="88" height="16" class="sheet-fill"/>{n(200, 474, "FIN SPAN 192", "middle")}
</svg>"""


def bubble(letter):
    return f'<span class="bubble" aria-hidden="true">{letter}</span>'


def title_block(sheet):
    cells = [("Drawn by", "M. Lehman"), ("Title", SITE["title"]), ("Location", SITE["location"]),
             ("Dwg no.", SITE["drawing"]), ("Rev", SITE["revision"].replace("REV ", "")), ("Sheet", f"{sheet} of 2")]
    return '<dl class="tblock">' + "".join(f'<div class="c{i}"><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for i, (k, v) in enumerate(cells)) + "</dl>"


def layout(path, title, description, body, sheet):
    root = "../" * path.count("/")
    nav_items = [("About", "#about"), ("Role", "role/"), ("Experience", "#experience"), ("Skills", "#skills"), ("Links", "#links")]
    nav = "".join(f'<a href="{root}{h}"{" aria-current=page" if h == path else ""}>{l}</a>' if not h.startswith("#") else
                  f'<a href="{root if path else ""}{h}">{l}</a>' for l, h in nav_items)
    full = f"{title} | {SITE['name']}" if title else f"{SITE['name']}, {SITE['title']}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(full)}</title>
<meta name="description" content="{e(description)}">
<meta name="author" content="{e(SITE['name'])}">
<link rel="preload" href="{root}assets/fonts/share-tech-mono-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/site.css">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<meta name="theme-color" content="#0F3D73">
<link rel="canonical" href="{e(SITE['url'] + path)}">
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{e(SITE['url'] + path)}">
<meta property="og:image" content="{e(SITE['url'])}assets/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
<a class="home" href="{root or './'}">{e(SITE['name'])}</a>
<nav aria-label="Sections">{nav}</nav>
</div></header>
<main id="main" class="sheet">
{body}
</main>
<footer class="site"><div class="wrap">
<p>Also building things at <a href="https://4thtry.tech/">4th Try Tech</a>.</p>
<p class="dim">{e(SITE['drawing'])} {e(SITE['revision'])}. Drawn in plain HTML and CSS.</p>
</div></footer>
</body>
</html>
"""


def page_home():
    exp = "".join(
        f'<li class="job{" now" if j.get("current") else ""}"><div class="dim-rail" aria-hidden="true"><span>{e(j["span"])}</span></div>'
        f'<div class="job-b"><h3>{e(j["role"])}</h3><p class="org">{e(j["company"])}<span class="when">{e(j["dates"])}</span></p>'
        f'<ul>{"".join(f"<li>{e(p)}</li>" for p in j["points"]).replace("on the role page.", "on the <a href=role/>role page</a>.")}</ul></div></li>'
        for j in EXPERIENCE)
    skills = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in SKILLS)
    links = "".join(f'<li><a href="{e(u)}">{e(n)}</a><span>{e(d)}</span></li>' for n, u, d in LINKS)
    areas = "".join(f"<li>{e(name)}</li>" for name, _ in ROLE["areas"])
    # built outside the f-string: a backslash inside an f-string expression needs Python 3.12
    about = "".join(f"<p>{e(p)}</p>" for p in ABOUT).replace("at 4th Try Tech.", 'at <a href="https://4thtry.tech/">4th Try Tech</a>.')
    body = f"""<section class="hero"><div class="wrap">
<div class="hero-g">
<div class="hero-t">
<h1>{e(SITE['name'])}</h1>
<p class="post">{e(SITE['title'])}</p>
<p class="intro">{e(INTRO)}</p>
<p class="acts"><a class="btn" href="role/">Read the role in full</a><a class="alt" href="#experience">Experience</a></p>
</div>
<div class="hero-d">{drawing()}</div>
</div>
{title_block(1)}
</div></section>
<section id="about" class="blk"><div class="wrap two">
<h2>{bubble("A")}About</h2>
<div class="prose">{about}</div>
</div></section>
<section id="role" class="blk"><div class="wrap two">
<h2>{bubble("B")}Current role</h2>
<div class="prose"><p>{e(ROLE['summary'])}</p>
<p>The role covers six areas:</p><ul class="areas">{areas}</ul>
<p><a class="btn" href="role/">Read the role in full</a></p></div>
</div></section>
<section id="experience" class="blk"><div class="wrap two">
<h2>{bubble("C")}Experience</h2>
<div><p class="overall"><span>Feb 1999</span><span class="span-line" aria-hidden="true"></span><span>today</span></p>
<ol class="jobs">{exp}</ol></div>
</div></section>
<section id="skills" class="blk"><div class="wrap two">
<h2>{bubble("D")}Skills</h2>
<dl class="skills">{skills}</dl>
</div></section>
<section id="links" class="blk"><div class="wrap two">
<h2>{bubble("E")}Elsewhere</h2>
<ul class="links">{links}</ul>
</div></section>"""
    return layout("", "", SITE["description"], body, 1)


def page_role():
    letters = "ABCDEF"
    areas = "".join(f'<section class="area"><h2>{bubble(letters[i])}{e(name)}</h2><ul>{"".join(f"<li>{e(p)}</li>" for p in pts)}</ul></section>'
                    for i, (name, pts) in enumerate(ROLE["areas"]))
    body = f"""<section class="hero small"><div class="wrap">
<p class="crumb"><a href="../">{e(SITE['name'])}</a></p>
<h1>{e(SITE['title'])}</h1>
<p class="intro">{e(ROLE['summary'])}</p>
{title_block(2)}
</div></section>
<div class="wrap role">{areas}
<p class="back"><a class="btn" href="../#experience">Back to experience</a></p></div>"""
    return layout("role/", SITE["title"], "The scope of Michael Lehman's role as " + SITE["title"] + ".", body, 2)


def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    os.chdir(HERE)
    if os.path.isdir(OUT):
        shutil.rmtree(OUT, ignore_errors=True)
    for src, dst in COPY.items():
        d = os.path.join(OUT, dst)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copyfile(os.path.join(BRAND, src), d)
    for folder, dest in (("src", "assets"), ("static/fonts", "assets/fonts"), ("static/images", "assets"), ("static/icons", "")):
        for name in os.listdir(folder):
            os.makedirs(os.path.join(OUT, dest), exist_ok=True)
            shutil.copyfile(os.path.join(folder, name), os.path.join(OUT, dest, name))
    write(".nojekyll", "")
    if SITE.get("domain"):
        write("CNAME", SITE["domain"] + "\n")
    write("index.html", page_home())
    write("role/index.html", page_role())
    nf = layout("", "Page not found", "That page is not here.",
                f'<section class="hero small"><div class="wrap"><h1>Not on this drawing</h1><p class="intro">The page you were after is not here.</p>'
                f'<p class="acts"><a class="btn" href="{SITE["url"]}">Back to the first sheet</a></p></div></section>', 1)
    write("404.html", nf)
    n = sum(len(f) for _, _, f in os.walk(OUT))
    print(f"built {n} files into {OUT}/")


if __name__ == "__main__":
    main()

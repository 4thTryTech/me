# michaellehman.me

Michael Lehman's online resume. It uses the **blueprint** theme variant of the [4th Try Tech brand](https://github.com/4thTryTech/brand) (art-direction style A5): the page is drawn as an engineering sheet with a drafting grid, a title block, dimension lines and detail bubbles.

## Build

```
python3 build.py ../brand      # path to a checkout of 4thTryTech/brand
```

Plain Python 3, no dependencies. Output goes to `docs/`, which GitHub Pages serves.

| File | What it holds |
| --- | --- |
| `content.py` | All copy: intro, about, role, experience, skills, links |
| `build.py` | Page templates and the rocket drawing |
| `src/site.css` | Blueprint styles, plus a clean whiteprint style for printing or saving as PDF |
| `static/` | Share Tech Mono (OFL), favicons and the link-preview image |
| `make_images.py` | Regenerates favicons and `og.png` (needs fonttools and playwright) |

Nunito Sans is copied from the brand repo at build time, so the brand repo stays the source of truth.

## Publish

1. Settings > Pages > Deploy from a branch > `main`, folder `/docs`.
2. `docs/CNAME` already says `michaellehman.me`. At the domain registrar add the GitHub Pages records: `A` records for `@` pointing to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, and a `CNAME` for `www` pointing to `4thtrytech.github.io`.
3. Once the certificate is issued, tick **Enforce HTTPS**.

## Sister site

[4thtry.tech](https://4thtry.tech/) carries the short bio and links here; this site links back from the About section, the Elsewhere section and the footer.

# Handoff: put michaellehman.me into the repos

Built in a phone session on 2026-09-21. Everything, binaries included, is in the artifact "Handoff bundle: michaellehman.me" (unpack with the extractor at its top; files under me/ go to the repo root).

## 1. `me` repo (D:\4thtrytech\me, remote github.com/4thTryTech/me, currently empty)

1. Unpack the bundle's me/ files into the repo root. Fonts (Share Tech Mono, SIL OFL), favicons and og.png are already there. `make_images.py` only needs rerunning if the name or title changes (fonttools + playwright).
2. The brand repo must sit beside it at ../brand (Nunito Sans is copied from there).
3. `python3 build.py ../brand` writes `docs/` (16 files, including CNAME = michaellehman.me and .nojekyll).
4. Check it: serve `docs/` and open `/` and `/role/` at 390 px and 1440 px; no sideways scroll, no missing files.
5. Commit ("Blueprint resume site: home, role page, experience, skills") and push `main`.
6. Michael then enables Pages: Settings > Pages > main, /docs. DNS at the registrar: A records for @ to 185.199.108.153, .109.153, .110.153, .111.153; CNAME www to 4thtrytech.github.io; then Enforce HTTPS.

## 2. `website` repo (4thtry.tech)

Apply the bundle's `website/website-bio-link.patch` with `git am website-bio-link.patch` (one commit: build.py, content.py and the rebuilt docs/). If docs/ conflicts, apply only the source changes with `git apply --include=build.py --include=content.py`, then run `python3 build.py ../brand`.
What it does: Story "Who is behind it" becomes the short bio ending with a link to michaellehman.me (the draft-wording note is removed); Contact gets a michaellehman.me line; every footer gets an "About Michael" link. Adds a ("link", before, label, url) body block to prose().
Push (commit message: "Story: short bio linking to michaellehman.me; footer and contact links").

## Open items for Michael
- LinkedIn and email are not on the site; a commented LinkedIn line is ready in content.py LINKS.
- Headline title is "IT Service and Platform Automation Architect"; the Capgemini job entry says "Architect" to match LinkedIn.
- Preview: https://claude.ai/artifact/6FijyMwy3CiWchdMuXkWcG

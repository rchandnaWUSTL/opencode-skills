"""Install HashiCorp Sans locally from the public Helios site (HashiCorp internal use only; do not redistribute).

Needs: python3 -m venv /tmp/fv && /tmp/fv/bin/pip install fonttools brotli   then run with /tmp/fv/bin/python.
Creates static TTFs in ~/Library/Fonts: 'HashiCorp Sans' (Regular, Bold), 'HashiCorp Sans Medium', 'HashiCorp Sans SemiBold'.
The variable font tops out at weight 600, so Bold == SemiBold. QUIT AND RELAUNCH Keynote afterwards, or it will not see the fonts.
"""
import os, urllib.request
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

SRC = "https://helios.hashicorp.design/assets/fonts/hashicorp-sans-variable.woff2"
urllib.request.urlretrieve(SRC, "/tmp/hs.woff2")
dest = os.path.expanduser("~/Library/Fonts")
for w, style, fam in [(400, "Regular", "HashiCorp Sans"), (500, "Medium", "HashiCorp Sans Medium"),
                      (600, "SemiBold", "HashiCorp Sans SemiBold"), (700, "Bold", "HashiCorp Sans")]:
    g = instancer.instantiateVariableFont(TTFont("/tmp/hs.woff2"), {"wght": w}); n = g["name"]
    for rec in list(n.names):
        if rec.nameID in (1, 2, 3, 4, 6, 16, 17, 21, 22, 25): n.removeNames(nameID=rec.nameID)
    ps = (fam + "-" + style).replace(" ", ""); sub = style if style in ("Regular", "Bold") else "Regular"
    for pid, eid, lid in ((3, 1, 0x409), (1, 0, 0)):
        n.setName(fam, 1, pid, eid, lid); n.setName(sub, 2, pid, eid, lid); n.setName(f"{fam} {style}", 4, pid, eid, lid)
        n.setName(ps, 6, pid, eid, lid); n.setName(ps + "-1", 3, pid, eid, lid)
    if style == "Bold": g["OS/2"].fsSelection = (g["OS/2"].fsSelection & ~0x40) | 0x20; g["head"].macStyle |= 1
    else: g["OS/2"].fsSelection = (g["OS/2"].fsSelection & ~0x21) | 0x40; g["head"].macStyle &= ~1
    g.flavor = None; g.save(os.path.join(dest, f"HashiCorpSans-{style}.ttf"))
print("installed; relaunch Keynote")

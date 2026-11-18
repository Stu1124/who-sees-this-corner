"""Inject policy facts + source links into template.html -> who-sees-this-corner.html.

Usage: python3 -I build.py <facts.json> [overrides.json]
"""
import json, sys, pathlib

here = pathlib.Path(__file__).resolve().parent
facts = json.loads(pathlib.Path(sys.argv[1]).read_text()) if len(sys.argv) > 1 and pathlib.Path(sys.argv[1]).exists() else []
if len(sys.argv) > 2:
    over = json.loads(pathlib.Path(sys.argv[2]).read_text())
    by = {f["id"]: f for f in facts}
    for fid, patch in over.items():
        by.setdefault(fid, {"id": fid}).update(patch)
    facts = list(by.values())

SOURCES = {
    "sfmta_speed": {"label": "Automated Speed Enforcement Camera", "url": "https://www.sf.gov/sites/default/files/2024-04/MTA%20Automated%20Speed%20Enforcement%20Camera%20STP%20-%20BOS%20Review.pdf"},
    "sfmta_redlight": {"label": "Red Light and No Right-Turn Camera", "url": "https://www.sf.gov/documents/38550/SFMTA_Automated_Red_Light_Camera_-_STP_2.pdf"},
    "sfmta_lpr": {"label": "License Plate Reader and Transit-Only Lane Enforcement Camera", "url": "https://sfgov.legistar.com/View.ashx?M=F&ID=11065541&GUID=A886AD5F-639A-48C9-9D6D-DE2B9D50E6C1"},
    "sfmta_security": {"label": "Security Camera", "url": "https://www.sf.gov/sites/default/files/2022-03/MTA_Security%20Camera%20Policy%20Final%20Draft%202-25-21.pdf"},
    "sfmta_busanalytics": {"label": "Driver-Safety Video Analytics", "url": "https://www.sf.gov/sites/default/files/2024-04/SFMTA%20Driver-Safety%20Video%20Analytics%20STP%20-%20BOS%20Review.pdf"},
    "sfmta_taxi": {"label": "Taxi Dashboard Camera", "url": "https://sfgov.legistar.com/View.ashx?M=F&ID=11065539&GUID=9205D990-FA00-4B8D-A9AB-D3900A34183F"},
    "sfpd_alpr": {"label": "Automated License Plate Reader", "url": "https://www.sf.gov/documents/55994/Surveillance_Tech_Policy_Amend.pdf"},
}

html = (here / "template.html").read_text()
def inject(src, tag, value):
    start, end = f"/*{tag}*/", "/*END*/"
    i = src.index(start); j = src.index(end, i)
    return src[:i + len(start)] + json.dumps(value, ensure_ascii=False).replace("</", "<\\/") + src[j:]
html = inject(html, "FACTS", facts)
html = inject(html, "SOURCES", SOURCES)
out = here / "who-sees-this-corner.html"
out.write_text(html)
print(f"wrote {out.name}: {len(facts)} policies, {len(html)//1024} KB")

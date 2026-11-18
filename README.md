# Who Sees This Corner

A live 3D model of Mission St & 16th St in San Francisco. Everything that records you is outlined in orange. Click it to see what it collects, how long the city keeps it, who else gets it, and the gaps in its policy, then send a public comment or records request in one click.

**Live:** https://stu1124.github.io/who-sees-this-corner/

## Data
Seven approved/draft surveillance technology policies from SF's Admin Code Ch. 19B inventory (sf.gov/surveillance-technology-inventory): SFMTA speed cameras, red-light cameras, license plate readers + transit-lane enforcement, security cameras, bus driver-safety video analytics, taxi dashcams; SFPD ALPR (2021 + amendment). Facts extracted with Claude into `data/facts.json`, each linked to its source PDF.

## Run
Open `index.html` in a browser. Rebuild: `python3 src/build.py data/facts.json data/overrides.json`.

## Limits
Device placement is illustrative, not real camera locations (by design). Extracted fields and the 56 flagged gaps are model-assisted and should be checked against the PDFs. Several posted policies show Board of Supervisors approval as "TBD".

Built at Claude Impact Lab SF, Trust & Safety Micro-Hack (Track 4: Privacy), Nov 17 2026.

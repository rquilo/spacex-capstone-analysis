# SpaceX Falcon 9 landing analysis

Applied Data Science Capstone, IBM / Coursera. Rodrigo Ariel Quilodran. Analysis date: 7 November 2026.

AI-assisted implementation and report preparation. Every notebook was executed; results are retained. This educational analysis uses historical public course snapshots, not current launch performance.

## Reproduce

Use Python 3.12. Install `requirements.txt`, then run notebooks 01 through 08 from Jupyter. Start `python dashboard.py` and visit http://127.0.0.1:8050. Open the HTML files under `maps/` for interactive Folium maps (internet needed for map tiles).

## Contents

- `notebooks/`: API collection, web scraping, wrangling, SQL, visual EDA, Folium, prediction, and Dash validation.
- `dashboard.py`: working site and payload filters with Plotly Dash.
- `data/`: original course snapshots and historical Wikipedia HTML.
- `results/`: generated datasets and JSON results.
- `maps/`: interactive site, outcome and proximity maps.
- `figures/`: analysis figures and browser screenshots.
- `report/`: presentation PDF.
- `data_sources.json` and `source_urls.json`: provenance.

## Scope and limitations

The main modeling dataset contains 90 Falcon 9 launches through 2020. SQL uses 101 records and four launch-site labels. The geographic and dashboard snapshot has 56 records. These populations must not be compared as if identical.

The SpaceX live v4 enrichment endpoints returned HTTP 522 or timed out. Notebook 01 normalizes IBM's static API response and explicitly uses IBM's enriched snapshot, validating the launch dates and outcomes against the raw JSON. No live API success is claimed.

Encoding only Orbit, LaunchSite, LandingPad and Serial gives 80 columns. Expanding the three Boolean columns to two indicators each gives the supplied 83-column modeling matrix.

The course baseline scales before splitting. The report uses an additional training-only scaling pipeline to avoid this leakage. Historical reuse metadata may contain hindsight information. A future deployment needs timestamp-valid features, chronological validation and larger samples. Class 1 includes controlled ocean landings and does not prove booster recovery or reuse.

Map distances use manually selected OpenStreetMap reference points and haversine distance. They are approximate straight-line distances, not road travel or surveyed nearest-feature distances.

## Sources and attribution

IBM Skills Network official capstone starter notebooks and datasets are attributed in the provenance JSON and notebook text. Wikipedia launch tables use revision 1027686922 and remain subject to Wikipedia's CC BY-SA terms. Map tiles and data are credited to OpenStreetMap contributors within each map. Original third-party materials retain their respective rights.

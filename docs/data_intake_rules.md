# Data Intake Rules

## 1. Raw Data Rules
- All original datasets go ONLY into data/raw/
- Raw files are immutable (read-only by convention)
- No renaming after initial save

## 2. File Naming Convention
<source>__<region>__<granularity>__<date_range>.<ext>

Examples:
- ev_sessions__bangalore__hourly__2023-01_to_2023-12.csv
- charger_locations__india__static__2024-05.geojson

## 3. Mandatory Metadata
Every dataset must have:
- Source URL or provider
- Collection date
- Timezone
- License (if any)

Metadata is documented in:
docs/datasets.md

## 4. Versioning Rule
If data is re-downloaded:
- New file, new name
- Never overwrite an existing raw file

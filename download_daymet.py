"""Download daily gridded Daymet estimates at three representative state-forest points."""
from pathlib import Path
from io import StringIO
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "daymet_forest_points"
OUT.mkdir(parents=True, exist_ok=True)

FORESTS = {
    "dupont": ("DuPont State Recreational Forest", 35.1903, -82.6025),
    "clemmons": ("Clemmons Educational State Forest", 35.6741, -78.4893),
    "bladen_lakes": ("Bladen Lakes State Forest", 34.6880, -78.5951),
}
for code, (name, latitude, longitude) in FORESTS.items():
    parameters = dict(lat=latitude, lon=longitude, vars="tmax,tmin,prcp", years="2023,2024,2025")
    try:
        response = requests.get("https://daymet.ornl.gov/single-pixel/api/data", params=parameters, timeout=90)
        response.raise_for_status()
        lines = response.text.splitlines()
        header = next((i for i, line in enumerate(lines) if line.strip().lower().startswith("year,yday")), None)
        if header is None:
            raise ValueError("Daymet returned no recognizable CSV header; verify API access")
        daily = pd.read_csv(StringIO("\n".join(lines[header:])))
        daily["forest"] = name
        daily["forest_lat"] = latitude
        daily["forest_lon"] = longitude
        out = OUT / f"{code}_daymet_2023_2025.csv"
        daily.to_csv(out, index=False)
        print(f"Saved {out}: {len(daily)} daily records")
    except (requests.RequestException, ValueError) as error:
        print(f"Could not download {name}: {error}")

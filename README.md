# North Carolina Forest Climate Analysis

This project examines temperature and precipitation patterns at three North Carolina state forest locations. Using Python, I compared long-term regional climate averages, analyzed daily climate estimates from 2023–2025, and retrieved short-term weather forecasts. The goal is to understand how conditions differ across the Mountains, Piedmont, and Coastal Plain.

## Study locations

| State forest | Region | Nearby reference station |
|---|---|---|
| DuPont State Recreational Forest | Mountains | Brevard |
| Clemmons Educational State Forest | Piedmont | Raleigh State University |
| Bladen Lakes State Forest | Coastal Plain | Lumberton |

## Data and analysis

The project uses three public climate datasets:

- **NOAA climate normals (1991–2020)** for a baseline comparison of temperature and rainfall.
- **NASA Daymet (2023–2025)** for daily temperature and precipitation estimates at the selected forest coordinates.
- **National Weather Service forecasts** for upcoming temperature and precipitation conditions.

The Python scripts organize the datasets, calculate monthly summaries, compare locations, and generate figures.

## Key observations

| Region | Mean annual temperature at reference station | Annual precipitation |
|---|---:|---:|
| Mountains (Brevard) | 55.6°F | 75.57 in |
| Piedmont (Raleigh State University) | 61.7°F | 49.36 in |
| Coastal Plain (Lumberton) | 63.0°F | 50.83 in |

The mountain location is cooler and wetter on average. The 2023–2025 Daymet records also show clear seasonal temperature patterns and considerable variation in precipitation between months. The forecast analysis provides a short-term view of expected conditions at the same three locations.

This is an exploratory comparison of representative locations. The historical reference stations are near the forests, Daymet provides gridded estimates, and forecast values come from the National Weather Service.

## Run the analysis

Install Python, then open a terminal in the project folder:

```powershell
python -m pip install -r requirements.txt
python analyze_climate.py
python download_daymet.py
python analyze_daymet.py
python nws_7day_forecast.py
```

The scripts save the climate summaries in `data/` and charts in `figures/`. The Daymet download and weather forecast scripts require internet access.

## Data sources

- [NOAA U.S. Climate Normals](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals)
- [NASA/ORNL Daymet](https://daymet.ornl.gov/)
- [National Weather Service API](https://www.weather.gov/documentation/services-web-api)
- [North Carolina Forest Service](https://www.ncagr.gov/divisions/nc-forest-service/state-forests)

Some analysis code and documentation were prepared with AI assistance; the scripts were executed and results reviewed by the researcher.

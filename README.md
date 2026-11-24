# North Carolina State Forest Climate Analysis

**Python research portfolio | Spatial comparison of regional climate and short-term weather forecasts**

## Research question
How do temperature and precipitation vary among representative locations in North Carolina's Mountains, Piedmont, and Coastal Plain, and what does the current National Weather Service forecast indicate at those locations?

## Locations and data
| Forest | Region | Historical reference station | Forest point (latitude, longitude) |
|---|---|---|---|
| DuPont State Recreational Forest | Mountains | Brevard | 35.1903, -82.6025 |
| Clemmons Educational State Forest | Piedmont | Raleigh State University | 35.6741, -78.4893 |
| Bladen Lakes State Forest | Coastal Plain | Lumberton | 34.6880, -78.5951 |

This study combines three different sources:
- **1991–2020 climate normals** from weather stations near the selected forests, used as historical regional reference conditions.
- **NASA/ORNL Daymet** daily gridded temperature and precipitation estimates for 2023–2025, sampled at representative forest coordinates.
- **National Weather Service (NWS)** short-term daytime/nighttime forecasts for those coordinates, retrieved from the official public API.

The datasets serve different purposes: *climate normals* represent long-term typical conditions; *Daymet* provides gridded historical estimates; *NWS* provides changing forecasts, **not predictions made by a model trained in this repository**.

## Initial results
| Region | Mean annual temperature at reference station (°F) | Published annual precipitation (inches) |
|---|---:|---:|
| Mountains (Brevard) | 55.6 | 75.57 |
| Piedmont (Raleigh State University) | 61.7 | 49.36 |
| Coastal Plain (Lumberton) | 63.0 | 50.83 |

The mountain reference station is comparatively cooler and wetter. These station-level results do not describe conditions across entire forests.

For the separate **2023–2025 Daymet analysis**, each selected point has 1,095 daily records. Aggregating them by calendar month reveals seasonal temperature cycles and large fluctuations in monthly precipitation. The Daymet estimate for October 2024 at the Bladen Lakes sample point was 0 mm on all 31 days; this is a **model-derived estimate**, not independent rain-gauge verification.

A forecast run in November 2026 identified a period of high precipitation probability around Thanksgiving Day at the three points. **Precipitation probability is not rainfall amount.** The forecast changes over time; rerun the NWS script to retrieve a current forecast.

## Reproduce the analyses
Python 3.11 or later recommended. From this repository's root folder:

```powershell
python -m pip install -r requirements.txt
python analyze_climate.py
python download_daymet.py
python analyze_daymet.py
python nws_7day_forecast.py
```

The scripts create output in `data/` and `figures/`.

- `analyze_climate.py`: reads the included station-normal CSVs and generates `figures/reproduced_monthly_climate.png`.
- `download_daymet.py`: fetches daily 2023–2025 records into `data/daymet_forest_points/`; internet required.
- `analyze_daymet.py`: aggregates the downloaded daily records into `data/daymet_monthly_results.csv` and plots monthly temperature/precipitation.
- `nws_7day_forecast.py`: retrieves current NWS forecast periods; saves `data/nws_7day_forecast.csv` and `figures/04_nws_7day_forecast.png`; internet required.

## Interpretation and limitations
This is an **exploratory analysis** of three representative locations, not a statewide forest climate assessment. Station observations and gridded estimates are not interchangeable. The three-year Daymet period is too short to support climate-change attribution, and no forest growth or vegetation response data are analyzed here. Forecast temperature and precipitation probabilities are taken from NWS, not predicted by a locally trained model. Recent forecast output is time-sensitive, so historical screenshots should not be presented as today's forecasts.

The repository contains **no unpublished master's thesis datasets**.

## Data credits
- NOAA U.S. Climate Normals: https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals
- Reference station tables transcribed from [Brevard](https://climate-charts.com/usa-stations/nc/usc00311055.html), [Raleigh State University](https://climate-charts.com/usa-stations/nc/usc00317079.html), and [Lumberton](https://climate-charts.com/usa-stations/nc/usc00315177.html). Monthly values as shown on source pages may be rounded; published annual precipitation is retained separately.
- NASA/ORNL Daymet web services: https://daymet.ornl.gov/web_services.html
- National Weather Service API: https://www.weather.gov/documentation/services-web-api
- North Carolina Forest Service state forests: https://www.ncagr.gov/divisions/nc-forest-service/state-forests

## Development note
This portfolio documents analysis that the researcher personally ran, inspected, and interpreted, with AI assistance in preparing some Python scripts and documentation. The project credits the original public data providers and does not claim a new weather forecasting model or independently authored code throughout.

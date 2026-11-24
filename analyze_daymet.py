"""Aggregate the Daymet 2023–2025 daily records by forest and month."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
files = list((ROOT / "data" / "daymet_forest_points").glob("*.csv"))
if not files:
    raise SystemExit("No Daymet input files. Run: python download_daymet.py")

frames = []
for file in files:
    daily = pd.read_csv(file)
    daily.columns = [column.strip() for column in daily.columns]
    tmax = next((name for name in daily if name.startswith("tmax")), None)
    tmin = next((name for name in daily if name.startswith("tmin")), None)
    prcp = next((name for name in daily if name.startswith("prcp")), None)
    if not all((tmax, tmin, prcp, "year" in daily, "yday" in daily, "forest" in daily)):
        raise ValueError(f"Unexpected data columns in {file}")
    daily["date"] = pd.to_datetime(daily.year.astype(str), format="%Y") + pd.to_timedelta(daily.yday - 1, unit="D")
    daily["mean_temp_c"] = (daily[tmax] + daily[tmin]) / 2
    daily["precip_mm"] = daily[prcp]
    frames.append(daily)

combined = pd.concat(frames, ignore_index=True)
combined["month"] = combined.date.dt.to_period("M").astype(str)
monthly = combined.groupby(["forest", "month"], as_index=False).agg(
    mean_temp_c=("mean_temp_c", "mean"),
    rainfall_mm=("precip_mm", "sum"),
    n_days=("date", "count"),
)
monthly.to_csv(ROOT / "data" / "daymet_monthly_results.csv", index=False)
(ROOT / "figures").mkdir(exist_ok=True)
fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
for name, group in monthly.groupby("forest"):
    dates = pd.to_datetime(group.month)
    axes[0].plot(dates, group.mean_temp_c, label=name)
    axes[1].plot(dates, group.rainfall_mm, label=name)
axes[0].set_ylabel("Mean air temperature (°C)")
axes[1].set_ylabel("Monthly estimated precipitation (mm)")
for axis in axes:
    axis.grid(alpha=0.2)
    axis.legend(fontsize=8)
    axis.tick_params(axis="x", rotation=45)
fig.tight_layout()
fig.savefig(ROOT / "figures" / "03_daymet_forest_daily_results.png", dpi=175)
plt.close(fig)
print("Saved data/daymet_monthly_results.csv and figures/03_daymet_forest_daily_results.png")

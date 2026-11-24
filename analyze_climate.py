"""Compare published 1991–2020 regional weather-station normals."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
monthly = pd.read_csv(ROOT / "data" / "nearby_noaa_station_climate_normals_monthly.csv")
annual = pd.read_csv(ROOT / "data" / "summary_climate_normals.csv")
(ROOT / "figures").mkdir(exist_ok=True)

fig, axes = plt.subplots(2, 1, figsize=(10.5, 8), sharex=True)
for (station, region), part in monthly.groupby(["station", "region"], sort=False):
    part = part.sort_values("month_num")
    axes[0].plot(part.month_num, (part.tmax_f + part.tmin_f) / 2, marker="o", label=f"{region}: {station}")
    axes[1].plot(part.month_num, part.precip_in, marker="o", label=f"{region}: {station}")

axes[0].set_title("Reference weather-station climate normals near NC state forests (1991–2020)")
axes[0].set_ylabel("Mean monthly temperature (°F)")
axes[0].legend(fontsize=8)
axes[1].set_ylabel("Monthly precipitation (inches)")
axes[1].set_xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
for ax in axes:
    ax.grid(alpha=0.25)
fig.tight_layout()
out = ROOT / "figures" / "reproduced_monthly_climate.png"
fig.savefig(out, dpi=175)
plt.close(fig)

print("\nReference climate summary (regional proxies, not in-forest measurements):")
print(annual[["region", "station", "annual_mean_temp_f", "annual_precip_in_published"]].to_string(index=False))
print(f"\nChart: {out}")

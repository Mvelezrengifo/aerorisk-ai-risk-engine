import xarray as xr
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "weather" / "era5-levels-members.grib"


def load_weather():
    ds = xr.open_dataset(DATA_PATH, engine="cfgrib")
    return ds


def build_climate_grid(ds):
    lats = ds.latitude.values
    lons = ds.longitude.values

    grid = []

    for lat in lats:
        for lon in lons:
            grid.append({
                "latitude": float(lat),
                "longitude": float(lon)
            })

    return grid


if __name__ == "__main__":
    ds = load_weather()
    grid = build_climate_grid(ds)

    print("Total climate cells:", len(grid))
    print(grid[:5])
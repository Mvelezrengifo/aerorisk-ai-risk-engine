from pathlib import Path
import xarray as xr

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "weather" / "era5-levels-members.grib"

def load_weather_dataset():
    ds = xr.open_dataset(DATA_PATH, engine="cfgrib")
    return ds

if __name__ == "__main__":
    dataset = load_weather_dataset()
    print(dataset)
from pathlib import Path
import pandas as pd

def import_health_data():
    print("Upload your Google Health folder.")
    # > Some sort of interface to upload Google Health folder

def read_health_folder():
    google_health_dir = Path.cwd() / "Google Health"
    azm_csv_files = [p for p in Path(google_health_dir / "Active Zone Minutes (AZM)").iterdir() ]
    print(azm_csv_files)
    #active_zone_minutes = pd.read_csv("/Google Health/" +)

read_health_folder()
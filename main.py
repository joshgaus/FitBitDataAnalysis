from pathlib import Path
import pandas as pd

google_health_dir = Path(__file__).resolve().parent / "Google Health"
paths_to_useful_health_folders = [Path(google_health_dir / "Active Zone Minutes (AZM)"),
                                  Path(google_health_dir / "Global Export Data"),
                                  Path(google_health_dir / "Health Fitness Data_GoogleData"),
                                  Path(google_health_dir / "Heart Rate Variability"),
                                  Path(google_health_dir / "Oxygen Saturation (SpO2)"),
                                  Path(google_health_dir / "Physical Activity_GoogleData"),
                                  Path(google_health_dir / "Sleep Score"),
                                  Path(google_health_dir / "Temperature")]
relevant_csv_files = ["sleep_score",
                  "daily_resting_heart_rate",
                  "daily_respiratory_rate",
                  "daily_readiness",
                  "daily_oxygen_saturation",
                  "daily_heart_rate_variability",
                  "cardio_load_observed_interval",
                  "cardio_acute_chronic_workload_ratio",
                  "Daily SpO2 -",
                  "Daily Respiratory Rate Summary",
                  "Daily Heart Rate Variability Summary",]
relevant_json_files = ["time_in_heart_rate_zones",  # 1 .json file per day
                  "sedentary_minutes-"]             # 1 .json file per month

def import_health_data():
    print("Upload your Google Health folder.")
    # > Some sort of interface to upload Google Health folder
    # Google health folder will eventually have to upload straight into project folder (whatever folder the script's in)
    # so that read_health_folder_can see it


def find_relevant_file_paths():
    for i in relevant_csv_files:
        print(list(google_health_dir.rglob(str(i) + "*.csv")))
    for i in relevant_json_files:
        print(list(google_health_dir.rglob(str(i) + "*.json")))
find_relevant_file_paths()
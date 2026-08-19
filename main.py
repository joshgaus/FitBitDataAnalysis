from datetime import datetime

import zoneinfo
from pathlib import Path

import pandas as pd
from pandas import DataFrame

google_health_dir = Path(__file__).resolve().parent / "Google Health"
relevant_csv_file_keywords = ["sleep_score",
                  "daily_resting_heart_rate",
                  "daily_respiratory_rate",
                  "daily_readiness",
                  "daily_oxygen_saturation",
                  "daily_heart_rate_variability",
                  "cardio_load_observed_interval",
                  "cardio_acute_chronic_workload_ratio"]
                 # "Daily SpO2 -"]
                 # "Daily Respiratory Rate Summary"
                 # "Daily Heart Rate Variability Summary",]
relevant_json_file_keywords = ["time_in_heart_rate_zones",  # 1 .json file per day
                  "sedentary_minutes-"]             # 1 .json file per month

def read_csvs_to_dataframe():
    # main_data is the primary dataframe which all other data is imported into
    main_frame = pd.DataFrame()

    # daily_resting_heart_rate.csv
    # Reads relevant columns into df, formats the timestamp
    daily_rhr_csv_path = google_health_dir / "Physical Activity_GoogleData" / "daily_resting_heart_rate.csv"
    # Relevant columns: 0-timestamp, 1-rhr in bpm
    df = pd.read_csv(daily_rhr_csv_path, usecols=[0,1], parse_dates=True)
    df = df.rename(columns={"beats per minute": "rhr in bpm"})

    main_frame = pd.concat([main_frame, df])
    main_frame["timestamp"] = pd.to_datetime(main_frame["timestamp"], format="ISO8601")

    # sleep_score.csv
    # Reads sleep_score.csv's relevant columns, formats the timestamp
    sleep_score_csv_path = google_health_dir / "Sleep Score" / "sleep_score.csv"
    # Relevant columns: 1-timestamp, 2-overall score, 6-deep sleep in minutes, 8-restlessness
    df = pd.read_csv(sleep_score_csv_path, usecols=[1,2,6,8],parse_dates=True)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="ISO8601")

    #Reconcile relevant rows in sleep_score.csv and main dataframe
    for df_index, df_timestamp in enumerate(df["timestamp"]):
        for mf_index, mf_timestamp in enumerate(main_frame["timestamp"]):
            #print(df_timestamp.date)
            if df_timestamp.normalize == mf_timestamp.normalize:
                print(True)
                main_frame = pd.concat([main_frame.iloc[mf_index], df.iloc[df_index, 1:]], axis=1)

   # print(main_frame.to_string())
read_csvs_to_dataframe()
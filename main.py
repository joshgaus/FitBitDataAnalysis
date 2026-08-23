from pathlib import Path
import pandas as pd

def main():
    google_health_dir = Path(__file__).resolve().parent / "Google Health"

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

    sleep_score_csv_path = google_health_dir / "Sleep Score" / "sleep_score.csv"
    main_frame = read_csv_into_main_frame(main_frame, sleep_score_csv_path, [1,2,6,8])

    daily_respiratory_rate_csv_path = google_health_dir / "Physical Activity_GoogleData" / "daily_respiratory_rate.csv"
    main_frame = read_csv_into_main_frame(main_frame, daily_respiratory_rate_csv_path, [0,1])

    daily_hrv_csv_path = google_health_dir / "Physical Activity_GoogleData" / "daily_heart_rate_variability.csv"
    main_frame = read_csv_into_main_frame(main_frame, daily_hrv_csv_path, [0,1])

    print(main_frame.to_string())

def read_csv_into_main_frame(mf: pd.DataFrame, csv_path: Path, col_nums_for_df: list[int]) -> pd.DataFrame:

    # Read relevant data from csv into df
    df = pd.read_csv(csv_path, usecols=col_nums_for_df, parse_dates=True)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="ISO8601").dt.normalize()

    # Initialize empty columns in main_frame to import data from df into
    col_names = []
    for col_name in df.columns.tolist():
        if col_name != "timestamp":
            mf[col_name] = None
            col_names.append(col_name)

    # Reconcile relevant rows in csv and main_frame
    for mf_index, mf_timestamp in enumerate(mf["timestamp"]):
        for df_index, df_timestamp in enumerate(df["timestamp"]):
            if df_timestamp == mf_timestamp:
                for column in col_names:
                    mf.at[mf_index, column] = df.at[df_index, column]
    return mf

if __name__ == "__main__":
    main()
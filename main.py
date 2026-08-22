from pathlib import Path
import pandas as pd

google_health_dir = Path(__file__).resolve().parent / "Google Health"

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
    '''
    # sleep_score.csv
    # Reads sleep_score.csv's relevant columns, formats the timestamp

    # Initialize rows to be filled in main_frame from sleep_score.csv
    main_frame["overall sleep score"] = None
    main_frame["deep sleep in minutes"] = None
    main_frame["restlessness"] = None

    # Relevant columns: 1-timestamp, 2-overall_score, 6-deep_sleep_in_minutes, 8-restlessness
    df = pd.read_csv(sleep_score_csv_path, usecols=[1,2,6,8],parse_dates=True)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="ISO8601").dt.normalize()

    #Reconcile relevant rows in sleep_score.csv and main dataframe
    for mf_index, mf_timestamp in enumerate(main_frame["timestamp"]):
        for df_index, df_timestamp in enumerate(df["timestamp"]):
            if df_timestamp == mf_timestamp:
                main_frame.at[mf_index, "overall sleep score"] = df.at[df_index, "overall_score"]
                main_frame.at[mf_index, "deep sleep in minutes"] = df.at[df_index, "deep_sleep_in_minutes"]
                main_frame.at[mf_index, "restlessness"] = df.at[df_index, "restlessness"]
    '''
    sleep_score_csv_path = google_health_dir / "Sleep Score" / "sleep_score.csv"
    daily_respiratory_rate_csv_path = google_health_dir / "Physical Activity_GoogleData" / "daily_respiratory_rate.csv"
    main_frame = read_csv_into_main_frame(main_frame, sleep_score_csv_path, [1,2,6,8])
    main_frame = read_csv_into_main_frame(main_frame, daily_respiratory_rate_csv_path, [0,1])
    print(main_frame.to_string())
'''
    # daily_respiratory_rate.csv
    # Reads daily_respiratory_rate.csv's relevant columns, formats timestamp

    # Initialize rows to be filled in main_frame from daily_respiratory_rate.csv
    main_frame["daily resp. rate, breaths/min"] = None

    daily_respiratory_rate_csv_path = google_health_dir / "Physical Activity_GoogleData" / "daily_respiratory_rate.csv"
    # Relevant columns: 0-timestamp, 1-breaths per minute
    df = pd.read_csv(daily_respiratory_rate_csv_path, usecols=[0,1], parse_dates=True)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="ISO8601")

    # Reconcile relevant rows in daily_respiratory_rate.csv and main dataframe
    for mf_index, mf_timestamp in enumerate(main_frame["timestamp"]):
        for df_index, df_timestamp in enumerate(df["timestamp"]):
            if df_timestamp == mf_timestamp:
                main_frame.at[mf_index, "daily resp. rate, breaths/min"] = df.at[df_index, "breaths per minute"]

    print(main_frame.to_string())
'''
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

read_csvs_to_dataframe()
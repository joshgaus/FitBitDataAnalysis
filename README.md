FitBit Data Analysis

This tool allows you to automatically load your Google Health Export data into a spreadsheet for easy analysis and visualization. Features to be added below.

TODO
1. Read all relevant data from files into main spreadsheet
   - ✔️ Make function for reusability
   - ✔️ Track indicators of stress
     - ✔️sleep_score
     - ✔️daily_resting_heart_rate
     - ✔️daily_respiratory_rate
     - ✔️daily_heart_rate_variability
   - Track user choices
     - Time to wake up
     - time_in_heart_rate_zones
     - sedentary_minutes
       - sedentary_minutes-2026-06-06.json
       - sedentary_minutes-2026-07-06.json
       - etc
   - Read wake up time from sleep_score (right now its normalizing the timestamp to just the date)
2. Visualize data
3. Perform correlation analysis on data for insights
4. Allow for use with web portal

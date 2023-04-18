import pandas as pd

# Read in the data
at_df = pd.read_csv("./data/at.csv")
wt_df = pd.read_csv("./data/wt.csv")

# Nomenclature
wt_df = wt_df.drop([ "agency_cd", "site_no", "parameter_cd", "ts_id"], 1).rename(columns={"year_nu": "Year", "mean_va": "Water_Temp_C", "month_nu": "Month"})

# Adjust string to integer
at_df["Month"] = at_df["Month"].astype(int)

# Look for month 1 (January)
jan_wt_df = wt_df.loc[wt_df["Month"] == 1]
jan_at_df = at_df.loc[at_df["Month"] == 1]

# Merge the two dataframes
jan_df = pd.merge(jan_wt_df, jan_at_df, on="Year", how="outer").set_index("Year").dropna().drop("Month_x", 1).rename(columns={"Month_y": "Month"})

# Save the data
jan_df.to_csv("./data/january_temp.csv")
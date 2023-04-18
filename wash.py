import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
at_df = pd.read_csv("./data/at.csv")
wt_df = pd.read_csv("./data/wt.csv")

wt_df = wt_df.drop([ "agency_cd", "site_no", "parameter_cd", "ts_id"], 1).rename(columns={"year_nu": "Year", "mean_va": "Water_Temp_C", "month_nu": "Month"})

df = pd.merge(at_df, wt_df, on="Year", how="outer").set_index("Year").dropna().drop("Month_x", 1).rename(columns={"Month_y": "Month"})
df.to_csv("./data/oregon_temp.csv")
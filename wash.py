import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./dt_temp_1.csv")

df["S"] = df["YEAR"].str.split("-").map(lambda items : sorted(items, key=str))

month = []
year = []

for i, row in df.iterrows():
  month.append(row["S"][0])
  year.append(row["S"][1])

df["month"] = month
df["year"] = year
df = df.drop(["YEAR", "S"], 1)

jan = df[df["month"] == "01"]
jan.to_csv("jan.csv")

feb = df[df["month"] == "02"]
feb.to_csv("feb.csv")

march = df[df["month"] == "03"]
march.to_csv("march.csv")

april = df[df["month"] == "04"]
april.to_csv("april.csv")

may = df[df["month"] == "05"]
may.to_csv("may.csv")

june = df[df["month"] == "06"]
june.to_csv("june.csv")

july = df[df["month"] == "07"]
july.to_csv("july.csv")

august = df[df["month"] == "08"]
august.to_csv("august.csv")

september = df[df["month"] == "09"]
september.to_csv("september.csv")

october = df[df["month"] == "10"]
october.to_csv("october.csv")

november = df[df["month"] == "11"]
november.to_csv("november.csv")

december = df[df["month"] == "12"]
december.to_csv("december.csv")

# df.plot(x='YEAR', y='TEMP', kind='line')
# plt.show()
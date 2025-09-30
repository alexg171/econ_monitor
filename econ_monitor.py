import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./bls_cpi_data/cu.data.1.AllItems", sep=r"\s+", header=0)

series_id = "CUUR0000SA0"
df_series = df[df["series_id"] == series_id].copy()

df_series = df_series[df_series["period"].str.match(r"M\d{2}") & (df_series["period"] != "M13")].copy()

df_series["month"] = df_series["period"].str.extract(r"M(\d{2})").astype(int)

df_series["date"] = pd.to_datetime(
    df_series["year"].astype(str) + "-" +
    df_series["month"].astype(str).str.zfill(2) + "-01"
)

plt.figure(figsize=(10, 5))
plt.plot(df_series["date"], df_series["value"], label="CPI: All Items (U.S. Avg)")
plt.title("Consumer Price Index Over Time")
plt.xlabel("Date")
plt.ylabel("Index Value")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

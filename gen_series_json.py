import pandas as pd
import json
import os

df_data = pd.read_csv("./bls_cpi_data/cu.data.1.AllItems", sep=r"\s+", header=0)
df_info = pd.read_csv("./bls_cpi_data/cu.series", sep=r"\t", engine="python", header=0)
df_info.columns = df_info.columns.str.strip()
df_info['series_id'] = df_info['series_id'].str.strip()

for i, series in enumerate(df_info["series_id"]):
    print(f"Processing {i+1}/{len(df_info)}: {series}")
    meta = df_info[df_info["series_id"] == series].iloc[0]
    meta = meta.fillna("")
    meta = meta.to_dict()

    data = df_data[df_data["series_id"] == series]
    if data.empty:
        continue
    data["date"] = data["year"].astype(str) + "-" + data["period"].str.replace("M", "").str.zfill(2)
    data = data[["date", "value"]]
    data = data.to_dict(orient="records")
    
    out = {
        "series_id": series,
        "title": meta["series_title"],
        "metadata": {k: meta[k] for k in meta if k not in ["series_id", "series_title"]},
        "data": data
    }
    
    with open(f"econ-monitor/public/{series}.json", "w") as f:
        json.dump(out, f, indent=2)

files = [f for f in os.listdir("econ-monitor/public") if f.endswith(".json")]
with open("econ-monitor/public/index.json", "w") as f:
    json.dump(files, f)







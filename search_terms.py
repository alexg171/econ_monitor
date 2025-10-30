import pandas as pd


df_info = pd.read_csv("./bls_cpi_data/cu.series", sep=r"\t", engine="python", header=0)
df_info.columns = df_info.columns.str.strip()
df_info['series_id'] = df_info['series_id'].str.strip()

df_info.to_json('output.json', orient='records', indent=4)

print("DataFrame successfully written to output.json")




import pandas as pd

df = pd.read_parquet("data/silver/exchange_rates/usd_brl.parquet")

print(df)
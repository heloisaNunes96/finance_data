import pandas as pd
import glob #busca arquivos automaticamente
import json

files = glob.glob("data/bronze/exchange_rates/*.json")

latest_file = max(files) #pega o arquivo mais recente

with open(latest_file, "r", encoding="utf-8") as file:
    data = json.load(file)

usd_data = data["USDBRL"]

df = pd.DataFrame([{#transforma JSON em tabela
    "code": usd_data["code"],
    "codein": usd_data["codein"],
    "name": usd_data["name"],
    "high": float(usd_data["high"]),
    "low": float(usd_data["low"]),
    "bid": float(usd_data["bid"]),
    "ask": float(usd_data["ask"]),
    "timestamp": usd_data["timestamp"]
}])

#o float padroniza os tipos numéricos

output_path = "data/silver/exchange_rates/usd_brl.parquet"

df.to_parquet(output_path, index=False)

print(df)

print(f"Arquivo salvo em: {output_path}")
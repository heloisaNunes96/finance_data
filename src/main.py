import requests #Importa biblioteca HTTP
import json
from datetime import datetime

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL" #Define URL da API

response = requests.get(url) #Faz a requisição GET: acessa a internet, chama a API e recebe a resposta

data = response.json() #converte o json obtido em dicionário python

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") #gera a parte dinâmica do nome do arquivo

file_name = f"data/bronze/exchange_rates/usd_brl_{timestamp}.json"  

#salva o arquivo no disco:
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)


print(f"Arquivo salvo com sucesso: {file_name}")
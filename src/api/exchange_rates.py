import requests

URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"


def get_exchange_rate():
    response = requests.get(URL, timeout=10) ##Faz a requisição GET: acessa a internet, chama a API e recebe a resposta e o timeout evita travamento infinito

    response.raise_for_status() #Se API responder: 500; 404; 403; o erro aparece corretamente.

    return response.json() #converte o json obtido em dicionário python
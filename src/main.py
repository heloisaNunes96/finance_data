from datetime import datetime

from api.exchange_rates import get_exchange_rate
from utils.file_utils import save_json


def main():

    data = get_exchange_rate()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = (
        f"data/bronze/exchange_rates/"
        f"usd_brl_{timestamp}.json"
    )

    save_json(data, file_path)

    print(f"Arquivo salvo com sucesso: {file_path}")

if __name__ == "__main__":
    main()
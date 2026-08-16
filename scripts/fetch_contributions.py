import requests
from bs4 import BeautifulSoup
import json
import os

USERNAME = "Guilherme5G"
URL = f"https://github.com/users/{USERNAME}/contributions"

def fetch_data():
    print(f"Buscando contribuições públicas para {USERNAME}...")
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    days = soup.find_all(attrs={"data-level": True, "data-date": True})
    contributions = []
    for day in days:
        date = day.get('data-date')
        level = day.get('data-level')
        if date and level:
            contributions.append({"date": date, "level": int(level)})
    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(contributions, f, indent=4)
    print(f"Sucesso! {len(contributions)} dias salvos em data/contributions.json")

if __name__ == "__main__":
    fetch_data()
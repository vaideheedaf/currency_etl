import requests
from datetime import datetime, date

CURRENCIES = ['USD', 'GBP', 'INR', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SGD', 'ZAR']

def extract_live_rates():
    print("Extracting live rates...")
    url = "https://api.frankfurter.app/latest"
    params = {"to": ",".join(CURRENCIES)}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(" Live rates extracted")
        return response.json()
    else:
        raise Exception(f" Failed: {response.status_code}")

def extract_historical_rates(start_date, end_date):
    print(f"Extracting historical rates {start_date} to {end_date}...")
    url = f"https://api.frankfurter.app/{start_date}..{end_date}"
    params = {"to": ",".join(CURRENCIES)}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f" Historical rates extracted")
        return response.json()
    else:
        raise Exception(f" Failed: {response.status_code}")

if __name__ == "__main__":
    # Test live
    live = extract_live_rates()
    print(live)
    
    # Test historical
    historical = extract_historical_rates("2026-01-01", "2026-01-07")
    print(f"Days extracted: {len(historical['rates'])}")
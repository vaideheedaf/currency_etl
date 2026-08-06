from extract import extract_live_rates, extract_historical_rates
from transform import transform_live, transform_historical
from load import load
from datetime import date

def run_live_pipeline():
    print("\n Running live pipeline...")
    raw = extract_live_rates()
    records = transform_live(raw)
    load(records)
    print(" Live pipeline complete!")

def run_historical_pipeline(start_date, end_date):
    print(f"\n Loading historical data {start_date} to {end_date}...")
    raw = extract_historical_rates(start_date, end_date)
    records = transform_historical(raw)
    load(records)
    print(" Historical pipeline complete!")

if __name__ == "__main__":
    # First run — load all history since Jan 2026
    run_historical_pipeline("2026-01-01", str(date.today()))
    
    # Then load today's live rates
    run_live_pipeline()
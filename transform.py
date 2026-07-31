from datetime import datetime

def transform_live(data):
    records = []
    now = datetime.now()
    
    for currency_code, rate in data['rates'].items():
        record = {
            "currency_code": currency_code,
            "rate": rate,
            "base_currency": data['base'],
            "timestamp": now,
            "day": now.day,
            "month": now.month,
            "year": now.year,
            "hour": now.hour
        }
        records.append(record)
    
    print(f" Transformed {len(records)} live records")
    return records

def transform_historical(data):
    records = []
    
    for date_str, rates in data['rates'].items():
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        
        for currency_code, rate in rates.items():
            record = {
                "currency_code": currency_code,
                "rate": rate,
                "base_currency": data['base'],
                "timestamp": dt,
                "day": dt.day,
                "month": dt.month,
                "year": dt.year,
                "hour": 0
            }
            records.append(record)
    
    print(f"Transformed {len(records)} historical records")
    return records

if __name__ == "__main__":
    # Test with dummy data
    sample_live = {
        "base": "EUR",
        "date": "2026-07-31",
        "rates": {"USD": 1.1485, "INR": 109.5495, "GBP": 0.85573}
    }
    records = transform_live(sample_live)
    for r in records:
        print(r)
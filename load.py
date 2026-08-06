import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def get_currency_id(cursor, currency_code):
    cursor.execute(
        "SELECT currency_id FROM dim_currency WHERE currency_code = %s",
        (currency_code,)
    )
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        raise Exception(f"Currency not found: {currency_code}")

def load(records):
    conn = get_connection()
    cursor = conn.cursor()
    
    for record in records:
        currency_id = get_currency_id(cursor, record["currency_code"])
        cursor.execute("""
            INSERT INTO fact_rates (
                currency_id, rate, base_currency,
                timestamp, day, month, year, hour
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            currency_id,
            record["rate"],
            record["base_currency"],
            record["timestamp"],
            record["day"],
            record["month"],
            record["year"],
            record["hour"]
        ))
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f" Loaded {len(records)} records into PostgreSQL")

if __name__ == "__main__":
    # Test with sample record
    sample = [{
        "currency_code": "USD",
        "rate": 1.1485,
        "base_currency": "EUR",
        "timestamp": __import__('datetime').datetime.now(),
        "day": 2,
        "month": 8,
        "year": 2026,
        "hour": 0
    }]
    load(sample)
import datetime
import pandas as pd
import asyncio
from env_canada import ECHistorical

def fetch_historical_weather(station_id, start_date, end_date):
    try:
        # Convert to datetime objects
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        # Prepare to store results
        all_data = []

        for date in pd.date_range(start_date, end_date, freq="YE"):
            try:
                year = (int)(date.year)
                ec = ECHistorical(station_id=station_id, year=year, language="english", format="xml")
                asyncio.run(ec.update())
                data = ec
                if data is not None:
                    all_data.extend(data)
            except Exception as e:
                print(f"Failed to retrieve data for {date.date()}: {e}")

        # Convert to DataFrame
        df = pd.DataFrame(all_data)
        print(df.head())
        return df

    except Exception as e:
        print(f"Error: {e}")

# Example usage
station_id = 51442  # Change to your desired station
start_date = "2020-03-01"
end_date = "2024-03-10"
data = fetch_historical_weather(station_id, start_date, end_date)
data.to_csv("historical_weather.csv", index=False)  # Save to CSV

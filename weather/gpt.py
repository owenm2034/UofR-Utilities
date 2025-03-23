import datetime
import pandas as pd
import asyncio
from env_canada import ECHistorical

## object defns
class Wind:
    def __init__(self, dirofmaxgust, speedofmaxgust):
        self.direction: int = dirofmaxgust # 10s of degrees
        self.speed: int = speedofmaxgust #

class Temp:
    def __init__(self, max, min, mean):
        self.max: int = max
        self.min: int = min
        self.mean: int = mean

class WeatherDay:
    def __init__(self, date: datetime, wind: Wind, temp: Temp):
        self.date: datetime = date
        self.wind: Wind = wind
        self.temp: Temp = temp

### fn
def fetch_historical_weather(station_id, start_year: int, end_year: int) -> list:
    try:
        # Convert to datetime objects
        start_year = datetime.datetime(year=start_year, month=1, day=1)
        end_year = datetime.datetime(year=end_year, month=1, day=1)

        # Prepare to store results
        weatherDays = []

        for date in pd.date_range(start_year, end_year, freq="YE"):
            try:
                year = (int)(date.year)
                ec = ECHistorical(station_id=station_id, year=year, language="english", format="xml")
                asyncio.run(ec.update())
                data = ec
                if data is not None:
                    for date, values in data.station_data.items():
                        w: Wind = Wind(
                            values['dirofmaxgust']['value'],
                            values['speedofmaxgust']['value']
                        )
                        t: Temp = Temp(
                            values['maxtemp']['value'], 
                            values['mintemp']['value'], 
                            values['meantemp']['value']
                        )
                        weatherDays.append(
                            WeatherDay(
                                datetime.datetime.strptime(date, "%Y-%m-%d"), 
                                w,
                                t
                            )
                        )
                return weatherDays
            
            except Exception as e:
                print(f"Failed to retrieve data for {date.date()}: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
station_id = 51442  # Change to your desired station
start_year = 2021
end_year = 2022
data = fetch_historical_weather(station_id, start_year, end_year)
data.to_csv("historical_weather.csv", index=False)  # Save to CSV

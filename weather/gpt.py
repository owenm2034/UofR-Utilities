from datetime import datetime
import pandas as pd
import asyncio
from env_canada import ECHistorical
import statistics

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
        start_year = datetime(year=start_year, month=1, day=1)
        end_year = datetime(year=end_year, month=1, day=1)

        # Prepare to store results
        weatherDays = []

        for date in pd.date_range(start_year, end_year, freq="YS"):
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
                                datetime.strptime(date, "%Y-%m-%d"), 
                                w,
                                t
                            )
                        )
            
            except Exception as e:
                print(f"Failed to retrieve data for {date.date()}: {e}")
        return weatherDays
    except Exception as e:
        print(f"Error: {e}")

def filter_weather_data(data, start_date, end_date) -> list:
    start_md = start_date
    end_md = end_date
    
    return list(filter(lambda x: start_md <= x.date.strftime("%m-%d") <= end_md, data))

def print_statistics(filteredWeatherDays):
    for attr, label, is_degree in [
        ("wind.direction", "Wind Direction", True),
        ("wind.speed", "Wind Speed", False),
        ("temp.min", "Min Temp", False),
        ("temp.max", "Max Temp", False),
        ("temp.mean", "Mean Temp", False)
    ]:
        values = [eval(f'w.{attr} * 10' if is_degree else f'w.{attr}') for w in filteredWeatherDays if eval(f'w.{attr}') is not None]
        if values:
            print(f'---{label}---')
            print(f'Average {label}: {statistics.mean(values)}')
            print(f'St_dev {label}: {statistics.stdev(values)}')
            print(f'Median {label}: {statistics.median(values)}')
        else:
            print(f'No valid data for {label}')

# Example usage
station_id = 51442  # Change to your desired station
start_year = 2000
end_year = 2023
start_date = '08-25'
end_date = '09-15'

data = fetch_historical_weather(station_id, start_year, end_year)
filtered_data = filter_weather_data(data, start_date, end_date)
print_statistics(filtered_data)
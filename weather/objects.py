# Example data
import datetime

class Wind:
    def __init__(self, date, dirofmaxgust, speedofmaxgust):
        self.date: datetime = date
        self.direction: int = dirofmaxgust
        self.speed: int = speedofmaxgust

class Temp:
    def __init__(self, max, min, mean):
        self.max = max,
        self.min = min,
        self.mean = mean

class WeatherDay:
    def __init__(self, date: datetime, wind: Wind, temp: Temp):
        self.wind = wind
        self.temp = temp

data = {
    '2020-03-01': {
        'maxtemp': {'value': 10.7, 'unit': '°C', 'label': 'Maximum Temperature'},
        'mintemp': {'value': 4.9, 'unit': '°C', 'label': 'Minimum Temperature'},
        'meantemp': {'value': 7.8, 'unit': '°C', 'label': 'Mean Temperature'},
        'heatdegdays': {'value': 10.2, 'unit': '°C', 'label': 'Heating Degree Days'},
        'cooldegdays': {'value': 0.0, 'unit': '°C', 'label': 'Cooling Degree Days'},
        'totalrain': {'value': 0.8, 'unit': 'mm', 'label': 'Total Rain'},
        'totalsnow': {'value': 0.0, 'unit': 'cm', 'label': 'Total Snow'},
        'totalprecipitation': {'value': 0.8, 'unit': 'mm', 'label': 'Total Precipitation'},
        'snowonground': {'value': None, 'label': 'Snow on Ground'},
        'dirofmaxgust': {'value': 27, 'unit': '10s Deg', 'label': 'Direction of Maximum Gust'},
        'speedofmaxgust': {'value': 68, 'unit': 'km/h', 'label': 'Speed of Maximum Gust'}
    }
}

# Extract relevant data
weatherDays = []

for date, values in data.items():
    w: Wind = (values['dirofmaxgust']['value'], values['speedofmaxgust']['value'])
    t: Temp = (values['maxtemp']['value'], values['mintemp']['value'], values['meantemp']['value'])
    weatherDays.append(
        WeatherDay(
            datetime.datetime.strptime(date, "%Y-%m-%d"), 
            w,
            t
        )
    )


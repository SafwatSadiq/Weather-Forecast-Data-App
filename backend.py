import requests
import pandas as pd
import os

API = os.getenv('Weather_API')


def get_data(place, forecast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API}"
    response = requests.get(url)
    data = response.json()
    filtered_datas = []
    dates = []
    for i in range(forecast_days * 8):
        if kind == 'Temperature':
            filtered_data = round(data['list'][i]['main']['temp'] - 273, 2)
        if kind == 'Sky':
            filtered_data = data['list'][i]['weather'][0]['main']
        filtered_datas.append(filtered_data)
        date = data['list'][i]['dt_txt']
        dates.append(date)
    return filtered_datas, dates

if __name__ == '__main__':
    print(get_data('dhaka', 5, 'Sky'))
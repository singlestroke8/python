import requests

def weather_command():
    base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    city_code = '130010'
    url = '{}?city={}'.format(base_url, city_code)
    r = requests.get(url)
    weather_data = r.json()
    # 都市名
    city = weather_data['location']['city']
    # 日付
    label = weather_data['forecasts'][0]['dateLabel']
    # 天気
    telop = weather_data['forecasts'][0]['telop']
    # 最高気温
    temperature_max = weather_data['forecasts'][0]['temperature']['max']

    response = '{}の{}の天気は「{}」、最高気温は{}です。'.format(city, label, telop, temperature_max)
    return response
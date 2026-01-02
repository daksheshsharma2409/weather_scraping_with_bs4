from bs4 import BeautifulSoup
import requests

def weather(city_code):
    pre_link = "https://weather.com/en-IN/weather/today/l/"
    city_code = city_code.strip()
    link = pre_link + city_code
    return link

def getWeather(link):
    html_code = requests.get(link).text

    soup = BeautifulSoup(html_code, 'lxml')

    location = soup.find('h1','CurrentConditions--location--yub4l').text.strip()
    time = soup.find('span','CurrentConditions--timestamp--LqnOd').text[6:].strip()
    temp = soup.find('span','CurrentConditions--tempValue--zUBSz').text.strip()
    cond = soup.find('div','CurrentConditions--phraseValue---VS-k').text.strip()
    feels_like = soup.find('span', 'TodayDetailsCard--feelsLikeTempValue--8WgHV').text.strip()
    sun = soup.find_all('p', 'TwcSunChart--dateValue--TzXBr')
    sun_rise = sun[0].text.strip()
    sun_set = sun[1].text.strip()

    det = soup.find_all('div', 'WeatherDetailsListItem--wxData--lW-7H')

    high_low = det[0].text.strip()
    wind = det[1].text.strip()
    humidity = det[2].text.strip()
    pressure = det[4].text.strip()

    aqi = soup.find('text', 'DonutChart--innerValue--VRvST AirQuality--innerValueLowerTextSize--rwyJM').text.strip()
    aqi_det = soup.find('span', 'AirQualityText--severity--jiW+F').text.strip()
    aqi_para = soup.find('p', 'AirQualityText--severityText--7Tout').text.strip()

    print(f"{location} \nAs per {time} \n{temp} [{cond}] \n")
    print(f"Feels Like : {feels_like}")
    print(f"Sun Rise : {sun_rise}")
    print(f"Sun Set : {sun_set}")
    print(f"High/Low : {high_low}")
    print(f"Wind : {wind}")
    print(f"Humidity : {humidity}")
    print(f"Pressure : {pressure} \n")

    print(f"AQI : {aqi} [{aqi_det}]")
    print(aqi_para)

def main():
    locations_text = open('locations.txt', 'r').read()
    locations = locations_text.split()
    for location in locations:
        link = weather(location)
        getWeather(link)
        print("\n\n")

if __name__ == '__main__':
    main()
from bs4 import BeautifulSoup
import requests
import os
import sys

#Get your 64 character location id from weather.com
#From this format https://weather.com/en-IN/weather/today/l/[weather-id]
#copy the weather-id put it in new line in locations.txt

def weather(city_code):
    pre_link = "https://weather.com/en-IN/weather/today/l/"
    city_code = city_code.strip()
    link = pre_link + city_code
    return link

def getWeather(link):
    try:
        html_code = requests.get(link, timeout=10).text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return

    soup = BeautifulSoup(html_code, 'lxml')

    try:
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
    except (AttributeError, IndexError) as e:
        print(f"Error parsing weather data. The website structure may have changed or the location ID is invalid.")
        return

def main():
    if not os.path.exists('locations.txt'):
        with open('locations.txt', 'w') as f:
            f.write('')
        print("locations.txt was created. Please add your location IDs (one per line) and run the script again.")
        sys.exit(0)
    
    try:
        with open('locations.txt', 'r') as f:
            locations_text = f.read()
    except IOError as e:
        print(f"Error reading locations.txt: {e}")
        sys.exit(1)
    
    locations = locations_text.split()
    
    if not locations:
        print("No locations found in locations.txt. Please add location IDs (one per line) and run the script again.")
        sys.exit(0)
    
    for location in locations:
        if location.strip():
            link = weather(location)
            getWeather(link)
            print("\n\n")

if __name__ == '__main__':
    main()
import requests
import json
 
website_url = "https://www.metaweather.com"
search_api = "/api/location/search/?query={}"
 
city = input("What is your city: ")
 
search_api_city = search_api.format(city)
search_api_final_link = website_url + search_api_city
 
website_data = requests.get(search_api_final_link).content
 
parsed_data = json.loads(website_data)
 
city_id = parsed_data[0]["woeid"]
 
weather_link = f"{website_url}/api/location/{city_id}/"
 
weather_data_dump = requests.get(weather_link).content
parsed_weather_data = json.loads(weather_data_dump)
weather_consolidated_data = parsed_weather_data["consolidated_weather"]
 
 
def general_weather_outlook(weather):
    if weather == "Clear":
        weather_outlook = "All clear today!"
    elif weather == "Light Cloud":
        weather_outlook = "It's a little cloudy today"
    elif weather == "Heavy Cloud":
        weather_outlook = "It's really cloudy today"
    elif weather == "Showers":
        weather_outlook = "Careful! It might rain today!"
    elif weather == "Light Rain":
        weather_outlook = "Don't forget your umbrella"
    elif weather == "Heavy Rains":
        weather_outlook = "Work from home!!"
    return weather_outlook
 
def heat(temp):
    if temp > 35:
        heat_outlook = "AC ke bahar mat nikalna"
    elif temp < 20:
        heat_outlook = "Bhai bhot thand hai"
    else:
        heat_outlook = "Perfect temperature!"
    return heat_outlook
 
def humidity(rel_humid):
    if rel_humid > 70:
        humidity_outlook = "Prepare for paseeeena!"
    elif rel_humid < 30:
        humidity_outlook = "Parched! Parched!"
    else:
        humidity_outlook = "Ideal humidity!"
    return humidity_outlook
 
def windiness(windspeed):
    if windspeed > 10:
        wind_outlook = "Toofan!"
    elif windspeed < 5:
        wind_outlook = "No hawa"
    else:
        wind_outlook = "Mand mand pawan"
    return wind_outlook
 
 
general_weather = weather_consolidated_data[0]["weather_state_name"]
max_temp =  weather_consolidated_data[0]["max_temp"]
min_temp =  weather_consolidated_data[0]["min_temp"]
wind_speed =  weather_consolidated_data[0]["wind_speed"]
humid =  weather_consolidated_data[0]["humidity"]
 
weather_message = general_weather_outlook(general_weather)
heat_message = heat(max_temp)
humidity_message = humidity(humid)
wind_message = windiness(wind_speed)
 
print(weather_message)
print(heat_message)
print(humidity_message)
print(wind_message)
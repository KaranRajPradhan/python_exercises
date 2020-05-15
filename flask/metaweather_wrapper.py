import requests

def get_data_from_metaweather():
    link = "https://www.metaweather.com/api/location/2295420/"
    json_data = requests.get(link).json()
    return json_data

def main():
    json_data = get_data_from_metaweather()
    consolidated_weather = json_data["consolidated_weather"]
    weather_list = []
    #weather = 0,1,2,3,4...
    for weather in consolidated_weather:
        weather_dict = {}
        weather_dict["date"] = weather["applicable_date"]
        weather_dict["min"] = weather["min_temp"]
        weather_dict["max"] = weather["max_temp"]
        weather_dict["counter"] = consolidated_weather.index(weather)

        weather_list.append(weather_dict)

    return weather_list

if __name__ == "__main__":
    result = main()
    print(result)
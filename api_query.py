import requests
import json
from datetime import datetime

f = open("tokens.json")
file = json.load(f)
TOKEN = file['discord']
accu_TOKEN = file['accuweather']
f.close()

async def query_accuweather_location_details(location):
    try:
        # get_query = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=" + accu_TOKEN + "&q="

        # split_query = location.split(" ")

        # for i in split_query:
        #     get_query = get_query + i +  "%20"

        #get_query = get_query[:-3]
        
        #response = requests.get(get_query).json()
        
        #return response
        return [{'Version': 1, 'Key': '337155', 'Type': 'City', 'Rank': 65, 'LocalizedName': 'Mill Valley', 'Country': {'ID': 'US', 'LocalizedName': 'United States'}, 'AdministrativeArea': {'ID': 'CA', 'LocalizedName': 'California'}}, {'Version': 1, 'Key': '2627279', 'Type': 'City', 'Rank': 85, 'LocalizedName': 'Mill Valley', 'Country': {'ID': 'US', 'LocalizedName': 'United States'}, 'AdministrativeArea': {'ID': 'WI', 'LocalizedName': 'Wisconsin'}}]
        
        
    except Exception as e:
        print("api_query")
        return "Not handled! Error in getting location details"




async def query_accuweather_current_conditions(location_key):
    try:
        get_query = "http://dataservice.accuweather.com/currentconditions/v1/"+ str(location_key) + "?&apikey=" + accu_TOKEN + "&details=true"
        #response = requests.get(get_query).json()
        response = {'LocalObservationDateTime': '2024-08-10T10:07:00-07:00',
 'EpochTime': 1723309620,
 'WeatherText': 'Mostly cloudy',
 'WeatherIcon': 6,
 'HasPrecipitation': False,
 'PrecipitationType': None,
 'IsDayTime': True,
 'Temperature': {'Metric': {'Value': 18.2, 'Unit': 'C', 'UnitType': 17},
  'Imperial': {'Value': 65.0, 'Unit': 'F', 'UnitType': 18}},
 'RealFeelTemperature': {'Metric': {'Value': 21.8,
   'Unit': 'C',
   'UnitType': 17,
   'Phrase': 'Pleasant'},
  'Imperial': {'Value': 71.0,
   'Unit': 'F',
   'UnitType': 18,
   'Phrase': 'Pleasant'}},
 'RealFeelTemperatureShade': {'Metric': {'Value': 18.8,
   'Unit': 'C',
   'UnitType': 17,
   'Phrase': 'Pleasant'},
  'Imperial': {'Value': 66.0,
   'Unit': 'F',
   'UnitType': 18,
   'Phrase': 'Pleasant'}},
 'RelativeHumidity': 87,
 'IndoorRelativeHumidity': 78,
 'DewPoint': {'Metric': {'Value': 16.1, 'Unit': 'C', 'UnitType': 17},
  'Imperial': {'Value': 61.0, 'Unit': 'F', 'UnitType': 18}},
 'Wind': {'Direction': {'Degrees': 248, 'Localized': 'WSW', 'English': 'WSW'},
  'Speed': {'Metric': {'Value': 4.6, 'Unit': 'km/h', 'UnitType': 7},
   'Imperial': {'Value': 2.9, 'Unit': 'mi/h', 'UnitType': 9}}},
 'WindGust': {'Speed': {'Metric': {'Value': 6.3,
    'Unit': 'km/h',
    'UnitType': 7},
   'Imperial': {'Value': 3.9, 'Unit': 'mi/h', 'UnitType': 9}}},
 'UVIndex': 3,
 'UVIndexText': 'Moderate',
 'Visibility': {'Metric': {'Value': 24.1, 'Unit': 'km', 'UnitType': 6},
  'Imperial': {'Value': 15.0, 'Unit': 'mi', 'UnitType': 2}},
 'ObstructionsToVisibility': '',
 'CloudCover': 81,
 'Ceiling': {'Metric': {'Value': 1707.0, 'Unit': 'm', 'UnitType': 5},
  'Imperial': {'Value': 5600.0, 'Unit': 'ft', 'UnitType': 0}},
 'Pressure': {'Metric': {'Value': 1014.2, 'Unit': 'mb', 'UnitType': 14},
  'Imperial': {'Value': 29.95, 'Unit': 'inHg', 'UnitType': 12}},
 'PressureTendency': {'LocalizedText': 'Falling', 'Code': 'F'},
 'Past24HourTemperatureDeparture': {'Metric': {'Value': 4.1,
   'Unit': 'C',
   'UnitType': 17},
  'Imperial': {'Value': 7.0, 'Unit': 'F', 'UnitType': 18}},
 'ApparentTemperature': {'Metric': {'Value': 20.0,
   'Unit': 'C',
   'UnitType': 17},
  'Imperial': {'Value': 68.0, 'Unit': 'F', 'UnitType': 18}},
 'WindChillTemperature': {'Metric': {'Value': 18.3,
   'Unit': 'C',
   'UnitType': 17},
  'Imperial': {'Value': 65.0, 'Unit': 'F', 'UnitType': 18}},
 'WetBulbTemperature': {'Metric': {'Value': 17.0, 'Unit': 'C', 'UnitType': 17},
  'Imperial': {'Value': 63.0, 'Unit': 'F', 'UnitType': 18}},
 'WetBulbGlobeTemperature': {'Metric': {'Value': 19.7,
   'Unit': 'C',
   'UnitType': 17},
  'Imperial': {'Value': 67.0, 'Unit': 'F', 'UnitType': 18}},
 'Precip1hr': {'Metric': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
  'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}},
 'PrecipitationSummary': {'Precipitation': {'Metric': {'Value': 0.0,
    'Unit': 'mm',
    'UnitType': 3},
   'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}},
  'PastHour': {'Metric': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
   'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}},
  'Past3Hours': {'Metric': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
   'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}},
  'Past6Hours': {'Metric': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
   'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}},
  'Past9Hours': {'Metric': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
   'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}},
  'Past12Hours': {'Metric': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
   'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}},
  'Past18Hours': {'Metric': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
   'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}},
  'Past24Hours': {'Metric': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
   'Imperial': {'Value': 0.0, 'Unit': 'in', 'UnitType': 1}}},
 'TemperatureSummary': {'Past6HourRange': {'Minimum': {'Metric': {'Value': 8.0,
     'Unit': 'C',
     'UnitType': 17},
    'Imperial': {'Value': 46.0, 'Unit': 'F', 'UnitType': 18}},
   'Maximum': {'Metric': {'Value': 18.2, 'Unit': 'C', 'UnitType': 17},
    'Imperial': {'Value': 65.0, 'Unit': 'F', 'UnitType': 18}}},
  'Past12HourRange': {'Minimum': {'Metric': {'Value': 8.0,
     'Unit': 'C',
     'UnitType': 17},
    'Imperial': {'Value': 46.0, 'Unit': 'F', 'UnitType': 18}},
   'Maximum': {'Metric': {'Value': 18.2, 'Unit': 'C', 'UnitType': 17},
    'Imperial': {'Value': 65.0, 'Unit': 'F', 'UnitType': 18}}},
  'Past24HourRange': {'Minimum': {'Metric': {'Value': 8.0,
     'Unit': 'C',
     'UnitType': 17},
    'Imperial': {'Value': 46.0, 'Unit': 'F', 'UnitType': 18}},
   'Maximum': {'Metric': {'Value': 22.4, 'Unit': 'C', 'UnitType': 17},
    'Imperial': {'Value': 72.0, 'Unit': 'F', 'UnitType': 18}}}},
 'MobileLink': 'http://www.accuweather.com/en/us/mill-valley-ca/94941/current-weather/337155?lang=en-us',
 'Link': 'http://www.accuweather.com/en/us/mill-valley-ca/94941/current-weather/337155?lang=en-us'}
        output_parsing = {
            "weather_icon": response['WeatherIcon'],
            "weather_description": response['WeatherText'],
            "is_raining": response['HasPrecipitation'],
            "rain_type": response['PrecipitationType'],
            "temperature": response['Temperature']['Imperial']['Value'],
            "feeling": response['RealFeelTemperature']['Imperial']['Phrase'],
            "humidity": response['RelativeHumidity'],
            "obstructions_to_visibility": response['ObstructionsToVisibility'],
            "cloud_cover": response["Ceiling"]["Imperial"]["Value"],
            "windchill": response["WindChillTemperature"]["Imperial"]["Value"],
            "precipitation_summary": response['PrecipitationSummary']["Precipitation"]["Imperial"]["Value"],
            "link": response['Link']
        }
        
        return output_parsing
    except Exception as e :
        print("ERROR")
        print(e)
        return "Not handled! Error in getting current weather conditions {e}"    

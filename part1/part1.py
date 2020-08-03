import json
from datetime import datetime

with open("/Users/rebeccamillwood/Desktop/She Codes /GitHub/python_project/part1/data/forecast_5days_a.json") as json_file:
    forecast_5days_a = json.load(json_file)
# print(forecast_5days_a)

# for key, value in forecast_5days_a.items():
#     for key1, value1 in value.items():
#         print()
#         print(key1, value1)

for data in forecast_5days_a["DailyForecasts"]:
    date = data["Date"]
    minTemp = data["Temperature"]["Minimum"]["Value"]
    maxTemp = data["Temperature"]["Maximum"]["Value"]
    daytime = data["Day"]["LongPhrase"]
    RainProbDay = data["Day"]["RainProbability"]
    nighttime = data["Night"]["LongPhrase"]
    RainProbNight = data["Night"]["RainProbability"]  

    print(date, minTemp, maxTemp, daytime, RainProbDay, nighttime, RainProbNight)




DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius.
    """
    pass

# def convert_f_to_c(temp_in_farenheit):
    # farenheit = float(temp_in_farenheit)
    # celsius = (farenheit - 32) * (5/9)
    # print(celsius)

# temp_in_farenheit = ??

# convert_f_to_c(temp_in_farenheit)


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    pass

# def calculate_mean(total, num_items):
#     mean = (total/num_items)
#     print(mean)

# num_items = ??
# total = ??

# calculate_mean(total, num_items)

def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    pass


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))






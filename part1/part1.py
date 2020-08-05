import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(date):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")



def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    farenheit = float(temp_in_farenheit)
    celsius = (farenheit - 32) * (5/9)
    print(f"{celsius:.1f}")

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

    with open(forecast_file) as json_file:
        forecast_5days_a = json.load(json_file)


    for data in forecast_5days_a["DailyForecasts"]:
        date = data["Date"]
        minTemp = data["Temperature"]["Minimum"]["Value"]
        maxTemp = data["Temperature"]["Maximum"]["Value"]
        daytime = data["Day"]["LongPhrase"]
        RainProbDay = data["Day"]["RainProbability"]
        nighttime = data["Night"]["LongPhrase"]
        RainProbNight = data["Night"]["RainProbability"]  
        a = ""
        print(f"--------{date}--------")
        print(f"Miniumum Temperature: {minTemp}")
        print(f"Maximum Temperature: {maxTemp}")
        print(f"Daytime: {daytime}")
        print(f"{a:>2}Chance of Rain: {RainProbDay}%")
        print(f"Nighttime: {nighttime}")
        print(f"{a:>2}Chance of Rain: {RainProbNight}%")
        print()
        print(convert_date(date))
        minTempFormat = format_temperature(convert_f_to_c(minTemp))
        maxTempFormat = format_temperature(convert_f_to_c(maxTemp))


    # print(f"5 Day Overview")
    # print(f"{a:>3}The lowest temperature will be {minTemp}, and will occure on {date}.")
    # print(f"{a:>3}The highest temperature will be {maxTemp}, and will occure on {date}.")
    # print(f"{a:>3}The average low this week is {minTemp}.")
    # print(f"{a:>3}The average high this week is {maxTemp}.")
    # print()

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))






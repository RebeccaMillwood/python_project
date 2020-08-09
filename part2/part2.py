import json
from datetime import datetime
import plotly.express as px
import pandas as pd

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
    celsius = round((farenheit - 32) * (5/9),1)
    return celsius

dates = []
minimum_temps = []
maximum_temps = []
minimum_realfeel_temps = []
minimum_realfeelshade_temps = []

# dataframe = {}

with open("data/forecast_5days_a.json") as json_file:
    forecast_5days_a = json.load(json_file)

for data in forecast_5days_a["DailyForecasts"]:
    date = convert_date(data["Date"])
    dates.append(date)   

    minTemp = convert_f_to_c(data["Temperature"]["Minimum"]["Value"])
    minTempFormat = format_temperature(minTemp)
    minimum_temps.append(minTemp)

    maxTemp = convert_f_to_c(data["Temperature"]["Maximum"]["Value"])
    maxTempFormat = format_temperature(maxTemp)
    maximum_temps.append(maxTemp)

    minRealFeel = convert_f_to_c(data["RealFeelTemperature"]["Minimum"]["Value"])
    minRealFeelFormat = format_temperature(minRealFeel)
    minimum_realfeel_temps.append(minRealFeel)

    minRealFeelShade = convert_f_to_c(data["RealFeelTemperatureShade"]["Minimum"]["Value"])
    minRealFeelShadeFormat = format_temperature(minRealFeelShade)
    minimum_realfeelshade_temps.append(minRealFeelShade)

# print(dates)
# print(minimum_temps)
# print(maximum_temps)
# print(minimum_realfeel_temps)
# print(minimum_realfeelshade_temps)

# graph 1: min and max temps for each day

dataframe1 = {
    "minimum": minimum_temps,
    "maximum": maximum_temps,
    "date": dates
}

fig = px.bar(
    dataframe1,
    y=["minimum", "maximum"],
    x="date",
    barmode="group"
)

fig.show() 

# graph 2: min, min "real feel", and min "real feel shade" temps

dataframe1 = {
    "minimum": minimum_temps,
    "minimum real feel": minimum_realfeel_temps,
    "minimum real feel shade": minimum_realfeelshade_temps,
    "date": dates
}

fig = px.bar(
    dataframe1,
    y=["minimum", "minimum real feel", "minimum real feel shade"],
    x="date",
    barmode="group"
)

fig.show() 

# convert date
# convert temp
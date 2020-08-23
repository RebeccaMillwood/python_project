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
minimum_real_feel_temps = []
minimum_real_feel_shade_temps = []

# dataframe = {}

with open("data/forecast_5days_a.json") as json_file:
    forecast_5days_a = json.load(json_file)

for data in forecast_5days_a["DailyForecasts"]:
    date = convert_date(data["Date"])
    dates.append(date)   

# with open("data/forecast_5days_b.json") as json_file:
#     forecast_5days_b = json.load(json_file)

# for data in forecast_5days_b["DailyForecasts"]:
#     date = convert_date(data["Date"])
#     dates.append(date)   

# with open("data/forecast_8days.json") as json_file:
#     forecast_8days = json.load(json_file)

# for data in forecast_8days["DailyForecasts"]:
#     date = convert_date(data["Date"])
#     dates.append(date)   

    min_temp = convert_f_to_c(data["Temperature"]["Minimum"]["Value"])
    min_temp_format = format_temperature(min_temp)
    minimum_temps.append(min_temp)

    max_temp = convert_f_to_c(data["Temperature"]["Maximum"]["Value"])
    max_temp_format = format_temperature(max_temp)
    maximum_temps.append(max_temp)

    min_real_feel = convert_f_to_c(data["RealFeelTemperature"]["Minimum"]["Value"])
    min_real_feel_format = format_temperature(min_real_feel)
    minimum_real_feel_temps.append(min_real_feel)

    min_real_feel_shade = convert_f_to_c(data["RealFeelTemperatureShade"]["Minimum"]["Value"])
    min_real_feel_shade_format = format_temperature(min_real_feel_shade)
    minimum_real_feel_shade_temps.append(min_real_feel_shade)

# print(dates)
# print(minimum_temps)
# print(maximum_temps)
# print(minimum_realfeel_temps)
# print(minimum_realfeelshade_temps)

# graph 1: min and max temps for each day

dataframe1 = {
    "Minimum": minimum_temps,
    "Maximum": maximum_temps,
    "Date": dates,
}

fig = px.line(
    dataframe1,
    y=["Minimum", "Maximum"],
    x="Date",
    labels={
        "value": "Temperature in Celsius",
        "variable": "Temperature",
    },
    title="Daily Forecast",
    template="plotly_dark",
)

fig.show() 

# graph 2: min, min "real feel", and min "real feel shade" temps

dataframe2 = {
    "Minimum": minimum_temps,
    "Minimum Real Feel": minimum_real_feel_temps,
    "Minimum Real Feel Shade": minimum_real_feel_shade_temps,
    "Date": dates
}

# fig = px.bar(
#     dataframe2,
#     y=["Minimum", "Minimum Real Feel", "Minimum Real Feel Shade"],
#     x="Date",
#     labels={
#         "value": "Temperature in Celsius",
#         "variable": "Temperature",
#     },
#     title="Daily Real Feel",
#     template="plotly_dark",
#     barmode="group"
# )

fig = px.line(
    dataframe2,
    y=["Minimum", "Minimum Real Feel", "Minimum Real Feel Shade"],
    x="Date",
    labels={
        "value": "Temperature in Celsius",
        "variable": "Temperature",
    },
    title="Daily Real Feel",
    template="plotly_dark",
)

fig.show() 

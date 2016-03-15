# -*- coding: utf-8 -*-

import datetime
import os
import pyowm
from app import config

CITY = "Ann Arbor"


def get_weather_description():
    api_key = os.environ.get("WEATHERMAP_KEY") or config['weather']['api_key']
    weather = pyowm.OWM(api_key)
    forecast = weather.three_hours_forecast(CITY)

    # Discard weather readings not from today
    today = datetime.datetime.today().day
    today_weather = []
    for w in forecast.get_forecast().get_weathers():
        date = datetime.datetime.fromtimestamp(w.get_reference_time())
        if date.day == today:
            today_weather.append(w)

    return weather_description(forecast, today_weather)


def weather_description(forecast, today_weather):
    stats = {
        "clouds": forecast.when_clouds(),
        "rain": forecast.when_rain(),
        "sun": forecast.when_sun(),
        "fog": forecast.when_fog(),
        "snow": forecast.when_snow()
    }

    # Discard weather readings not from today
    today = datetime.datetime.today().day
    for key in stats:
        today_weather = []
        for w in stats[key]:
            date = datetime.datetime.fromtimestamp(w.get_reference_time())
            if date.day == today:
                today_weather.append(w)
        stats[key] = today_weather

    weather_types = stats.keys()
    weather_types.sort(key=lambda t: len(stats[t]), reverse=True)

    high_temp = get_high(today_weather)

    t1_when = [x.get_reference_time() for x in stats[weather_types[0]]]
    t2_when = [x.get_reference_time() for x in stats[weather_types[1]]]
    t1_hours = [datetime.datetime.fromtimestamp(x).hour for x in t1_when]
    t2_hours = [datetime.datetime.fromtimestamp(x).hour for x in t2_when]

    weather_adjectives = {
        "clouds": "cloudy",
        "rain": "rainy",
        "sun": "sunny",
        "fog": "foggy",
        "snow": "snowing"
    }

    msg = ""
    if len(t1_hours) != 0:
        if len(t2_hours) == 0:
            msg = "and "

        msg = weather_adjectives[weather_types[0]]
        msg += " " + when_occuring(t1_when)

        if len(t2_hours) != 0:
            msg += ", and " + weather_adjectives[weather_types[1]]
            msg += " " + when_occuring(t2_when)
    else:
        return "The day will be great."

    return "Today in {0}, it'll be {1}°, {2}.".format(CITY, high_temp, msg)


def get_datetime_at_hour(hour):
    today = datetime.date.today()
    hour_time = datetime.time(hour)
    return datetime.datetime.combine(today, hour_time)


def when_occuring(times):
    morning = 0
    afternoon = 0
    evening = 0

    for time in times:
        hour = datetime.datetime.fromtimestamp(time).hour
        print hour
        if hour <= 11:
            morning += 1
        elif hour <= 16:
            afternoon += 1
        else:
            evening += 1

    number_nonzero = len([x for x in [morning, afternoon, evening] if x != 0])
    if number_nonzero == 0:
        return ""
    elif number_nonzero == 1:
        if morning:
            return "in the morning"
        if afternoon:
            return "in the afternoon"
        if evening:
            return "in the evening"
    elif number_nonzero == 2:
        if morning and afternoon:
            return "in the morning and afternoon"
        if morning and evening:
            return "in the morning and evening"
        if afternoon and evening:
            return "in the afternoon and evening"
    else:
        return "all day"


def get_high(today_weather):
    if len(today_weather) == 0:
        return "?"
    kelvin = max([x.get_temperature()['temp_max'] for x in today_weather])
    return int((kelvin - 273.15) * 1.8 + 32)

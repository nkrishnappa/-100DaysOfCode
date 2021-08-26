# Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit
#  f = c * 9/5 + 32
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = { day:(celcius * 9/5 + 32) for day, celcius in weather_c.items() }
import json
print(json.dumps(weather_f, indent=2))
# {
#   "Monday": 53.6,
#   "Tuesday": 57.2,
#   "Wednesday": 59.0,
#   "Thursday": 57.2,
#   "Friday": 69.8,
#   "Saturday": 71.6,
#   "Sunday": 75.2
# }

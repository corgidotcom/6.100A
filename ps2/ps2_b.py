# 6.100A Fall 2025
# Problem Set 2: Part B
# Name: Gabriel Zendejas
# Collaborators: None
# Time Spent: 00:10


############################################################
# Global variables
# Prior to running `test_ps2_student.py`, please comment
# these variables out!

# daily_forecast = "sunny cloudy rainy sunny sunny"
############################################################


############################################################
# Count each type of forecast
############################################################

# Your code here

# Initalize all necessary variables
countSunny = 0
countCloudy = 0
countRainy = 0
countPartlyCloudy = 0

# Create a temp string containing all the daily forecasts, then initialize currentforecast as the first forecast in that string
tempForecast = daily_forecast
currentForecast = daily_forecast[0: tempForecast.find(" ")]

# Iterate through each forecast, which is equal to the number of spaces in daily_forecast plus one
for i in range(daily_forecast.count(" ") + 1):
    if(currentForecast == "sunny"):
        countSunny += 1
    if(currentForecast == "cloudy"):
        countCloudy += 1
    if(currentForecast == "rainy"):
        countRainy += 1
    if(currentForecast == "partly_cloudy"):
        countPartlyCloudy += 1

    # Update the tempForecast string to remove the forecast we just checked to avoid double counting
    tempForecast = tempForecast[tempForecast.find(" ") + 1:]
    if(tempForecast.count(" ") > 0):
        currentForecast = tempForecast[:tempForecast.find(" ")]
    else:
        # This condition runs on the last forecast contained in tempForecast
        currentForecast = tempForecast

# Print Results
print("Sunny count: " + str(countSunny))
print("Cloudy count: " + str(countCloudy))
print("Rainy count: " + str(countRainy))
print("Partly cloudy count: " + str(countPartlyCloudy))




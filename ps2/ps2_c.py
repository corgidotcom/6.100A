# 6.100A Fall 2025
# Problem Set 2: Part C
# Name: Gabriel Zendejas
# Collaborators: PyTutor
# Time Spent: 0:10


############################################################
# Global variables
# Prior to running `test_ps2_student.py`, please comment
# these variables out!

# daily_forecast = "sunny cloudy sunny sunny sunny"
############################################################


############################################################
# Find the longest continuous sunny streak
############################################################

# Your code here

# Initialize necessary variables
tempforecast = daily_forecast
nextword = tempforecast[0:tempforecast.find(" ")]
currentStreak = 0
longestStreak = 0

# Iterates through every forecast in daily_forecast
for i in range(daily_forecast.count(" ") + 1):
    # Checks if the current word is "sunny"
    if(nextword == "sunny"):
        currentStreak += 1
        if(currentStreak > longestStreak):
            # Updates the longest streak
            longestStreak = currentStreak
    else:
        # Once another word is detected, resets the current streak
        currentStreak = 0

    # Updates the tempforecast string to remove the forecast that was just checked
    tempforecast = tempforecast[tempforecast.find(" ") + 1:]
    if(tempforecast.count(" ") > 0):
        nextword = tempforecast[0:tempforecast.find(" ")]
    else:
        nextword = tempforecast

# Print result       
print("Longest continuous sunny streak: " + str(longestStreak))
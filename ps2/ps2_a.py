# 6.100A Fall 2025
# Problem Set 2: Part A
# Name: Gabriel Zendejas
# Collaborators: PyTutor
# Time Spent: 00:10


############################################################
# Global variables
# Prior to running `test_ps2_student.py`, please comment
# these variables out!

# temps = "75.2 76.9 75.2 78.4 79.2 75.2 81.5 82.1 77.1 77.1"
# min_temp = 75
# max_temp = 82
############################################################


############################################################
# Determining the mode with custom temperature binning
############################################################

# Your code here

# Initialize necessary variables
tempTemps = temps
currentTemp = tempTemps[0: tempTemps.find(" ")]
binCount = 0
maxBinCount = 0
maxBin = min_temp


# Iterate through every integer temp between min_temp and max_temp inclusive
for i in range(min_temp, max_temp + 1):
    # Iterate through every temperature in "temps" for every bin
    for j in range(temps.count(" ") + 1):
        # If the current temperature being checked rounds to the current bin, add one to the current bincount and update the maximum
        if(int(float(currentTemp) + 0.5) == i):
            binCount += 1
            if(binCount >= maxBinCount):
                maxBinCount = binCount
                maxBin = i
        # Update the temps string by removing the temperature we just checked, and set the next temperature equal to currentTemp
        tempTemps = tempTemps[tempTemps.find(" ") + 1:]
        if(tempTemps.count(" ") > 0):
            currentTemp = tempTemps[: tempTemps.find(" ")]
        else:
            currentTemp = tempTemps
    # Before iterating through the next bin, reset all necessary variables
    binCount = 0
    tempTemps = temps
    currentTemp = tempTemps[0: tempTemps.find(" ")]
print("Mode bin rounded temperature: " + str(maxBin))
print("Count: " + str(maxBinCount))


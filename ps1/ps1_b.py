# 6.100A Fall 2025
# Problem Set 1: Part B
# Name: Gabriel Zendejas
# Collaborators: PyTutor
# Time Spent: 4:00:00 (roughly?)

############################################################
# Global variables
# Prior to running `test_ps1_student.py`, please comment
# these variables out!

# To be used for all three parts
# dates = "2024-08-01 2024-08-02 2024-08-03 2024-08-04 2024-08-05 2024-08-06 2024-08-07 2024-08-08 2024-08-09 2024-08-10"
# temperatures = "75.2 77.1 74.6 78.4 79.2 80.3 81.5 82.1 76.3 77.7"


# To be used in third part
# target_temp = 78.0
# start_date = "2024-08-02" 
# end_date = "2024-08-06" 
############################################################


############################################################
# Complex String Processing
############################################################


# Task 1: Calculate the Average Temperature
# Your code here
total = 0
count = 0
temp1 = temperatures
for i in range(temp1.count(" ")+1):
    spaceindex = temp1.find(" ")
    if(spaceindex != -1):
        total += float(temp1[:temp1.find(" ")])
    else:
        total += float(temp1)
    temp1 = temp1[temp1.find(" ")+1:]
    count += 1
print(f'Average temperature: {total/count}')


# Part 2: Calculate the Maximum and Minimum Temperatures
# Your code here
maxTemp = 0
minTemp = 100000000000
temp2 = temperatures
for i in range(temp2.count(" ") + 1):
    spaceindex = temp2.find(" ")
    if(spaceindex != -1):
        newTemp = float(temp2[:temp2.find(" ")])
        if(newTemp > maxTemp):
            maxTemp = newTemp
        if(newTemp < minTemp):
            minTemp = newTemp
    else:
        newTemp = float(temp2)
        if(newTemp > maxTemp):
            maxTemp = newTemp
        if(newTemp < minTemp):
            minTemp = newTemp
    temp2 = temp2[temp2.find(" ")+1:]
print(f'Maximum temperature: {maxTemp}')
print(f'Minimum temperature: {minTemp}')

# Part 3: Finding the Closest Temperature (with a Guess-and-Check Approach)
# Your code here
def find(targetstring, targetcharacter, targetcount):
    if(targetcount == 0):
        return(-1)
    if(targetcount == targetstring.count(targetcharacter) + 1):
        return(len(targetstring))
    return_index = -1
    count = 0
    for index in range(len(targetstring)):
        if targetstring[index] == targetcharacter:
            return_index = index
            count += 1
            if(count == targetcount):
                return(return_index)
    return(return_index)

posOfStartDate = dates.find(start_date)
posOfEndDate = dates.find(end_date) + len(end_date)
if(posOfStartDate == -1 and posOfEndDate == len(end_date) - 1):
    dateRange = dates
    beginIndex = 0
    endIndex = dates.count(" ")
elif(posOfStartDate == -1):
    dateRange = dates[:posOfEndDate]
    beginIndex = 0
    endIndex = dateRange.count(" ")
elif(posOfEndDate == len(end_date) - 1):
    dateRange = dates[posOfStartDate:]
    beginIndex = dates[:posOfStartDate].count(" ")
    endIndex = dateRange.count(" ") + beginIndex
else:
    dateRange = dates[posOfStartDate: posOfEndDate]
    beginIndex = dates[:posOfStartDate].count(" ")
    endIndex = dateRange.count(" ") + beginIndex

posOfStartTemp = find(temperatures, " ", beginIndex) + 1
posOfEndTemp = find(temperatures, " ", endIndex + 1)
tempRange = temperatures[posOfStartTemp:posOfEndTemp]

minDiff = 100000000
closestTemp = 0
for i in range(tempRange.count(" ") + 1):
    tempSpaceIndex = tempRange.find(" ")
    dateSpaceIndex = dateRange.find(" ")
    if(tempSpaceIndex != -1):
        newTemp = float(tempRange[:tempSpaceIndex])
        newDate = dateRange[:dateSpaceIndex]
    else:
        newTemp = float(tempRange)
        newDate = dateRange
    if(abs(target_temp - newTemp) < minDiff):
        closestTemp = newTemp
        closestDate = newDate
        minDiff = abs(target_temp - newTemp)
    tempRange = tempRange[tempSpaceIndex+1:]
    dateRange = dateRange[dateSpaceIndex+1:]
print("Date with closest temperature: " + str(closestDate))
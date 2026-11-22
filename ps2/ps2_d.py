# 6.100A Fall 2025
# Problem Set 2: Part D
# Name: Gabriel Zendejas
# Collaborators: PyTutor
# Time Spent: 0:20


############################################################
# Global variables
############################################################
# Bisection search_parameters
# Prior to running `test_ps2_student.py`, please comment
# these variables out!

# low = 50.0
# high = 100.0
# epsilon = 0.00001
# temperature = 82.0 # bisection search should output humidity of 85
# heat_threshold = 90.0
############################################################
# Constants for the heat index formula
# Be sure to leave these variables uncommented when running
# `test_ps2_student.py`!

c1 = -42.379
c2 = 2.04901523
c3 = 10.14333127
c4 = -0.22475541
c5 = -0.00683783
c6 = -0.05481717
c7 = 0.00122874
c8 = 0.00085282
c9 = -0.00000199
############################################################


############################################################
# Estimating the heat warning threshold using bisection search
############################################################
# Your code here


T = temperature
mid = (high + low)/2
while((high - low)/2 > epsilon):
    currentGuess = c1 + c2*T + c3*mid + c4*T*mid + c5*T**2 + c6*mid**2 + c7*mid*T**2 + c8*T*mid**2 + c9*(mid**2)*(T**2)
    if(currentGuess > heat_threshold):
        high = mid
    else:
        low = mid
    mid = (high + low)/2
print("Relative humidity threshold:", int(mid+0.5))
   
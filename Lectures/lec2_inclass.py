###############################################
a = 33
b = 88

# Manipulate a and b to print "3388"

print(str(a) + str(b))

###############################################
love = "I love pizza"
n = 4
time = "times a day"

# Use one print statement to print 
# "I love pizzapizzapizza 4 times a day" 
# by manipulating the variables given. Eg. slicing and concatenating.

print(love + 2*love[7:12] + love[1] + str(n) + love[1] + time)

###############################################
# Ask the user for a noun, verb, and adjective. Use the user input 
# to print a short story. Eg. The [insert adjective here] and small 
# [insert noun here] was so happy to finally [insert verb here] outside today.

noun = input("Insert a noun: ")
verb = input("Insert a verb: ")
adjective = input("Insert an adjective: ")

print("The " + noun + " jumped up in excitement when he heard there would be " + verb + " happening at the " + adjective + " function.")

###############################################
# Ask the user for a name and two numbers. Use the user input to print 
# a short story. Eg. I played [insert one number here] hours of video 
# games last year and my friend [insert name here] played 
# [insert other number here]. That's [insert sum of numbers here] total hours!

name = input("Insert a name: ")
num1 = int(input("Input Number 1: "))
num2 = int(input("Input Number 2: "))

print("I was up so late last night because my roommate " + name + " spent " + str(num1) + " hours psetting!! I only got " + str(num2) + " hours of sleep")


###############################################
# Read in two numbers from the user. Write code that prints 
# True if both numbers are positive and False otherwise.

number1 = int(input("Insert a number: "))
number2 = int(input("Insert a number: "))

if(number1 > 0 and number2 > 0):
    print("True")
else:
    print("False")

###############################################
# Read in two names from the user. Print True if the first character 
# of both names is uppercase and False otherwise.

name1 = input("Insert a name: ")
name2 = input("Insert a name: ")

if(name1[0].isupper() and name2[0].isupper()):
    print("True")
else:
    print("False")
###############################################
# What does this print?
# n1 = 3 # try 3
# n2 = 3 # try 4
# if n1 <= n2:
#     print("...and equal")
# elif n1 < n2:
#     print("tiny n1")
# elif n2 < n1:
#     print("baby n2")
# else:
#     print("what's this for?")


###############################################
# Assume you're given 2 int variables: n1 and n2. Print "both" if they 
# are both positive, "only one" if only one of them is positive, 
# and "neither" if neither are positive.


###############################################
# Assume you're given 2 int variables: n1 and n2. Print "both" if they 
# both have a 0 as one of their digits, "only one" if only one of them 
# has a 0, and "neither" if neither has a 0.


###############################################
# Assume you're given 2 int variables: n1 and n2. If both are positive, print the 
# sum of the first digits in each. If both are negative, print the sum of the 
# last digits in each. If only one is positive and the other is not, print the 
# result when you divide the last digit by the first digit of the positive n.

# 6.100A Fall 2025
# Problem Set 1: Part A
# Name: Gabriel Zendejas
# Collaborators: PyTutor
# Time Spent: 1:30:00 (roughly?)


############################################################
# Global variables
# Prior to running `test_ps1_student.py`, please comment
# these variables out!

# task_1_many_dates = "2024-08-01 2024-08-02 2024-08-03"
# task_2_date = "2024-08-01"
# task_3_date = "2024-08-02"
# task_4_date = "2024-08-03"
############################################################


############################################################
# Warm-up Tasks
############################################################


# Task 1: Finding the position of the first occurrence of a space
# Your code here

first_space = task_1_many_dates.find(" ")
if(first_space == -1):
    first_space = "None"
print(f'Position of first space: {first_space}')

# Task 2: Replacing dashes with slashes in a string
# Your code here

new_date = task_2_date.replace("-", "/")
print(f'Modified string: {new_date}')


# Task 3: Reversing the date into the opposite order
# Your code here

reversed_date = task_3_date[::-1]
if(reversed_date == ""):
    print(f'Reversed string: None')
else:
    print(f'Reversed string: {reversed_date}')

# Task 4: Date format conversion from YYYY-MM-DD to MM-DD-YYYY
# Your code here

# This find function finds the index of the nth appearence of targetcharacter in targetstring. 
# For example, find("aaaaa", "a", 2) will return index 1, because that is the 2nd occurence of "a"
def find(targetstring, targetcharacter, targetcount):
    if(targetcount == 0):
        return(0) 
    return_index = -1
    count = 0
    for index in range(len(task_4_date)):
        if targetstring[index] == targetcharacter:
            return_index = index
            count += 1
            if(count == targetcount):
                return(return_index)
    return(return_index)

YYYY = task_4_date[0:find(task_4_date, "-", 1)]
MM = task_4_date[find(task_4_date, "-", 1)+1: find(task_4_date, "-", 2)]
DD = task_4_date[find(task_4_date, "-", 2)+1:]

if(YYYY == "" or MM == "" or DD == ""):
    print(f"Converted date: None")
else:
    print(f"Converted date: {MM}-{DD}-{YYYY}")

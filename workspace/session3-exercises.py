#%%
# https://en.wikipedia.org/wiki/Collatz_conjecture
#
# Implement a function that receives an integer as a parameter
# and returns the list containing all steps until one.
#
# The rules are:
# if current integer is even, divide it by 2
# if current integer is odd, multiply it by 3 and add 1
#
# repeat the process until you reach 1
#
# Example inputs and outputs:
# collatz(1) -> [1]
# collatz(8) -> [8, 4, 2, 1]
# collatz(12) -> [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

import string


def collatz(num):
    lst = []
    if num % 2 == 0:
        lst.append(num)
        print(num)
        collatz(num)
        while num % 2 == 0 & num > 1:
            print(num)
            num /= 2
            lst.append(int(num))
    else:
        print("odd")
        lst.append(num)
        print(num)
        print(num)

    return lst

#print("collatz(1) -> " + str(collatz(1)))
#print("collatz(8) -> " + str(collatz(8)))
print("collatz(12) -> " + str(collatz(12)))

#%%

def collatz(number):
    if number <= 0:
        return "this doesn't work"
    
    steps_list = [number]

    while number != 1:
        

    # lst = []
    # if num % 2 == 0:
    #     lst.append(num)
    #     print(num)
    #     collatz(num)
    #     while num % 2 == 0 & num > 1:
    #         print(num)
    #         num /= 2
    #         lst.append(int(num))
    # else:
    #     print("odd")
    #     lst.append(num)
    #     print(num)
    #     print(num)

    # return lst

#print("collatz(1) -> " + str(collatz(1)))
#print("collatz(8) -> " + str(collatz(8)))
print("collatz(12) -> " + str(collatz(12)))



#%%
#
# Pangram
# from the Greek, παν γράμμα, which means "every letter".
#
# this function receives a string, and returns a boolean.
# The function returns true if the input string contains letters
# from a to z from the latin alphabet false otherwise.

def contains_letters(str):
    for i in str:
        if i.isalpha():
            return True
            #result.append("True")
        else:
            #result.append("False")        
            return False
        
print(contains_letters(" "))
print(contains_letters("Aida "))

#%% PANGRAM

# Pangram
# from the Greek, παν γράμμα, which means "every letter".
#
# this function receives a string, and returns a boolean.
# The function returns true if the input string contains letters
# from a to z from the latin alphabet false otherwise.

import string
def pangram(str):
    latin_alphabet = set(string.ascii_letters)
    for letter in latin_alphabet:
        if letter.lower() not in str.lower():
            return False
        else:
            return True

print(pangram("The quic brown fox jumps over the laxy dog"))
print(pangram("The the lazy dog"))
#%%

# Student Grade Management System

# Create an empty dictionary to store student information.
# Initialize an empty dictionary named 'students'.

# Define a function to calculate the average grade.
# Create a function named 'calculate_average' that takes a list of grades as input.
# In the function, calculate the average of the grades and return it.

def calculate_average(grades):
    # count = 0
    # print(grades)
    # print(type(grades))
    # for i in grades:
    #     count+=int(i)
    print(str(sum(grades)))
    mean = sum(grades)/len(grades)
    #mean = sum(list(grades))/len(grades)
    print("\n*********************\nSuccesfully computed the average: " + str(mean))
    return mean

students = {

}

# Menu-driven interface
# Create a while loop that displays a menu and continues until the user chooses to quit.

while True:
    print("\nWelcome to the Student Grade Management System!")
    print("1. Add a new student")
    print("2. Calculate average grades")
    print("3. Find the student with the highest average grade")
    print("4. Search for a student")
    print("5. Quit")
    
    # Get user's choice
    choice = input("Choose 1-5: ")

    
    
    if choice == '1':
        # Add a new student and their grades
        # Ask the user for the student's name and grades as input.
        student = input("Input student's name")
        grades = input("Input student's grades separated by comas (e.g. 5, 7, 7)").split(", ")
        grades_ = []
        for i in grades:
            grades_.append(float(i))

        #print(grades)
        students[student] = grades_
        print("\nRelation of the student and grades properly added")
        # Split the grades input into a list of integers.
        # Add the student's name as the key and their grades as the value to the 'students' dictionary.
        # Print a success message.
        pass

    elif choice == '2':
        # Calculate and display average grades
        average_grades = []
        
        for student, grades in students.items():
            media = calculate_average(grades)
            average_grades.append(media)
            print("\nStudent: " + student + "\n\tAverage grade: " + str(average_grades[-1]))
        # Iterate through the 'students' dictionary.
        # For each student, calculate the average grade using the 'calculate_average' function and print it.
        pass

    elif choice == '3':
        # Find and display the student with the highest average grade
        # Check if the 'students' dictionary is empty.
        # If not, find the student with the highest average grade using the 'calculate_average' function and 'max'.
        # Print the name of the student with the highest average grade.
        if len(students.keys()) > 0:
            max = 0
            name = ""
            for student, grades in students.items():
                mean = calculate_average(grades)
                if mean > max:
                    max = mean
                    name = student
            print("\nThe student with the highest average grade is: " + name + "\n\tGraded with: " + str(max))
        else:
            print("No students yet in the database")
        

    elif choice == '4':
        # Search for a student
        # Ask the user to enter the name of the student they want to search for.
        # Check if the entered name is in the 'students' dictionary.
        # If found, print the student's name and grades.
        # If not found, print a message indicating that the student was not found.
        name_search = input("Input the name of the student you want to search for")
        
        if name_search in students:
            print("\nSTUDENT: " + name_search + "\n\tGRADES: " + str(students.get(name_search)))
        else:
            print("\nThe student wasn't found. Please, make sure the student name is correctly written.")
        

        # name = input("who are you looing for?")
        # if name in students:
        #     print(f"{name}: {students[name]})

    elif choice == '5':
        # Quit the program
        # Print a goodbye message and exit the loop to end the program.
        print("\nGoodbye!")
        break
        exit
        
    
    else:
        # Invalid choice
        # Print a message for an invalid choice and continue the loop.
        print("\nInvalid choice. Please enter a valid option (1-5).")
# %% 

def word_frequencies(text):
    wordcount = {}

    for word in text.lower().split():
        print(word)
        stripped_word = word.strip(",").strip(".")
        print(stripped_word)
        if stripped_word in wordcount:
            wordcount[stripped_word] = wordcount[stripped_word] + 1
        else:
            wordcount[stripped_word] = 1

    return wordcount

text = """
Ministerial by-elections were criticised as an inconvenience
to the government, and were argued to hold back potential
executive talent that represented marginal constituencies 
where a by-election would be risky. Nevertheless, supporters
"""

word_frequencies(text)

# %%

str = '''Hola, soy, aida'''
print(str)
splitted = str.split(", ")
print(type(input("Hola")))
print(splitted)
# %%

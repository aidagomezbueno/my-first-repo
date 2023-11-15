#%% Equality

print("potato" == "tomato")
print(4 != 5)
print(1000 > 0)
print(1000 < 0)
print(1000 >= 1000)
print(1000 <= 1000)

print("a" > "b")

print(type(5) == int)
# %%

if 3 > 2:
    print("three is greater than two")





#%%

# Given a variable "a", create a program that
# would print "this is a string" if the variable
# contains a string

a = "1234"

if type(a) == str:
    print("This is a string!")

if type(a) == int:
    print("That's an int")

# %%

a = "False"

if type(a) == str:
    print("this is a string")
else:
    if type(a) == int:
        print("this is an int")
    else:
        if type(a) == float:
            print("this is a float")
        else:
            print("this is a boolean")

# %%

a = None
type_of_a = type(a)

if type_of_a == str:
    print("this is a str")
elif type_of_a == int:
    print("this is a int")
elif type_of_a == float:
    print("this is a float")
elif type_of_a == bool:
    print("this is a bool")
else:
    print("it wasn't any of the previous types: " + str(type(a)))


# %%

# Create a program that checks if the user can drive
# and prints "you can drive" if they can,
# and "wait" if they don't

age = int(input('please tell me your age'))
neccesary_age = 18
accompanied_by_an_adult_response = input("are you accompanied by an adult")
accompanied_by_an_adult = None
difference = neccesary_age - age

positive_responses = ["true", "True", "t", "yes", "y", "si"]

if accompanied_by_an_adult_response in positive_responses:
    accompanied_by_an_adult = True
else:
    accompanied_by_an_adult = False

if age >= neccesary_age:
    print("you can drive")
elif age >= 16 and accompanied_by_an_adult == True:
    print("You can drive")
else:
    print("Wait " + str(difference) + " years")
# %% calling functions

print()
print(123, 432, "asdf")
type("asdf")
bool(1)

# %%

def say_hello(name):
    print("Hello, " + name)

result = say_hello("Pepe")

print(result)
# %%

# AWayOfSeparatingWordsInAText
# what_we_use_in_python_is_snake_case

def add_two_numbers(first, second):
    return first + second

result = add_two_numbers(7, 5)
add_two_numbers(first=6, second=8) # named arguments / named params
add_two_numbers(second=4, first=643)

print(result)
# %%

ACCELERATION_OF_GRAVITY = 9.8

#%%

def calculate_are_triangle_rectangle(number_of_sides, base, height):
    if number_of_sides == 3:
        return base * height / 2
    elif number_of_sides == 4:
        return base * height
    
print(calculate_are_triangle_rectangle(537, 5, 55))
# %%

def weekly_commute_time():
    daily_commute = input("how long is your daily commute?")
    weekly = 5 * 2 * int(daily_commute)
    
    return weekly

time = weekly_commute_time()
print(time)
# %%

def im_in_love(weekday):
    weekday = weekday.lower()

    if weekday == "monday":
        return "blue"
    elif weekday == "tuesday" or weekday == "wednesday":
        return "grey"
    elif weekday == "thursday":
        return "I don't care about you"
    elif weekday == "friday":
        return "I'm in love!"
    
print(im_in_love("Monday"))
print(im_in_love("tuesday"))
print(im_in_love("wednesday"))
print(im_in_love("thursday"))
print(im_in_love("friday"))
print(im_in_love("saturday"))

# %% 

import json
with open('luke.json') as file:
    

# %%

import json


with open("/Users/pepegarcia/Downloads/luke.json") as luke_file:
    # json.load:: File -> Dict
    # luke_file: File
    # luke_data: Dict
    luke_data = json.load(luke_file)

    print("name = " + luke_data["name"])
    print("height = " + luke_data["height"])
    print("eye_color = " + luke_data["eye_color"])
    print("mass = " + luke_data["mass"])

# %%

import csv
import json

def format_converter(csv_path):
    json_content = []

    # 1. read the csv
    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)


        # 2. for each row in csv, create a dict
        for row in reader:
            row_dict = {
                "Symbol": row[0],
                "Name": row[1],
                "Sector": row[2]
            }

            # 3. append that dict to a list
            json_content.append(row_dict)

        # 4. dump said list to a json file
        with open("converted.json", "w") as json_file:
            json.dump(json_content, json_file)


format_converter("Downloads/data.csv")
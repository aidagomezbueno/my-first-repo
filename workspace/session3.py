
# represent integers

1

423


# Floating point numbers

3.14
0.5
0.12341234

# Strings (used for text)

"Hello everyone"
'Hello Everyone'
'I am Jose Luis but they call me "Pepe"'
"I'm Jose Luis"
"I'm Jose Luis but they call me \"Pepe\"" # escaping characters
"Hello Iñigo, 1234"

# Booleans

True
False

#%% type function

print(type(3))


# %%

print(type("there's some text here"))
print(type(1))
print(type(True))
print(type(44.4))
print(type('true'))
print(type('True'))

# %% arithmetic operators

print(3 + 4)
print(4 - 3)
print(43.4 * 4)
print(43.4 / 4)
print(2 ** 7)
print(13 / 4)
print(13 // 4)
print(15 % 4)

# %% Operators on string

print("Hello, my name is " + "Pepe")
print("Hello" * 4)
print("Na" * 16 + " Batman")

# %% Variables

size = 10
brand = "Nike"
model = "Air Force One"
weight = 0.4
price = 100.4
is_rain_proof = False
is_metal_protected = False


print("I bought a pair of " + brand + ' ' + model)
print("they weight " + str(weight) + " and costed me " + str(price) + "$")

#%% mutabilty

age = 24
print(age)

age = 25
print(age)

# don't try to read this as a
# math equation
age = age + 1
print(age)

age += 1
print(age)


# %%

age = int("24")

print(age + 10)
# %%

name = input("Please, tell me your name: ")

print("Hello, " + name)

# %%

age = int(input("how old are you? "))
age_in_ten_years = age + 10

print("in 10 years you'll be " + str(age_in_ten_years) + " years old")







# %% Total seconds in an hour

seconds_in_an_hour = 60 * 60

print("There are " + str(seconds_in_an_hour) + " seconds in an hour")

# %%

age = int(input("how old are you? "))
mom = int(input("how old is your mom? "))

print("the age difference between the two of you is " + str(mom - age) + " years")
# %%
a = 3
b = "3"

#print(str(3 + 3))

print(a + int(b))

#%%


print('there are ' + str(4) + ' dogs barking')

# %%

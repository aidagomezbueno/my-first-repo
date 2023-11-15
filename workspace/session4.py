#%% FILES - opening files

file = open("names.txt")
# print(type(file))

for line in file:
    print(line)

file.close()

# %%

with open("names.txt") as file:
    for line in file:
        print(line)
    # file.close() python automatically closes the file whenever the with loop ends

#  for that reason this would not work:
# for line in file:
#     print(line)
# %%

with open("hello.txt", "w") as file:
    file.write("hello everybody!")


# %%
# Exercise:
# without using csv library, open users.csv and print each cell individually

with open("users.csv") as file:
    for line in file:
        for cell in line.strip().split(","):
            print(cell)


# %%
users = [
    ["Pepe", 33],
    ["JC", 23],
    ["Other People", 64]
]

# %%
import csv
# import pandas

# with open("users.csv") as file:
#     reader = csv.reader(file)
#     for line in reader:
#         print(line[1])
#         # for cell in line:
#         #     print(cell)

users = [
    ["Pepe", 33],
    ["JC", 23],
    ["Other People", 64]
]

with open("class.csv", "a") as file:
    writer = csv.writer(file)
    for user in users:
        writer.writerow(user)


# %%

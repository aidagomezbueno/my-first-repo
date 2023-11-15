# %% Simple Stock Analysis Tool

# Objective
# Create a tool to read, analyze, and interact with historical 
# stock data. The data will be stored in a CSV file with the following 
# headers: Date, Open, High, Low, Close, Volume, Name. 

# You can use all_stocks_5yr.csv from blackboard.

import csv 
from json import dump



# Instructions

# 1. Functions:
# load_data(): Reads the data from the csv file and returns a list of 
# dictionaries. Each dictionary represents a trading day.

def load_data(csv_path):
    trading_days = []
    # 1. read the csv
    with open(csv_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            trading_days.append(row)
        # print(reader)
        # next(reader)
        # 2. for each row in csv, create a dict
        # for row in reader:
        #     row_dict = {
        #         "Date": row[0],
        #         "Open": row[1],
        #         "High": row[2],
        #         "Low": row[3],
        #         "Close": row[4],
        #         "Volume": row[5],
        #         "Name": row[6]
        #     } 
            # trading_days.append(row_dict)
    return trading_days
DATA = load_data("all_stocks_5yr.csv")
# highest_closing_price(data): Returns the date and value of the highest 
# closing price.

def highest_closing_price(data):
    value = 0.0
    date = ""
    for dic in data:
        if float(dic["close"]) > value:
            value = float(dic["close"])
            date = dic["date"]
    print("HIGHEST CLOSING PRICE:\n\t" + date + "\n\t" + str(value))

# lowest_closing_price(data): Returns the date and value of the lowest 
# closing price.

def lowest_closing_price(data):
    value = 999999999.99
    date = ""
    for dic in data:
        if float(dic["close"]) < value:
            value = float(dic["close"])
            date = dic["date"]
    print("LOWEST CLOSING PRICE:\n\t" + date + "\n\t" + str(value))

# highest_closing_price(load_data("all_stocks_5yr.csv"))
# lowest_closing_price(load_data("all_stocks_5yr.csv"))


# average_volume(data): Calculates the average trading volume over all days.

def average_volume(data):
    total_entries = len(data)
    # print(mean)
    vol = 0.0
    for dic in data:
        vol += float(dic["volume"])
    # print(str(vol))
    mean = vol/total_entries
    return mean
       
average_volume(DATA)

# price_on_date(data, date): Returns the opening, high, low, and closing 
# prices for a specific date.

# Extend the price_on_date function to also display the trading volume 
# for the specific date.

def price_on_date(data, date):
    prices = []
    for dic in data:
        if dic["date"] == date:
            dic_date = {
                "open": dic["open"],
                "high": dic["high"],
                "low": dic["low"],
                "close": dic["close"], 
                "volume": dic["volume"]
            }
            prices.append(dic_date)
    print("PRICES FOR " + date + ":\n\tOPEN\t\tHIGH\t\tLOW\t\tCLOSE\t\tVOLUME")
    for i in prices:
        print("\t" + i["open"] + "\t\t" + i["high"] + "\t\t" + i["low"] + "\t\t" + i["close"]+ "\t\t" + i["volume"])

# Create a function to calculate and display the average closing price 
# over a given date range.

def avg_closing_price(data, date):
    # prices = []
    closing_prices = 0.0
    cont = 0
    for dic in data:
        if dic["date"] == date:
            cont+=1
            closing_prices+=float(dic["close"])
    mean = closing_prices/cont
    print("The average closing price for the date given is: " + str(mean))


            
            # dic_date = {
            #     "open": dic["open"],
            #     "high": dic["high"],
            #     "low": dic["low"],
            #     "close": dic["close"], 
            #     "volume": dic["volume"]
            # }
    #         prices.append(dic_date)
    # print("PRICES FOR " + date + ":\n\tOPEN\t\tHIGH\t\tLOW\t\tCLOSE\t\tVOLUME")
    # for i in prices:
    #     print("\t" + i["open"] + "\t\t" + i["high"] + "\t\t" + i["low"] + "\t\t" + i["close"]+ "\t\t" + i["volume"])


# price_on_date(load_data("all_stocks_5yr.csv"), "2017-08-08")

# save_to_json(data): saves the data to a json file

def save_to_json(data):
    with open("json_file", "w") as json_file:
            dump(data, json_file)

save_to_json(load_data("all_stocks_5yr.csv"))

def top5_trading_volume(data):
    # total_entries = len(data)
    # print(mean)
    dics = []
    vol = 0.0
    date = data[1]["date"]
    max = 0
    date = ""
    for dic in data:
        # print(dic)
        # date = dic["date"]
        if date == dic["date"]:
            vol+=float(dic["volume"])
        else:
            new_dic = {
                "date": date,
                "total_volume": vol
            }
            dics.append(new_dic)
            date = dic["date"]
            vol = float(dic["volume"])
    for i in dics:
        if i["total_volume"] > max:
            max = i["total_volume"]
            date = i["date"]
    for i in dics:
        if i["total_volume"] == max:
            
    # print(type(dics))
    # print(str(dics.pop(date)))





        # vol += float(dic["volume"])
    # print(str(vol))
    # mean = vol/total_entries
    # return mean
top5_trading_volume(DATA)



# 2. User Interface:
# When the program runs, prompt the user with a menu:

# Stock Analysis Tool:
# 1. View Highest Closing Price
# 2. View Lowest Closing Price
# 3. Calculate Average Trading Volume
# 4. Get Stock Details for a Specific Date
# 5. Exit

# Depending on the userâ€™s selection, the program should call the 
# appropriate function and display the result.
# The program should continue displaying the menu and receiving input 
# until the user selects the â€˜Exitâ€™ option.

# while True:
#     selected_func = int(input("Stock Analysis Tool:\n1. View Highest Closing Price\n2. View Lowest Closing Price\n3. Calculate Average Trading Volume\n4. Get Stock Details for a Specific Date\n5. Exit\n6. Print top 5 days with the highest trading volume."))
#     data = load_data("all_stocks_5yr.csv")
#     if selected_func == 1:
#         highest_closing_price(data)
#     elif selected_func == 2:
#         lowest_closing_price(data)
#     elif selected_func == 3:
#         print("The Average Trading Volume is: " + str(average_volume(load_data("all_stocks_5yr.csv"))))
#     elif selected_func == 4:
#         date = input("Introduce an specific date to show the stock details")
#         price_on_date(data, date)
#         avg_closing_price(data, date)
#     elif selected_func == 5:
#         break
#     elif selected_func == 6:
#         top5_trading_volume(data)
#     else:
#         print("Invalid option. Please, introduce a number between 1-5.")
#         selected_func = int(input("Stock Analysis Tool:\n1. View Highest Closing Price\n2. View Lowest Closing Price\n3. Calculate Average Trading Volume\n4. Get Stock Details for a Specific Date\n5. Exit"))

# Bonus Tasks


# Implement a feature to display the top 5 days with the highest trading 
# volume.
# Add error-handling, e.g., for dates that are not in the dataset.
# %%

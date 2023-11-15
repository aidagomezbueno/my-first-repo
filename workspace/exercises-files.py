#%%

import csv

def find_cheapest_buy_day(ticker):
    # ticker_info = []
    lowest = 1000000.0
    date = ""
    with open("all_stocks_5yr.csv") as file:
        reader = csv.reader(file)
        for line in reader:
            # line_splitted = line.strip().split(",")
            if line[6] == ticker:
                if float(line[3]) < lowest:
                    lowest = float(line[3])
                    date = line[0]
    #             ticker_info.append(line)
    # for row in ticker_info:
    #     # print(float(row[3]))
    #     if float(row[3]) < lowest:
    #         # print(float(row[3]))
    #         lowest = float(row[3])
    #         date = row[0]
    print("The cheapest day to buy the stock is: " + str(date))
            
find_cheapest_buy_day("AAPL")

# %% print the dataset
with open("all_stocks_5yr.csv") as file:
    for line in file:
        line_splitted = line.strip().split(",")
        print(line)

        # if line_splitted[6] == "MSFT":
        #     print(line_splitted[6])
        # print(line_splitted[6])
# %%
# Create a function that receives:
# A ticker (example ‘GOOG’)
# A buy date (example 2023-01-20)
# A sell date (example 2023-12-25)
# and an amount in dollars (example 1000)
# And returns the selling amount.

import csv

def calculate_total_price(ticker, buy_date, sell_date, dollars_amount):
    
    buy_price = 0
    sell_price = 0

    if buy_date > sell_date:
        print("buy date needs to happen before sell")
        return

    with open("all_stocks_5yr.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if ticker == row[-1]:
                if row[0] == buy_date:
                    buy_price = float(row[1])
                elif row[0] == sell_date:
                    sell_price = float(row[1])

    return dollars_amount / buy_price * sell_price
    

print(calculate_total_price("AAPL", "2013-06-03", "2014-06-03", 1000))

# %% Solved in class:
import csv

def find_cheapest_by_day(ticker):
    lowest_price = float("inf")
    cheapest_day = None

    with open("all_stocks_5yr.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if ticker == row[-1]:
                float_price = float(row[1])
                if float_price < lowest_price:
                    lowest_price = float_price
                    cheapest_day = row[0]

    return cheapest_day

print(find_cheapest_by_day("AAPL"))

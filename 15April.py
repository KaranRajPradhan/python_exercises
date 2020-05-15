import json
import os

filename = "database.json"
def startup(filename):
    stock = {"orange": {"quantity": 25, "price": 100},
            "apple": {"quantity": 20, "price": 200},
            "banana": {"quantity": 30, "price": 40},
            "pineapple": {"quantity": 15, "price": 60},
            "kiwi": {"quantity": 5, "price": 450}
            }

    if os.path.exists(filename):
        file_data = open(filename).read()
        if len(file_data) > 0:
            stock_data = json.loads(file_data)
            return stock_data
        else:
            return stock
    else:
        return stock

stock = startup(filename)


while True:
    action = input("What action do you want? Buy/Sell/Exit: ")
    if action == "sell" or action == "buy":
        fruit_name = input("Enter the fruit name: ")
        how_much = float(input("Enter the quantity: "))

        current_stock = stock.get(fruit_name).get("quantity")
        if action == "sell":
            if not current_stock:
                print("Sorry, fruit not available")
            elif current_stock < how_much:
                print(f"Sorry, current stock is {current_stock}")
            else:
                new_stock = current_stock - how_much
                print("BILL:")
                print("Amount Payable: ", how_much * stock[fruit_name]["price"])
                stock[fruit_name]["quantity"] = new_stock
        else:
            if current_stock == None:
                stock[fruit_name]["quantity"] = how_much
                stock[fruit_name]["price"] = input("Price for the item: ")
            else:
                stock[fruit_name]["quantity"] = current_stock + how_much
        print(stock)
    
    elif action == "exit":
        json_stock = json.dumps(stock)
        file = open(filename, "w")
        file.write(json_stock)
        file.close()
        exit()
    else:
        print("Not a valid action!!")
    
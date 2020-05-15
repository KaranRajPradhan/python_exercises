import json
import os

filename = "library_data.json"
prompt = "->"
def startup(filename):
        stock = {"Harry Potter": {"Full name": "Harry Potter and the Chamber of Secrets",
                                "Author": "J.K. Rowling",
                                "Price": 399,
                                "Pages": 735,
                                "Borrowed": False,
                                "Borrowed by": " "},
                "Game of Thrones": {"Full name": "A Song of Ice and Fire",
                                "Author": "George R. R. Martin",
                                "Price": 500,
                                "Pages": 452,
                                "Borrowed": False,
                                "Borrowed by": " "},
                "The Little Prince": {"Full name": "The Little Prince",
                                "Author": "Antoine de Saint-Exupéry",
                                "Price": 380,
                                "Pages": 200,
                                "Borrowed": False,
                                "Borrowed by": " "},
                "The Alchemist": {"Full name": "The Alchemist",
                                "Author": "Paulo Coelho",
                                "Price": 299,
                                "Pages": 350,
                                "Borrowed": False,
                                "Borrowed by": " "}
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
        print("Please enter customer's name")
        username = input(prompt)
        print(f"Hi {username}!!! Do you want to borrow, return or check? Type 'exit' to exit.")
        action = input(prompt)
        if action == "borrow":
                print("Which book do you want to borrow today?")
                bookname = input(prompt)
                if bookname not in stock.keys():
                        print(f"Sorry {username}, we don't have the book '{bookname}' in this library.")
                elif stock[bookname]["Borrowed"] == True:
                        print(f"Sorry {username}, the book '{bookname}' is already borrowed by {stock[bookname]['Borrowed by']}. Please check back later.")
                else:
                        stock[bookname]["Borrowed"] = True
                        stock[bookname]["Borrowed by"] = username
                        print("Here's your book! Have fun reading! Please return within 15 days to avoid any fines")
        elif action == "return":
                print("Which book do you want to return?")
                bookname = input(prompt)
                if stock[bookname]["Borrowed"] == False:
                        print("Sorry, the book is not borrowed. Please try again")
                else:
                        stock[bookname]["Borrowed"] = False
                        stock[bookname]["Borrowed by"] = " "
                        print(f"Hope you enjoyed reading {bookname}!!!")
        elif action == "check":
                print("Here's a list of all the amazing books you can choose to borrow today!!!")
                count = 0
                for i in stock:
                        if stock[i]["Borrowed"] == False:
                                count += 1
                                print(f"{count}. {i}")
                # print(stock)
        elif action == "exit":
                json_stock = json.dumps(stock)
                file = open(filename, "w")
                file.write(json_stock)
                file.close()
                exit()
        else:
                print("Sorry! Invalid Input. Please try again.")
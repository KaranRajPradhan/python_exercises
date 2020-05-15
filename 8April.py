# hasan = {
#     "name":"Hasan",
#     "age":25,
#     "city":"Bangalore",
#     "language": ["Hindi","English"],
#     "insane":True
#     "coffee":"Milk and Sugar"
# }

# alfrin = {
#     "name":"Alfrin",
#     "age":28,
#     "city":"Bangalore",
#     "language": ["Hindi", "English", "Kannada"],
#     "insane":False
#     "coffee": "Black and Sugar"
# }

# humans = [hasan, alfrin]

answers = {}
questions = {"name":"What is your name: ",
            "age":"What is your age: ",
            "city":"City: ",
            "language": "Languages you speak: ",
            "insane": "Are you insane: ",
            "coffee": "Type of coffee: "
            }
users = []
user1 = []
user2 = []
user3 = []

for i in range(3):
    for key in questions:
        question = questions[key]
        answer = input(question)
        answers[key] = answer
    users.append(answers)
    if i == 0:
        user1 = answers
    elif i == 1:
        user2 = answers
    else:
        user3 = answers
if user1["city"] == user2["city"]:
    # print(f"{user1["name"]} and {user2["name"]} live in the same city")
    print("User1 and User2 live in the same city")

elif user2["city"] == user3["city"]:
    # print(f"{user2["name"]} and {user3["name"]} live in the same city")
    print("User2 and User3 live in the same city")    
elif user1["city"] == user3["city"]:
    # print(f"{user1["name"]} and {user3["name"]} live in the same city")
    print("User2 and User3 live in the same city")
else:
    print("No Matching Cities")

# print(users)

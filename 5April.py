# myself = {"name":"Karan", 
#             "age":22, 
#             "city":"Bangalore",
#             "language":["Hindi","English"],
#             "insane":True
#         }
# # print(myself["name"])
# # print(myself["language"])

# myself["coffee"] = "Milk with Sugar and Ice"
# # print(myself["coffee"])
# del(myself["coffee"])
# # print(myself)
# dress = {"top":"shirt", "bottom":"pants"}
# myself.update(dress)
# print(myself)
# print(myself.values())
# print(myself.keys())
# print(myself.items())
# print(list(myself.items())[0])


# answers = {}
# questions = {"name":"What is your name:",
#             "age":"What is your age:",
#             "city":"Where do you live:"}
# for key in questions:
#     question = questions[key]
#     answer = input(question)
#     answers[key] = answer
# print(answers)
# for key in answers:
#     if key == "age":
#         answers[key] = int(answers[key])

# print(answers)

# answers = {}
# questions = {"name":"What is your name: ",
#             "age":"What is your age: ",
#             "books":"Books you like: ",
#             "hobbies":"What are your hobbies: "}
# for key in questions:
#     question = questions[key]
#     answer = input(question)
#     if key == "books" or key == "hobbies":
#         answers[key] = answer.split(",")
#     else:
#         answers[key] = answer
# print(answers)

answers = {}
total = 0
questions = {"english":"Marks obtained in English: ",
            "maths":"Marks obtained in Maths: ",
            "science":"Marks obtained in Science: ",
            "history":"Marks obtained in History: ",
            "geography":"Marks obtained in Geography: "}
for key in questions:
    question = questions[key]
    answer = int(input(question))
    answers[key] = answer
    total += answer
percentage = (total * 100) / 500
print(answers)
# for  in answers
#     print(list(answers.items())[key])
print("Total Marks: ", total)
print("Percentage: ", percentage)
if percentage > 90:
    print("Grade: A")
elif percentage >80:
    print ("Grade: B")
else:
    print("Grade: C")
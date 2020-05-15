prompt = "->"
donors = []
recipients = []
donor_questions = {"name":"What is your name: ",
                   "age":"What is your age: ",
                   "BG":"Blood Group: ",
                   "city":"City: ",
                   "phone": "Phone No.: "
                  }
recipient_questions = {"name":"What is your name: ",
                       "age":"What is your age: ",
                       "BG":"Blood Group: ",
                       "city":"City: ",
                       "phone": "Phone No.: "}
while True:
    match_counter = 0
    answers = {}
    print("Welcome to Jaaga Blood Bank! Are you a donor or a recipient?")
    action = input(prompt)
    if action == "donor":
        for key in donor_questions:
            question = donor_questions[key]
            answer = input(question)
            answers[key] = answer
        donors.append(answers)
    elif action == "recipient":
        recipient_BG = input("Blood Group: ")
        recipient_city = input("City: ")
        for i in donors:
            if i['BG'] == recipient_BG or i['BG'] == "O+" and i['city'] == recipient_city:
                print(f"Matched with {i['name']}. Contact: {i['phone']}")
                match_counter += 1
        if match_counter == 0:
            print("Sorry! No Matches Found")
    
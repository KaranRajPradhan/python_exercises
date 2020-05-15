
donors = []

def donate():
    user = {}
    user["name"] = input("What is your name: ")
    user["city"] = input("What is your city: ")
    user["bg"] = input("What is your blood group: ")
    user["phone"] = input("What is your phone number: ")
    donors.append(user)

def receive():
    city = input("What is your city: ")
    blood_group = input("What is your blood group: ")
    for donor in donors:
        valid_blood_group = donor["bg"] == blood_group
        valid_city = donor["city"] == city
        if valid_blood_group and valid_city:
            print(donor["name"], donor["phone"])

while True:
    user_type = input("Are you a donor(0) or a recipient(1)?")

    if user_type == "0":
        donate()
    elif user_type == "1":
        receive()
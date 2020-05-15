members = []

def add_member():
    match_counter = 0
    new_member = {}
    new_member["name"] = input("What is your name: ")
    new_member["dog_name"] = input("What is your dog's name: ")
    new_member["dog_breed"] = input("What is your dog's breed: ")
    new_member["city"] = input("What is your city: ")
    new_member["gender"] = input("What is your dog's gender")
    match_mate = input("Enter 1 to find a mate, 0 to pass.")
    for member in members:
        valid_dog_breed = member["dog_breed"] == new_member["dog_breed"]
        valid_city = member["city"] == new_member["city"]
        if valid_dog_breed and valid_city:
            print(member["name"], member["dog_name"])
            match_counter += 1
    if match_counter == 0:
        print("Sorry No Matches")
    members.append(new_member)


while True:
    add_member()
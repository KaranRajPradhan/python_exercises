import April26_filewriter

filename = input("Enter the file name: ")
try:
    txt = open(filename)

    print(txt.read())
except FileNotFoundError:
    action = input("File does not exist. Do you want to create this file? (y or n): ")
    if action == "y":
        April26_filewriter.write_file(filename)
    else:
        exit()
from sys import argv
script, filename = argv

print("We are going to erase {filename}")
print("If you dont want that, hit Ctrl+C")
print("If you do want that, hit Return")

input("?")

print("Opening the target file ...")
target = open(filename, 'w')

print("Truncating the file, GOODBYE!!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Im going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()

target = open(filename)
print(target.read())

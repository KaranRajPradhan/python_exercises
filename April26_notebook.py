prompt = ">"

filename = input("Enter the filename to create: ")

txt = open(filename, 'w')

try:
    while True:
        print("Enter line: ")
        line = input(prompt)
        if line == "done":
            break
        else:
            txt.write(line)
            txt.write("\n")
    # txt.close()

except KeyboardInterrupt:
    # txt.close()
    # exit()
    print("Saving")

finally:
    txt.close()


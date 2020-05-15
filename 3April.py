# start1 = int(input("Enter start 1\n"))
# jump1 = int(input("Enter jump 1\n"))
# start2 = int(input("Enter start 2\n"))
# jump2 = int(input("Enter jump 2\n"))


# if start1 > start2 and jump1 > jump2:
#     print("NO")
# elif start1 < start2 and jump1 < jump2:
#     print("NO")
# elif start1 == start2 and jump1 != jump2:
#     print("NO")
# else:
#     if (start2 - start1) % (jump1 - jump2) == 0:
#         print("YES")
#     else:
#         print("NO")

# rows = int(input("Enter rows\n"))
# cols = int(input("Enter columns\n"))
# print(" ", end = '')
# print("-"*rows)
# for i in range(cols):
#     if i == 0 or i == (cols-1):
#         print("|", end = '')
#         print("-"*(rows), end = '')
#         print("|")
#     else:
#         print("|", end = '')
#         print(" "*(rows), end = '')
#         print("|")
# print(" ", end = '')
# print("-"*rows)


input_string = input("Enter the sentence: ")
string_list = input_string.split()
print(string_list)
for i in range(len(string_list)):
    print(string_list.count(string_list[i]))
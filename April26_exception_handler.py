try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    numbers = [0,1,2,3,4,5]

# try:
    num2 = numbers[num2]
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Can't divide a number by zero")
# except IndexError:
#     print("Wrong Index Number")
except KeyboardInterrupt:
    print("BYEBYE!!")
    exit()
except Exception as e:  #handle unhandled exceptions
    print(e)
    print("Sorry BYEBYE")
finally:    #always executes regardless of error occuring or not
    print("Hope you come back")
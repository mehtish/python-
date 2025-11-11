
def calculatr ():
    print ("welcome to the calculator")
    number1=int(input("please enter your first number : "))
    operation=input("please enter your operation: ")
    number2= int(input("please enter your second number : "))
    if operation == "+":
        print(number1+number2)
    elif operation == "-":
        print(number1-number2)
    elif operation == "/":
        if number2!=0:
            print(number1 / number2)
        else: 
            print("Error : cannot divide by zero!")
    elif operation == "*": 
        print(number1 * number2)
    else: 
        print("invalid operation.")
calculatr()







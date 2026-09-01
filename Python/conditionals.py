day_of_week=input("Enter the day of the week: ").lower()  #taking input from user and converting it to lowercase
print("You entered:", day_of_week)  #printing the entered day

if day_of_week == "saturday" or day_of_week == "sunday":  #this is condition
    print("i will learn DevOps")  #true
else:
    print("I will practice DevOps") #false

sum1 = int(input("Enter first number: "))    #taking input from user
sum2 = int(input("Enter second number: "))   #str->int conversion is called type casting 

choice = input("Input your operations: (Options + , - , * , / , %) ")

if choice == "+":
    sum = sum1 + sum2
    print("Total Sum is: ", sum)
elif choice == "-":
    diff = sum1 - sum2
    print("subtraction is: ", diff)
elif choice == "*":
    mul = sum1 * sum2
    print("multiply  is: ", mul)
elif choice == "/":
    div = sum1 / sum2
    print("division:", div)
elif choice == "%":
    rem = sum1 % sum2
    print("remainder is: ", rem)
else:
    print("Invalid Choice")
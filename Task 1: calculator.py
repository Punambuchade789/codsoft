# Design a simple calculator for arithmetic operation
# function for addition
def add(num1, num2):
    return num1 + num2

# function for substraction
def subtract(num1, num2):
    return num1 - num2

# function for multiplication
def multiply(num1, num2):
    return num1 * num2

# fuction for division
def divide(num1, num2):
    return num1 / num2


print("Select operation.")
print("1.Add")
print("2.Divide")
print("3.Multiply")
print("4.Subtract")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        
        further_calculation = input("Let's do further calculation? (yes/no): ")
        if further_calculation == "no":
          break
    else:
        print("Invalid Input")









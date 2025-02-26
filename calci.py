def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    if b != 0:
        return a / b
    
    else:
        return ("Error: Division by zero is not allowed.")

def calculator():
    
    while True:
        
        print("Select operation: ")
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            
            if choice == '1':
                
                print("Result:", add(num1, num2))
           
            elif choice == '2':
                
                print("Result:", subtract(num1, num2))
           
            elif choice == '3':
                
                print("Result:", multiply(num1, num2))
           
            elif choice == '4':
              
                print("Result:", divide(num1, num2))
       
        else:
            print("Invalid Input!")
        if not ask_again():
            break

def ask_again():
    choice = input("Want to perform another calculations? (yes/no): ")
    return choice == "yes"

calculator()
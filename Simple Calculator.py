def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
    
def mul(a, b):
    answer = a * b 
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b 
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

print("A. Addition")
print("B. Substraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")


while True:
    choice = input("Input your choice: ")
    if choice.upper() == "A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a,b)
    elif choice.upper() == "B":
        print("Substraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b)
    elif choice.upper() == "C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a, b)
    elif choice.upper() == "D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a, b)
    elif choice.upper() == "E":
        print("Program Ended")
        quit() 
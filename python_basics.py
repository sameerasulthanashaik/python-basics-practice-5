# 1. Print Statement
print("Hello World")
print("Welcome to Python")

print("------------------")

# 2. Variables and Data Types
a = 10
b = 20.5
name = "Python"
status = True

print(a)
print(b)
print(name)
print(status)

print("------------------")

# 3. User Input
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name:", name)
print("Age:", age)

print("------------------")

# 4. Type Conversion
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", x + y)

print("------------------")

# 5. Operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

print("------------------")

# 6. If Else
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
else:
    print("Negative number")

print("------------------")

# 7. For Loop
for i in range(1, 6):
    print(i)

print("------------------")

# 8. While Loop
i = 1
while i <= 5:
    print(i)
    i += 1

print("------------------")

# 9. List
numbers = [10, 20, 30, 40]
print(numbers)
numbers.append(50)
print(numbers)

print("------------------")

# 10. Tuple
t = (1, 2, 3, 4)
print(t)

print("------------------")

# 11. Set
s = {1, 2, 3, 4, 4}
print(s)

print("------------------")

# 12. Dictionary
student = {
    "name": "Sam",
    "age": 20,
    "course": "Python"
}
print(student)
print(student["name"])

print("------------------")

# 13. String Operations
text = "Python Programming"
print(text.upper())
print(text.lower())
print(len(text))

print("------------------")

# 14. Function
def add(a, b):
    return a + b

print(add(5, 3))

print("------------------")

# 15. Even or Odd Program
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#16 .ATM
balance = 10000
pin = 24062002

entered_pin = int(input("Enter your ATM PIN: "))

if entered_pin == pin:
    print("Login Successful")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your Balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == 3:
        deposit = int(input("Enter deposit amount: "))
        balance = balance + deposit
        print("Amount Deposited Successfully")
        print("Updated Balance:", balance)

    elif choice == 4:
        print("Thank you for using ATM")

    else:
        print("Invalid choice")

else:
    print("Wrong PIN")

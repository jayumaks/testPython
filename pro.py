# Write a Program to determine the Largest of two numbers gotten from a User.

first = int(input("Enter your first number: \n"))
second = int(input("Enter the second number: \n"))

if first > second:
    print(f"Your first number {first} os larger than your second number...")
elif first  < second:
    print(f"Your second number {second} is larger than your first number...")
else:
    print("Both numbers you inputed are thesame")
# Write a program that accepts a maximum of 2 integers from a user and determines if they are even or odd numbers.
# Hint: No Odd number will give u a remainder of 0 when divided by an even number.

print("Enter Two Numbers: \n")

A = int(input("Enter First Number: \n"))
B = int(input("Enter Second Number: \n"))

if (A%2) == 0 and (B%2) == 0:
    print(f"First Number {A} and second number{B} are EVEN NUMBERS...")
elif (A%2) != 0 and (B%2) != 0:
    print(f"First Number {A} and second Number {B} are ODD NUMBERS...")
elif (A%2) == 0 and (B%2) != 0:
    print(f"First Number {A} is an EVEN NUMBER while second number {B} is an ODD NUMBER")
elif (A%2) != 0 and (B%2) == 0:
    print(f"First Number {A} is an ODD NUMBER while second number {B} is an EVEN NUMBER")
else:
    print("Unrectified numbers")

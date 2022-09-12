# Write a Program that Carries out the following instructions. If the number is divisible by 3, it should return “Fizz”. 
# If it is divisible by 5, it should return “Buzz”.
#  If it is divisible by both 3 and 5, it should return “FizzBuzz”. Otherwise, it should return the same number.

number = int(input("Enter a Number: "))

if (number%3) == 0 and (number%5) == 0:
    print("FizzBuzz")
elif (number%5) == 0:
    print("Buzz")
elif (number%3) == 0:
    print("Fizz")
else:
    print(f"{number}")
"""Task 1"""
# def celsius_to_fahrenheit(c):
#     return (c * 1.8) + 32
#
# def fahrenheit_to_celsius(f):
#     return (f - 32) / 1.8
#
# print("Choose conversion type:")
#
# choice = input("Enter Celsius or Fahrenheit: ")
# if choice == "Celsius":
#     celsius = float(input("Enter temperature: "))
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     print(f"{celsius}°C = {fahrenheit:.2f}°F")
# elif choice == "Fahrenheit":
#     fahrenheit = float(input("Enter temperature: "))
#     celsius = fahrenheit_to_celsius(fahrenheit)
#     print(f"{fahrenheit}°F = {celsius:.2f}°C")
# else:
#     print("Invalid choice")
"""OUTPUT"""
# Choose conversion type:
# Enter Celsius or Fahrenheit: Celsius
# Enter temperature: 101
# 101.0°C = 213.80°F

"""Task 2"""
import random

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return None
    return a / b

def exponent(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def main():
    score = 0
    total = 0

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponent")
        print("6. Remainder")
        print("7. Exit")

        choice = input("Your choice: ")

        if choice == "7":
            print("\nThanks for playing!")
            print(f"Final score: {score}/{total}")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Wrong choice. Try again.")
            continue

        a = random.randint(0, 9)
        b = random.randint(0, 9)

        if choice == "1":
            correct = addition(a, b)
            sign = "+"
        elif choice == "2":
            correct = subtraction(a, b)
            sign = "-"
        elif choice == "3":
            correct = multiplication(a, b)
            sign = "*"
        elif choice == "4":
            correct = division(a, b)
            sign = "/"
        elif choice == "5":
            correct = exponent(a, b)
            sign = "^"
        else:
            correct = remainder(a, b)
            sign = "%"

        if correct is None:
            print("Cannot divide by zero.")
            continue

        try:
            user = float(input(f"\nWhat is {a} {sign} {b}? "))
        except:
            print("Please enter a number.")
            continue

        total += 1

        if abs(user - correct) < 0.001:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer is {correct}")

        again = input("Continue? (y/n): ").lower()
        if again != "y":
            print(f"\nFinal Score: {score}/{total}")
            break

main()

"""Task 3"""
"""Task 4"""
"""Task 5"""
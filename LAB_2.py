# # """"""Task 1""""""
# password = input("Enter password: ")
# if len(password) < 8:
#     print("Weak")
# elif 8 < len(password) < 11:
#     print("Moderate")
# else:
#     print("Strong")
#
# # """"""Task 2""""""
#
# import random
# while True:
#     number_1 = random.randint(1, 10)
#     number_2 = random.randint(1, 10)
#     answer = number_1 * number_2
#     print(f"What is: {number_1} * {number_2} ?")
#     user_answer = int(input("Enter your answer: "))
#     if user_answer == answer:
#         print("Correct")
#     else:
#         print("Incorrect")
#
# # """"""Task 3""""""
#
# answer = input("Enter a number: ")
# if answer.isnumeric():
#     print("integer")
# elif answer.isalpha():
#     print("str")
# else:
#     print("float")
#
# # """"""Task 4""""""
# weight_p = float(input("Enter weight in pounds: "))
# height_inch = float(input("Enter height in inches: "))
# weight_kg = weight_p * 0.453592
# height_m = height_inch * 0.0254
# BMI = weight_kg / (height_m ** 2)
# if BMI < 18.5:
#     print("Underweight")
# elif 18.5 <= BMI < 25:
#     print("Normal")
# elif 25 <= BMI < 30:
#     print("Overweight")
# else:
#     print("Obese")
#
#
# # """""Task 5""""""
#
# marks = [45, 67, 89, 34, 50, 76, 92, 48, 60, 73]
# total = 0
# for mark in marks:
#     total += mark
# average = total / len(marks)
# highest = max(marks)
# lowest = min(marks)
# passed = 0
# failed = 0
# for mark in marks:
#     if mark >= 50:
#         passed += 1
#     else:
#         failed += 1
# print(f"Average mark: {average}")
# print(f"Highest mark: {highest}")
# print(f"Lowest mark: {lowest}")
# print(f"passed: {passed}")
# print(f"failed: {failed}")
#
# # """""Task 6""""""
#
# for i in range(-1,-11, -1):
#     print(i)

# quote = "Knowledge is the raw material of production and VALUE in this age."
# lower_text = quote.lower()
# capitalised = quote.capitalize()
# upper_text = quote.upper()
# print(lower_text)
# print(capitalised)
# print(upper_text)
#


# # """"7"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# # """"8"""
# sum = 0
# user_num = int(input("Enter a number: "))
# for num in range(1, user_num):
#     sum = sum + user_num
# print(f"Total is: {sum}")
#
# # """"9""""
# sum = 2
# for i in range(1, 11):
#     print(f"{i} * {sum} = {i * sum} ")
#
# # """"10""""

# for i in range(10):
#     for n in range(10):
#         print(f"{i * n:2}", end="")
#     print()
#
# # """11"""
# import math
# print("Number    Square Root")
# for num in range(0, 20, 2):
#     print(num,"       ",round(math.sqrt(num), 2))

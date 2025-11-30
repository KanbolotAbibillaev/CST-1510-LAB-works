# """"""Week5""""""


# """"""Activity 1"""""""
file = open('my_profile.txt', 'w')
file.write("Name: Kanbolot Abibillaev\n")
file.write('Age: 20\n')
file.write('Favorite color: Red')
file.close()

with open("my_profile.txt", "r") as file:
    lines = file.readlines()

print("Your Name is:", lines[0].strip().split(": ")[1])
print("Your Age is:", lines[1].strip().split(": ")[1])
print("Your Favorite Color is:", lines[2].strip().split(": ")[1])

# """"""Activity 2"""""""

with open("shopping.txt", "w") as file:
    file.write("Eggs\n Bread\n Meat\n Souse\n Potato")

with open("shopping.txt") as file:
    items = file.readlines()

for i in items:
    print(f"U need to buy: {i.strip()}")

print(f"Total num of items: ", len(items))

# """"""Activity 3"""""""

with open("tems.txt", "w") as file:
    for day in range(1, 6):
        temp = int(input(f"Write the temperature for day {day}: "))
        file.write(f"Day: {day}: {temp} C\n")

with open("tems.txt") as file:
    temps_list = [float(line.split(": ")[-1].replace(" C", "").strip()) for line in file]

average = sum(temps_list) / len(temps_list)

print("Average Temperature:", average, "C")

# """"""Activity 4"""""""

movies = {
    "Hulk": 2028,
    "Marvel": 2029,
    "Kingsman": 2031
}
earliest_movie = min(movies, key=movies.get)
print(f"The earliest movie is: {earliest_movie}, {movies[earliest_movie]}")

# """"""Activity 5"""""""

alex_hobbies = {"reading", "gaming", "cooking", "hiking"}
sam_hobbies = {"gaming", "hiking", "photography", "music"}
both_hobbies = alex_hobbies & sam_hobbies
only_alex_hobbies = alex_hobbies - sam_hobbies
all_hobbies = alex_hobbies, sam_hobbies
print("Hobbies they enjoy:", all_hobbies)
print("Hobbies that Alex enjoy:", only_alex_hobbies)
print("Hobbies Sam enjoy:", sam_hobbies)

# """"""Activity 6"""""""
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
grades["Diana"] = 88
grades["Bob"] = 95
above_80 = [(n, s) for n, s in grades.items() if s > 80]
average = sum(grades.values()) / len(grades)
print(grades)
print(f"Above 80: {above_80}")
print(f"Average: {average}")

# """"""Activity 7"""""""
contacts = {"Mom": "555-1234",
            "Dad": "555-5678",
            "Friend": "555-9012"}
contacts['Alex'] = '555-0911'
name = input("Enter name of contact: ")
print(f"{name}: {contacts.get(name, 'Not found')}")

for n, num in contacts.items():
    print(f'{n}: {num}')

# """"""Activity 8"""""""

with open('Les_Brown.txt', 'r') as myFile:
    content_list = myFile.readlines()

total = len(content_list)
print(content_list, f"Total number of lines is: {total}")







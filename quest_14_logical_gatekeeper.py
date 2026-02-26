age = int(input("Enter your age: "))
gold = int(input("Enter how many gold coins you have: "))

if age >= 18 and gold >= 20:
    print("Welcome to the club! ")
elif age < 18 and gold >= 20:
    print("You have enough gold, but you're too young.")
elif age >= 18 and gold < 20:
    print("You're old enough, but you need more gold.")
else:
    print("You're too young and too poor for entry.")
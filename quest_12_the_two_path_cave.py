correct_password = "dragon123"
user_password = input("Enter the password: ")

if user_password == correct_password:
    print("Access Granted")
else:
    print("Access Denied. Try again.")
secret_code = 42
attempts = 3

for attempt in range(1, attempts + 1):
    guess =  int(input(f"Attempt {attempt}/3 - Enter the secret code: "))

    if guess ==  secret_code:
        print("Access granted. Correct code.")
        break
    else:
        print("Incorrect code.")
else:
    print("Access denied. Too many failed attempts.")
    
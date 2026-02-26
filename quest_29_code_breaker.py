secret_code = 42          # Store the correct secret code
attempts = 3              # Maximum number of allowed attempts

# Loop from 1 to 3 (inclusive) to track attempts
for attempt in range(1, attempts + 1):

    # Ask the user for a guess and convert input to integer
    guess = int(input(f"Attempt {attempt}/3 - Enter the secret code: "))

    # Check if the guess matches the secret code
    if guess == secret_code:
        print("Access granted. Correct code.")
        break              # Stop the loop immediately if correct
    else:
        print("Incorrect code.")

# This else belongs to the for loop
# It runs ONLY if the loop finishes without hitting break
else:
    print("Access denied. Too many failed attempts.")
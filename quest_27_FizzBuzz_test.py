# Loop through numbers from 1 to 100 (101 is excluded)
for number in range(1, 101):
    # Check if the number is divisible by BOTH 3 and 5 first
    # We do this first because 15 is divisible by both,
    # and we don't want it to print just "Fizz" or just "Buzz"
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # If not both, check if divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # If not divisible by 3, check if divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # If none of the above conditions match, just print the number 
    else:
        print(number)

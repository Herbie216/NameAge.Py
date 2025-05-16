# Get user name
name = input("What is your name? ")

# Input check
if not name.strip().isalpha():
    print("Are you a robot? Try again")
    exit()

# Get user age
age_input = input("How old are you? ")

# Input check
if not age_input.strip().isdigit() or int(age_input) < 0:
    print("Silly human, you can't fool me!")
    exit()

# Input to Output vars
age = int(age_input)
year = 2025
born = year - age

# Output
print(f"Hello, {name}! You were born in {born}.")

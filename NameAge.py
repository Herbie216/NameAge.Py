# Get user name with validation loop
while True:
    name = input("What is your name? ")
    if name.strip().isalpha():
        break
    print("Are you a robot? Try again.")

# Get user age with validation loop
while True:
    age_input = input("How old are you? ")
    if age_input.strip().isdigit() and int(age_input) >= 0:
        age = int(age_input)
        break
    print("Silly human, you can't fool me!")

# Calculate birth year
year = 2025
born = year - age

# Output
print(f"Hello, {name.strip()}! You were born in {born}.")

# Pause so the user can see output
input("Press Enter to exit...")

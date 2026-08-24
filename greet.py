name = input("What's your name? ")

age_input = input("How old are you? ")
while not age_input.isdigit():
    print("'" + age_input + "' doesn't look like a whole number. Try again.")
    age_input = input("How old are you? ")

age = int(age_input)
print("Hello, " + name + "!")
print("In 10 years, you'll be " + str(age + 10) + " years old.")
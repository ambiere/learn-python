prompt = "Tell me your password: "
password = input(prompt)

if password:
    first_letter = password[0].upper()
    message = "The first letter you entered was: "
    print(f"{message}{first_letter}")
else:
    print("You provided empty password :/")

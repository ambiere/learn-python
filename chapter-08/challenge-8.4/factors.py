print("Factors of a Number\n")

prompt = "Enter a positive integer: "
integer = input(prompt)


def parse_input(str):
    try:
        return int(str)
    except ValueError:
        print("Invalid integer :/")
        exit(1)


integer = parse_input(integer)

print("")

for factor in range(1, integer+1):
    has_reminder = integer % factor
    if has_reminder > 0:
        continue
    else:
        print(f"{factor} is a factor of {integer}")

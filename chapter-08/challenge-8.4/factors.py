print("Factors of a Number\n")

prompt = "Enter a positive integer: "
integer = input(prompt)


def parseinput(str):
    try:
        return int(str)
    except ValueError:
        print("Invalid integer :/")
        exit(1)


integer = parseinput(integer)

print("")

for factor in range(1, integer+1):
    if integer % factor == 0:
        print(f"{factor} is a factor of {integer}")

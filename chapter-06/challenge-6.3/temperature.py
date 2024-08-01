print("Temperatures Conversion\n")
prompt_choice = "Convert temperature to:\n1: Celsius\n2: Fahrenheit\n\n"

choice_dict = {
    "2": "Celsius",
    "1": "Fahrenheit"
}


def get_context():
    try:
        choice_index = input(prompt_choice)
        return choice_dict[choice_index]
    except KeyError:
        print("[KeyError] Choice out of range :/")
        exit(1)


def parse_to_float(str):
    try:
        return float(str.strip())
    except ValueError:
        print(f"Invalid temperature value: {str}")
        exit(1)


context = get_context()
prompt_temp = f"\nEnter a temperature in degrees {context}: "

temp = input(prompt_temp)
temp = parse_to_float(temp)

if (context is choice_dict["2"]):
    converted_temp = temp * 9/5 + 32
    converted_temp = round(converted_temp, 2)
    print(f"{temp} degrees C = {converted_temp} degrees F")
else:
    converted_temp = (temp - 32) * 5/9
    converted_temp = round(converted_temp, 2)
    print(f"{temp} degrees F = {converted_temp} degrees C")

prompt_base = "Enter a base: "
prompt_exponent = "Enter an exponent: "

base = input(prompt_base)
exponent = input(prompt_exponent)


def convert_to_number(str):
    try:
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            message = f"You provided an incorrect value '{str}'"
            print(message)
            return


base = convert_to_number(base)
exponent = convert_to_number(exponent)

if base is not None and exponent is not None:
    result = base ** exponent
    print(f"{base} to the power of {exponent} = {result}")
else:
    exit()

print("Track Your Investments\n")

prompt_years = "Enter investment years: "
prompt_amount = "Enter a principal amount ($): "
prompt_rate = "Enter annual rate of return (float/integer): "


def invest(amount, rate):
    rate_not_none = rate is not None
    amount_not_none = amount is not None

    if rate_not_none and amount_not_none:
        return amount + amount * rate
    else:
        print("Invalid amount or rate :/")


def parse_input(str):
    str = str.strip()
    try:
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            print(f"[ValueError] '{str}' is invalid :/")
            exit(1)


def handle_float_years(parsed_years, years):
    if parsed_years.is_integer():
        return {
            "whole_year": parsed_years,
            "float_year": 0
        }
    else:
        whole_year = years.split(".")[0]
        float_year = years.split(".")[1]
        return {
            "whole_year": parse_input(whole_year),
            "float_year":  parse_input(f".{float_year}")
        }


def print_accumulation(amount, rate, years_dict):
    whole_year = years_dict["whole_year"]
    float_year = years_dict["float_year"]

    for year in range(1, whole_year + 1):
        amount = invest(amount, rate)
        print(f"year {year}: ${amount:,.2f}")

    # if the year provided is not whole number
    if float_year > 0:
        incremented_amount = invest(amount, rate) - amount
        amount = amount + (incremented_amount * float_year)
        print(f"year {whole_year + float_year}: ${amount:,.2f}")


amount = input(prompt_amount)
rate = input(prompt_rate)
years = input(prompt_years)

rate = parse_input(rate)
amount = parse_input(amount)
parsed_years = parse_input(years)

years = handle_float_years(parsed_years, years)


print_accumulation(amount, rate, years)

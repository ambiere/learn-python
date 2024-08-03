print("Track Your Investments\n")

PROMPT_YEARS = "Enter investment years: "
PROMPT_AMOUNT = "Enter a principal amount ($): "
PROMPT_RATE = "Enter annual rate of return (float/integer): "


def invest(amount, rate):
    ratevalid = rate is not None
    amountvalid = amount is not None

    if ratevalid and amountvalid:
        return amount + amount * rate
    else:
        print("Invalid amount or rate :/")


def parseinput(str):
    str = str.strip()
    try:
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            print(f"[ValueError] '{str}' is invalid :/")
            exit(1)


def floatyears(parsedyear, years):
    if parsedyear.is_integer():
        return (parsedyear, 0)
    else:
        whole = years.split(".")[0]
        float = years.split(".")[1]
        return (
            parseinput(whole),
            parseinput(f".{float}")
        )


def printgrowth(amount, rate, years):
    whole, float = years

    for year in range(1, whole + 1):
        amount = invest(amount, rate)
        print(f"year {year}: ${amount:,.2f}")

    # if the year provided is not whole number
    if float > 0:
        amountinc = invest(amount, rate) - amount
        amount = amount + (amountinc * float)
        print(f"year {whole + float}: ${amount:,.2f}")


amount = parseinput(input(PROMPT_AMOUNT))
rate = parseinput(input(PROMPT_RATE))
years = input(PROMPT_YEARS)

parsedyear = parseinput(years)
years = floatyears(parsedyear, years)

printgrowth(amount, rate, years)

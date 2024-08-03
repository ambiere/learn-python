import random


def coinflip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


flipcount = 0
NUMBER_TRIALS = 10_000

for trial in range(NUMBER_TRIALS):
    if coinflip() == "heads":
        flipcount = flipcount+1
        while coinflip() == "heads":
            flipcount = flipcount + 1
        flipcount = flipcount + 1
    else:
        flipcount = flipcount + 1
        while coinflip() == "tails":
            flipcount = flipcount + 1
        flipcount = flipcount + 1

averageflips = flipcount / NUMBER_TRIALS
print(f"The average number of flips per trial is {averageflips}")

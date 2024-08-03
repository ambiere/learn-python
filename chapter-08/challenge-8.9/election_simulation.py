import random


def regionalelection(chance):
    if random.random() < chance:
        return "A"
    else:
        return "B"


def election(chances):
    wonA = 0
    for chance in chances:
        if regionalelection(chance) == "A":
            wonA = wonA + 1

    wonB = len(chances) - wonA
    if wonA > wonB:
        return "A"
    else:
        return "B"


CHANCES = [0.87, 0.65, 0.17]
TRIALS = 10_000

winsA = 0

for trial in range(TRIALS):
    if election(CHANCES) == "A":
        winsA = winsA + 1


print(f"Probability A wins: {winsA / TRIALS}")
print(f"Probability B wins: {1 - (winsA / TRIALS)}")

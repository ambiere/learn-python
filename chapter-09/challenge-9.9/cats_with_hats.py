CATS = 100
ROUND = 100

cats = {}


def putHat(round):
    # track each stop
    for catIndex in range(1, CATS + 1):
        if round == 1:
            cats[catIndex] = True
        else:
            if catIndex % round == 0:
                if cats[catIndex]:
                    cats[catIndex] = False
                else:
                    cats[catIndex] = True


# keep track of round
for round in range(1, ROUND + 1):
    putHat(round)


for catIndex, hat in cats.items():
    if hat:
        print(f"cat #{catIndex} has a hat")
    else:
        print(f"cat #{catIndex} is hatless")

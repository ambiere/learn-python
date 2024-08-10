import random

NOUNS = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla"
]

VERBS = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles"
]

ADJECTIVES = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening"
]


PREPOSITIONS = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within"
]

ADVERBS = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously"
]


def makePoem():
    n1, n2, n3 = random.choices(NOUNS, k=3)
    v1, v2, v3 = random.choices(VERBS, k=3)
    adv1, adv2, adv3 = random.choices(ADVERBS, k=3)
    adj1, adj2, adj3 = random.choices(ADJECTIVES, k=3)
    prep1, prep2, prep3 = random.choices(PREPOSITIONS, k=3)

    article = "A"

    if "aeiou".find(adj1[0]) > -1:
        article = "An"

    poem = (
        f"{article} {adj1} {n1}\n\n"
        f"{article} {adj1} {n1} {v1} {prep1} the {adj2} {n2}\n"
        f"{adv1}, the {n1} {v2}\n"
        f"the {n2} {v3} {prep2} a {adj3} {n3}"
    )

    return poem


poem = makePoem()
print(poem)

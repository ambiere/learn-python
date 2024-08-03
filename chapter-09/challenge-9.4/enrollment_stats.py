UNIVERSITIES = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollmentStats(input):
    studentValue = [uni[1] for uni in input]
    tuitionFees = [uni[2] for uni in input]
    return studentValue, tuitionFees


def mean(data):
    return sum(data) / len(data)


def median(data):
    data.sort()
    if len(data) % 2 == 1:
        centerIndex = len(data) / 2
        return data[int(centerIndex)]
    else:
        centerLeft = (len(data) - 1) // 2
        centerRight = (len(data) + 1) // 2
        return mean([data[centerLeft], data[centerRight]])


data = enrollmentStats(UNIVERSITIES)

print("")
print("*****" * 6)
print(f"Total students:   {sum(data[0]):,}")
print(f"Total tuition:  $ {sum(data[1]):,}")
print(f"\nStudent mean:     {mean(data[0]):,.2f}")
print(f"Student median:   {median(data[0]):,}")
print(f"\nTuition mean:   $ {mean(data[1]):,.2f}")
print(f"Tuition median: $ {median(data[1]):,}")
print("*****" * 6)
print("")

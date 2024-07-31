prompt = "Enter some text: "
text = input(prompt)

if text:
    converted = text.replace("a", "4")
    converted = converted.replace("b", "8")
    converted = converted.replace("e", "3")
    converted = converted.replace("l", "1")
    converted = converted.replace("o", "0")
    converted = converted.replace("s", "5")
    converted = converted.replace("t", "7")

    print(converted)
else:
    print("No text entered :/")

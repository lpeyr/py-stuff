alphabet = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-Ray",
    "Y": "Yankee",
    "Z": "Zulu",
    " ": " ",
    ".": ".",
    ",": ",",
    "É": "Echo",
    "È": "Echo",
    "Ê": "Echo",
    "Ë": "Echo",
    "Â": "Alpha",
    "À": "Alpha",
    "Ä": "Alpha",
    "Ç": "Charlie",
    "'": " "
}

text = input("Enter text\n> ")
s = ""
for c in text:
    s += f"{alphabet[c.upper()]} "

print(s.upper())

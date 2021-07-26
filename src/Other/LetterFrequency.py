import matplotlib.pyplot as plt
from string import ascii_uppercase

def countSpecific(_path, _letter):
    _letter = _letter.strip().upper()
    file = open(_path, 'rb')
    text = str(file.read())
    return text.count(_letter) + text.count(_letter.lower())

def countAll(_path):
    file = open(_path, "rb")
    text = str(file.read())
    letters = dict.fromkeys(ascii_uppercase, 0)
    for char in text:
        if char.isalpha():
            letters[char.upper()]+=1

    return letters

D = countAll("src\\Other\\test.txt")
print(D)
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))


plt.show()
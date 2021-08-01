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

path = input("What file would you like to use? (text.txt) ")
D = countAll("src\\Other\\" + path)
# D = D | countAll("src\\Other\\" + path)
# S = {k: v for k, v in sorted(D.items(), key=lambda item: item[1])}
print(D)
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))


plt.show()
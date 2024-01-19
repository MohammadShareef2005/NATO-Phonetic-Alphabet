import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic = {nato.letter: nato.code for (index, nato) in data.iterrows()}

word = input().upper()
lis = [phonetic[n] for n in word]
print(lis)

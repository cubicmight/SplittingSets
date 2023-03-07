import os
import csv

partisanship = r"C:\Users\838sa\Downloads\phrase_partisanship"
x = os.listdir(partisanship)
y = []
for f in x:
    if 'partisan_phrases_' in f:
        y.append(f)
phrases = []
for file in y:
    join = os.path.join(partisanship, file)
    with open(join, 'r') as datafile:
        next(datafile)  ##skip first line (table header)
        for line in datafile:
            splitted = line.split("|")
            splitted[1] = splitted[1].strip()
            phrases.append(splitted)

with open('result.txt', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(phrases)

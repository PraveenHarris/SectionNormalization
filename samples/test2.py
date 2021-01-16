import csv
from ../python/normalization/normalizer import Normalizer

sections = []
with open('metstest.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        x = line[0].lower()
        sections.append(x)
        # print(line)
sections = sections[1:]
# print(sections, len(sections))

s = []
for sec in sections:
    sec = ''.join(dig for dig in sec if dig.isdigit())
    s.append(int(sec))

for x, y in zip(s, sections):
    print(x, y)

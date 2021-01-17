import csv
from normalizer import Normalizer

normalizer = Normalizer()
# normalizer.read_manifest('../../manifests/citifield_sections.csv')
normalizer.read_manifest('../../manifests/dodgerstadium_sections.csv')

inp = []
correct = []

with open('../../samples/dodgertest.csv') as file:
    # with open('../../samples/metstest.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        inp.append({'section': line[0],
                    'row': line[1]})
        if line[4].strip() == 'True':
            correct.append(
                {'section_id': line[2], 'row_id': line[3], 'valid': True})
        else:
            correct.append(
                {'section_id': line[2], 'row_id': line[3], 'valid': False})

inp = inp[1:]
correct = correct[1:]
assert len(inp) == len(correct)

i1 = inp[0]
c1 = correct[0]

right = 0
wrong = 0
count = 0
cc = 0

for i, c in zip(inp, correct):
    count += 1
    # try:
    section_id, row_id, valid = normalizer.normalize(
        i['section'], i['row'])
    # if not valid:
    # print(count, section_id, row_id)
    if section_id != c['section_id'] or row_id != c['row_id'] or valid != c['valid']:
        cc += 1
        wrong += 1
        if cc == 3:
            print(i, c)
            print('count: ', count, 'section id: ', section_id,
                  'row id: ', row_id, 'valid: ', valid)
    else:
        right += 1
    # except:
    #     wrong += 1
    # print(section_id, c['section_id'])
    # print(row_id, c['row_id'])
    # print(valid, c['valid'])

    # if section_id != c['section_id'] or row_id != c['row_id'] or valid != c['valid']:
    #     wrong += 1
    # else:
    #     right += 1

print(right, wrong)

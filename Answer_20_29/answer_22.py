import json

with open("jawiki-country.json", 'r') as f:
    for line in f.readlines():

        # str > dict
        line = json.loads(line)

        if line['title'] == 'イギリス':
            text = line['text']

for l in text.split('\n\n'):
    if 'Category' in l:
        category = l

for l in category.split('\n'):
    if 'Category' in l:
        cate = l.replace('[', '').replace(']', '').split(':')[-1]
        print(cate)

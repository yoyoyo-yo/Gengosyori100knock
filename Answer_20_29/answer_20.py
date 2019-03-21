import json

with open("jawiki-country.json", 'r') as f:
    for line in f.readlines():

        # str > dict
        line = json.loads(line)

        if line['title'] == 'イギリス':
            print(line['text'])


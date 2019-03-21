import json
import re

with open("jawiki-country.json", 'r') as f:
    for line in f.readlines():

        # str > dict
        line = json.loads(line)

        if line['title'] == 'イギリス':
            text = line['text']

matches = re.findall(r"File:.*", text) + re.findall(r"ファイル:.*", text)
            
for match in matches:
    print(match.split(':')[-1].split('|')[0])


import json
import re

with open("jawiki-country.json", 'r') as f:
    for line in f.readlines():

        # str > dict
        line = json.loads(line)

        if line['title'] == 'イギリス':
            text = line['text']


# answer 1
for i, match in enumerate(re.findall(r'===.*===', text)):
    print(i, match)
    i += 1
            
# answer 2
"""
ind = 0

for l in text.split('\n\n'):
    match = re.search(r"===.*===", l)
    if match:
        print(ind, match.group(0))
        ind += 1
"""

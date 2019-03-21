import json
import re

with open("jawiki-country.json", 'r') as f:
    for line in f.readlines():

        # str > dict
        line = json.loads(line)

        if line['title'] == 'イギリス':
            text = line['text']

match = re.findall("基礎情報.*\n}}", text, re.DOTALL)[0]

dic = {}

for m in match.split('\n')[1:]:
    if m[0] == '|':
        m = m[1:]
        spl = m.split('=')
        key = spl[0].strip()
        val = spl[1].strip()
    else:
        val += '\n' + m

    val = val.replace("*", '').replace('[', '').replace(']', '')
    
    dic[key] = val

print(dic)

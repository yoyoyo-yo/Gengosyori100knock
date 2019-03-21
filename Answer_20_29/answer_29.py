import json
import re
import requests

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

    val = val.replace("*", '').replace('[', '').replace(']', '').replace('=', '').replace('#', '').replace('"', '').replace(';', '')
    
    dic[key] = val


url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(dic['国旗画像']),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

json_data = requests.get(url, params=payload).json()
query = json_data['query']['pages']['23473560']['imageinfo'][0]['url']

print(query)

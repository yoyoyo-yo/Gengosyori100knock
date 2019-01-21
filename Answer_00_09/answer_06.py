def ngram(text, n=2):
    ws = []
    cs = []

    spl = text.split(' ')
    for i in range(len(spl) - (n-1)):
        gram = ''
        for _t in spl[i:i+n]:
            gram += _t + ' '
        gram = gram.strip()
        ws.append(gram)

    _text = text.replace(' ', '')
    for i in range(len(_text) - (n-1)):
        cs.append(_text[i:i+n])

    return ws, cs

a1 = "paraparaparadise"
a2 = "paragraph"

ws1, cs1 = ngram(a1, n=2)
ws2, cs2 = ngram(a2, n=2)

# Sum Set
S = [a for a in cs1]
for _w in cs2:
    if _w not in S:
        S.append(_w)

# Diff Set
## answer 1
D = list(set(cs2) - set(cs1))
D += list(set(cs1) - set(cs2))

## answer 2
"""
D = []
for _w in cs1:
    if _w not in cs2:
        D.append(_w)
        
for _w in cs2:
    if _w not in cs1:
        D.append(_w)
"""

key = 'se'

S_in = True if key in S else False
D_in = True if key in D else False

print("Sum set:", S)
print("Diff set:", D)

print("whether S contains", key, 'or not:', S_in)
print("whether D contains", key, 'or not:', D_in)


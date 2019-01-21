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

a = "I am an NLPer"

ws, cs = ngram(a, n=2)

print("word bi-gram:", ws)
print("char bi-gram:", cs)

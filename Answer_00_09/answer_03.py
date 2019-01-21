a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

cs = []

for _a in a.split(' '):
    _a = _a.replace(",", "")
    cs.append(len(_a))

print(cs)

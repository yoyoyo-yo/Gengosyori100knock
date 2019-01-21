a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

b = ''

for _a in a:
    b += chr(219 - ord(_a)) if _a.islower() else _a
    
print(b)

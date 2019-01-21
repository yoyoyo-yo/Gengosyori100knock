import random
random.seed(0)

a = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

b = ''

for _a in a.split(' '):
    if len(_a) < 4:
        b += _a + ' '
    else:
        begin = _a[0]
        end = _a[-1]
        inter = _a[1:-1]
        c = ''
        for _c in random.sample(inter, len(inter)):
            c += _c

        b += begin + c + end + ' '

b = b.strip()

print(b)

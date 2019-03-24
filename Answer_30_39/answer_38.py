import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

mappings = []

with open("neko.txt.mecab", 'r') as f:
    #print(f.read())
    for line in f.readlines():
        spl = line.strip().split('\t')
        if len(spl) != 2:
            continue
        surface, parse = spl

        spl = parse.split(',')
        if len(spl) == 9:
            pos, pos1, pos2, pos3, act1, act2, base, read, pron = spl
        elif len(spl) == 7:
            pos, pos1, pos2, pos3, act1, act2, base = spl

        mapping = {'surface': surface,
                   'base': base,
                   'pos': pos,
                   'pos1': pos1}

        mappings.append(mapping)


# histogram

hists = {}
        
for mapping in mappings:
    w = mapping['surface']
    if w in hists.keys():
        hists[w] += 1
    else:
        hists[w] = 1

# sort
        
hists_sort_w = []
hists_sort_c = []

maximum = 0
maximum_w = None

while len(hists.keys()) > 0:

    maximum = 0
        
    for key, count in hists.items():
        if count > maximum:
            if key not in hists_sort_w:
                maximum = count
                maximum_w = key

    hists.pop(maximum_w)
            
    hists_sort_w.append(maximum_w)
    hists_sort_c.append(maximum)


# display bar graph   
plt.hist(hists_sort_c, bins=10)
plt.show()

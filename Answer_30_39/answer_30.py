
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
        

print(mappings)

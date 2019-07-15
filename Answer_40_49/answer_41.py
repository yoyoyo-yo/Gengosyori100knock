
class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def display(self):
        print("surface:", self.surface, end=' ')
        print("base:", self.base, end=' ')
        print("pos:", self.pos, end=' ')
        print("pos1:", self.pos1)


class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

        
        
# make Morph
        
with open("neko.txt.cabocha", 'r') as f:

    morphs = []
    chunks = []
    sentences = []
    
    for l in f.readlines()[4:]:
        l = l.strip()

        if l == 'EOS':
            if len(morphs) > 0:
                chunk = Chunk(morphs=morphs, dst)
                chunks.append(chunk)
                morphs = []

            if len(chunks) > 0:
                sentences.append(chunks)
                
            chunks = []
                
            continue
        
        spl = l.split('\t')
        
        if len(spl) > 1:
            surface, parse = spl
            
            spl2 = parse.split(',')
            if len(spl2) == 9:
                pos, pos1, pos2, pos3, katsuyokei, katsuyogata, base, read, pron = spl2
            else:
                pos, pos1, pos2, pos3, katsuyokei, katsuyogata, base = spl2

            morph = Morph(surface=surface, base=base, pos=pos, pos1=pos1)
            morphs.append(morph)

        else:
            if len(morphs) > 0:
                chunk = Chunk(morphs=morphs, dst)
                chunks.append(chunk)
                morphs = []
                
            spl = spl[0].split(' ')
            _, chunk_num, dst, syuji_kino, score = spl

            print(spl)

for mor in sentences[4]:
    mor.display()

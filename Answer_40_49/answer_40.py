
class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def display(self):
        print(" [surface] {} [base] {} [pos] {} [pos1] {}".format(
            self.surface, self.base, self.pos, self.pos1))


# make Morph
        
with open("neko.txt.cabocha", 'r') as f:

    sentence = []
    sentences = []
    
    for l in f.readlines()[4:]:
        l = l.strip()

        if l == 'EOS':
            if len(sentence) > 0:
                sentences.append(sentence)
            sentence = []
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
            sentence.append(morph)


sentence_N = 4

print("sentence", sentence_N)

for mor in sentences[4]:
    mor.display()

DEBUG = False


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def display(self):
        print(" [surface] {} [base] {} [pos] {} [pos1] {}".format(
            self.surface, self.base, self.pos, self.pos1))


class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def display(self):
        for i, morph in enumerate(self.morphs):
            print("morph {}:".format(i))
            morph.display()
        print("dst:", self.dst, end=' ')
        print("srcs:", self.srcs)

        
# make Morph
with open("neko.txt.cabocha", 'r') as f:

    morphs = []
    kakarisaki_index_list = []
    morphs_per_chunk = []
    kakarisaki_pairs = []
    dsts = []
    bunsetsu_index = 0
    sentences = []
    chunks = []
    
    # each line
    for l in f.readlines()[4:]:
        # strip
        l = l.rstrip()

        if l == "EOS":
            if len(dsts) < 1:
                continue

            # add last morphs to morphs_per_chunk
            morphs_per_chunk.append(morphs)

            # get kakarimoto
            chunk_N = bunsetsu_index + 1

            # count kakarimoto index list
            srcs = [[] for _ in range(chunk_N)]
            
            for kakarimoto_index, kakarisaki_index in kakarisaki_pairs:
                srcs[kakarisaki_index].append(kakarisaki_index)

            if DEBUG:
                print("Chunk number :", chunk_N)
                print("morphs list per chunk :", morphs_per_chunk)
                print("dst list :", dsts)
                print("srcs list :", srcs)

            for i in range(chunk_N):
                chunk = Chunk(morphs=morphs_per_chunk[i], dst=dsts[i], srcs=srcs[i])
                chunks.append(chunk)

            sentences.append(chunks)
            chunks = []

            morphs = []
            morphs_per_chunk = []
            dsts = []
            kakarisaki_index_list = []
            kakarisaki_pairs = []
        
        # kakarisaki information case
        elif l[0] == "*":
            if DEBUG:
                print(l)

            # if morph list contains more than one morph instance
            if len(morphs) > 0:
                morphs_per_chunk.append(morphs)
                morphs = []

            # parse by space
            _, bunsetsu_index, kakarisaki_index, keitaiso_index, kakarisaki_score = l.split(" ")

            # get kakarisaki_index
            kakarisaki_index = int(kakarisaki_index[:-1])
            kakarisaki_index_list.append(kakarisaki_index)

            # add kakarisaki_index to dsts
            dsts.append(kakarisaki_index)

            # change type
            bunsetsu_index = int(bunsetsu_index)

            # add pairs to count kakarimoto list in EOS
            kakarisaki_pairs.append([bunsetsu_index, kakarisaki_index])
            

        # parse case
        else:
            if DEBUG:
                print(l)

            # split by tab
            surface, parse = l.split("\t")

            # split by camma
            spl2 = parse.split(",")

            # get parsed information
            if len(spl2) == 9:
                pos, pos1, pos2, pos3, katsuyokei, katsuyogata, base, read, pron = spl2
            else:
                pos, pos1, pos2, pos3, katsuyokei, katsuyogata, base = spl2

            # get morph instance
            morph = Morph(surface=surface, base=base, pos=pos, pos1=pos1)
            # add morph list
            morphs.append(morph)


sentence_N = 4

print("sentence", sentence_N)

for i, chunk in enumerate(sentences[sentence_N]):
    print("Chunk", i)
    chunk.display()
    print()

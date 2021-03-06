DEBUG = False

import matplotlib.pyplot as plt
import os


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
                srcs[kakarisaki_index].append(kakarimoto_index)

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


with open('answer_45.txt', 'w') as f:
    for sentence_N in range(len(sentences)):
        print("--\nsentence :", sentence_N)
        # prepare text list
        texts = []
        poss = []

        # each chunk
        for i, chunk in enumerate(sentences[sentence_N]):
            text = ""
            pos = []

            # concatenate each surface
            for morph in chunk.morphs:
                text += morph.surface
                pos.append(morph.pos)

            texts.append(text)
            poss.append(pos)

        kakus = {}

        for index in range(len(sentences[sentence_N])):
            chunk = sentences[sentence_N][index]
            text = texts[index]
            pos = poss[index]

            # add text to text list
            texts.append(text)

            # get kakarisaki text
            dst = chunk.dst

            if dst > -1:
                kakarisaki = texts[dst]
                kakarisaki_chunk = sentences[sentence_N][dst]
            else:
                continue


            verb = ''
            # get kakarisaki verb base
            for _morph in kakarisaki_chunk.morphs:
                if '動詞' == _morph.pos:
                    verb = _morph.base
                    kakus[verb] = []
                    break

            if verb == '':
                continue

            for _morph in chunk.morphs:
                if '助詞' == _morph.pos:
                    kakus[verb] += [_morph.surface]
                    #kaku += _morph.surface + ' '

        for key, item in kakus.items():
            if len(item) < 1:
                continue

            kaku = ' '.join(item)
            data = '{}\t{}'.format(key, kaku)
            print(data)
            f.write(data + '\n')
        
            """
            if ("名詞" in pos) and ("動詞" in poss[dst]):
                print(kakarisaki)
                kakarisaki_chunk.display()
                #for _morph in chunk.morphs:


                print(text + "\t" + kakarisaki)
                if text != '' or kakarisaki != '':
                    text = text.replace('\'', '')
                    f.write('    {} -> {};\n'.format(text, kakarisaki))
            """


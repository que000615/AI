import picture
# translate dot matrix to pinyin
alphabet = {
    'b': (1,1,0,0,0,0),
    'p': (1,1,1,1,0,0),
    'm': (1,0,1,1,0,0),
    'f': (1,1,0,1,0,0),
    'd': (1,0,0,1,1,0),
    't': (0,1,1,1,1,0),
    'n': (1,0,1,1,1,0),
    'l': (1,1,1,0,0,0),
    'g': (1,1,0,1,1,0),
    'j': (1,1,0,1,1,0),
    'k': (1,0,1,0,0,0),
    'q': (1,0,1,0,0,0),
    'h': (1,1,0,0,1,0),
    'x': (1,1,0,0,1,0),
    'zh': (0,0,1,1,0,0),
    'ch': (1,1,1,1,1,0),
    'sh': (1,0,0,0,1,1),
    'r': (0,1,0,1,1,0),
    'z': (1,0,1,0,1,1),
    'c': (1,0,0,1,0,0),
    's': (0,1,1,1,0,0),

    'a': (0,0,1,0,1,0),
    'o': (0,1,0,0,0,1),
    'e': (0,1,0,0,0,1),
    'i': (0,1,0,1,0,0),
    'u': (1,0,1,0,0,1),
    'v': (0,0,1,1,0,1),
    'er': (1,1,1,0,1,0),
    'ai': (0,1,0,1,0,1),
    'ao': (0,1,1,0,1,0),
    'ei': (0,1,1,1,0,1),
    'ou': (1,1,1,0,1,1),
    'ia': (1,1,0,1,0,1),
    'iao': (0,0,1,1,1,0),
    'ie': (1,0,0,0,1,0),
    'iu': (1,1,0,0,1,1),
    'ua': (1,1,1,1,1,1),
    'uai': (1,0,1,1,1,1),
    'ui': (0,1,0,1,1,1),
    'uo': (1,0,1,0,1,0),
    've': (0,1,1,1,1,1),
    'an': (1,1,1,0,0,1),
    'ang': (0,1,1,0,0,1),
    'en': (0,0,1,0,1,1),
    'eng': (0,0,1,1,1,1),
    'ian': (1,0,0,1,0,1),
    'iang': (1,0,1,1,0,1),
    'in': (1,1,0,0,0,1),
    'ing': (1,0,0,0,0,1),
    'uan': (1,1,0,1,1,1),
    'uang': (0,1,1,0,1,1),
    'un': (0,1,0,0,1,0),
    'ong': (0,1,0,0,1,1),
    'van': (1,1,1,1,0,1),
    'vn': (0,0,0,1,1,1),
    'iong': (1,0,0,1,1,1)
}
dot = {}
for each in alphabet.items():
    if tuple(each[1]) in dot.keys():
        dot[tuple(each[1])].append(each[1])
    else:
        dot[tuple(each[1])] = [each[0]]
#print(dot)

yinbiao = [(1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),(0,1,1,0,0,0)]

# test if there are collision, except for g/j, k/q, h/x, o/e
def ts():
    for i in alphabet:
        for j in alphabet:
            if i != j and alphabet[i] == alphabet[j]:
                print("colision! ",i,j,alphabet[i])
#ts()
dotArray = picture.getDot()
index = 0
ret = [[]]
for i in dotArray:
    if tuple(i) not in yinbiao:
        ret[index] += dot[tuple(i)][0]
    else:
        ret.append([])
        index += 1

# combine each string
ret2 = []
for i in ret:
    ret2.append(''.join(i))

def getString():
    return ret2

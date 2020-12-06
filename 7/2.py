from common import parse


def abas(supernets):
    abas = []
    for supernet in supernets:
        for i in range(len(supernet) - 2):
            three = supernet[i: i + 3]
            if three[0] == three[2] and three[0] != three[1]:
                abas.append(three)
    return abas


def to_bab(aba):
    return aba[1] + aba[0] + aba[1]


with open('input.txt') as data:
        print(sum(any(to_bab(aba) in hypernet
                  for aba in abas(supernets)
                  for hypernet in hypernets)
                  for supernets, hypernets in map(parse, data)))

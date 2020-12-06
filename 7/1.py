from common import parse


def has_abba(sequence):
    for i in range(len(sequence) - 3):
        four = sequence[i: i + 4]
        if four == four[::-1] and four[0] != four[1]:
            return True
    return False


with open('input.txt') as data:
    print(sum(any(map(has_abba, supernets)) and
              not any(map(has_abba, hypernets))
              for supernets, hypernets in map(parse, data)))

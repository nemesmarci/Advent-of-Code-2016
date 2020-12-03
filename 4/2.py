from common import parse

A = ord('a')
Z = ord('z')


def decrypt(word, iterations):
    return ''.join(' ' if char == '-' else
                   chr(A + (ord(char) - A + iterations) % (Z - A + 1))
                   for char in word)


with open('input.txt') as data:
    for line in data:
        encrypted, sector, _ = parse(line)
        if decrypt(encrypted, int(sector)) == 'northpole object storage':
            print(sector)
            break

def decompress(sequence, version):
    i = 0
    marker = False
    length = ''
    times = ''
    decompressed = 0
    while i < len(sequence):
        char = sequence[i]
        if char == '(' and not marker:
            marker = True
        elif marker:
            while char != 'x':
                length += char
                i += 1
                char = sequence[i]
            length = int(length)
            i += 1  # skip 'x'
            char = sequence[i]
            while char != ')':
                times += char
                i += 1
                char = sequence[i]
            times = int(times)
            i += 1  # skip ')'
            decompressed += times * (length if version == 1 else
                                     decompress(sequence[i: i + length],
                                                version=2))
            i += length - 1
            marker = False
            length = ''
            times = ''
        else:
            decompressed += 1
        i += 1
    return decompressed


def solve(version):
    with open('input.txt') as data:
        return decompress(data.read().strip(), version)

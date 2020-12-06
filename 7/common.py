import re

SUPERNET = re.compile(r'[a-z]+')
HYPERNET = re.compile(r'\[[a-z]+]')


def parse(ip):
    hypernets = [hypernet[1:-1] for hypernet in re.findall(HYPERNET, ip)]
    supernets = [supernet for supernet in re.findall(SUPERNET, ip)
                 if supernet not in hypernets]
    return supernets, hypernets

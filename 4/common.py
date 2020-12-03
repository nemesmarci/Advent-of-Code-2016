import re

RE = re.compile(r'((?:\w+-)+\w+)-(\d+)\[(\w+)]')


def parse(line):
    return re.match(RE, line).groups()

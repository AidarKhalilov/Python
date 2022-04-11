import re


def parse_keys(x):
    keys = r"\w+"
    return re.findall(keys, x)


def parse(x):
    result = {}
    p = re.findall(r'\([\s]*\w+[\s;]*\w+[\s;]*\w+[\s;]*\w+', x)
    s = re.findall(r'`\w+', x)
    keys = parse_keys(''.join(str(e) for e in s))
    for i in range(len(keys)):
        result[keys[i]] = parse_keys(p[i])
    return result


def main(x):
    parse(x)


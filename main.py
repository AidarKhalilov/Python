import re


def parse_value(x):
    return re.findall(r"\w+", x)


def parse(x):
    result = {}
    keys = re.findall(r'(?<=var\s)\w+', x)
    values = re.findall(r'(?<=array\()[^)]+', x)
    keys_values = []
    for i in range(len(keys)):
        result[keys[i]] = parse_value(values[i])
    return result


print(parse("begin(( var xeza<==array( @'rige' . @'orus' . @'ries_278' ). ))."
            "((var bibe_339<== array(@'inatat_92' . @'geon_269' . @'tiveso'.@'male'). "
            ")).(( var zaer <== array( @'maendi_298' . @'arte_937' .@'rigedi_817'). "
            ")). end"))
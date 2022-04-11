from struct import *


def get_bstruct(x, offset):
    offset = unpack_from('I', x, offset)[0]
    result = {'B1': unpack_from('h', x, offset)[0],
              'B2': unpack_from('b', x, offset + 2)[0],
              'B3': unpack_from('H', x, offset + 3)[0],
              'B4': unpack_from('B', x, offset + 5)[0]}
    return result


def get_cstruct(x, offset):
    offset = unpack_from('I', x, offset)[0]
    result = {'C1': unpack_from('b', x, offset)[0],
              'C2': unpack_from('B', x, offset + 1)[0],
              'C3': get_dstruct(x, offset + 2),
              'C4': unpack_from('q', x, offset + 10)[0]}
    offset += 18
    result['C5'] = array_help([], 8, 2, x, offset, 'H')
    result['C6'] = unpack_from('i', x, offset + 16)[0]
    offset += 20
    result['C7'] = array_help([], 4, 4, x, offset, 'i')
    result['C8'] = {'E1': unpack_from('b', x, offset + 16)[0],
                    'E2': unpack_from('q', x, offset + 17)[0],
                    'E3': unpack_from('H', x, offset + 25)[0],
                    'E4': unpack_from('d', x, offset + 27)[0],
                    'E5': unpack_from('h', x, offset + 35)[0]}
    return result


def get_dstruct(x, offset):
    size = unpack_from('I', x, offset)[0]
    offset = unpack_from('I', x, offset + 4)[0]
    result = []
    for i in range(size):
        result.append(dstruct(x, offset))
        offset += 10
    return result


def dstruct(x, offset):
    result = {'D1': unpack_from('B', x, offset)[0]}
    array_size = unpack_from('H', x, offset + 1)[0]
    array_offset = unpack_from('I', x, offset + 3)[0]
    result['D2'] = array_help([], array_size, 2, x, array_offset, 'h')
    result['D3'] = unpack_from('b', x, offset + 7)[0]
    result['D4'] = unpack_from('H', x, offset + 8)[0]
    return result


def array_help(array, size, inc, x, offset, formation):
    for i in range(size):
        array.append(unpack_from(formation, x, offset)[0])
        offset += inc
    return array


def main(x):
    array = []
    offset = 33
    result = {'A1': get_bstruct(x, 5), 'A2': get_cstruct(x, 9),
              'A3': unpack_from('I', x, 13)[0],
              'A4': unpack_from('Q', x, 17)[0],
              'A5': unpack_from('q', x, 25)[0],
              'A6': array_help(array, 3, 2, x, offset, 'h'),
              'A7': unpack_from('B', x, offset + 6)[0],
              'A8': unpack_from('d', x, offset + 7)[0]}
    return result

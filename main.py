from struct import *


def get_bstruct(data, variable):
    offset = unpack_from('I', data, variable)[0]
    result = []
    first = {'B1': unpack_from('b', data, offset)[0]}
    first['B2'], offset = get_cstruct(data, offset + 1)
    first['B3'] = unpack_from('h', data, offset)[0]
    first['B4'] = unpack_from('B', data, offset + 2)[0]
    first['B5'] = unpack_from('b', data, offset + 3)[0]
    result.append(first)
    second = {'B1': unpack_from('b', data, offset + 4)[0]}
    second['B2'], offset = get_cstruct(data, offset + 5)
    second['B3'] = unpack_from('h', data, offset)[0]
    second['B4'] = unpack_from('B', data, offset + 2)[0]
    second['B5'] = unpack_from('b', data, offset + 3)[0]
    result.append(second)
    third = {'B1': unpack_from('b', data, offset + 4)[0]}
    third['B2'], offset = get_cstruct(data, offset + 5)
    third['B3'] = unpack_from('h', data, offset)[0]
    third['B4'] = unpack_from('B', data, offset + 2)[0]
    third['B5'] = unpack_from('b', data, offset + 3)[0]
    result.append(third)
    return result


def get_cstruct(data, variable):
    result = []
    first = {'C1': unpack_from('b', data, variable)[0],
             'C2': unpack_from('d', data, variable + 1)[0]}
    result.append(first)
    second = {'C1': unpack_from('b', data, variable + 9)[0],
              'C2': unpack_from('d', data, variable + 10)[0]}
    result.append(second)
    return result, variable + 18


def get_dstruct(data, variable):
    size = unpack_from('I', data, variable)[0]
    offset_x = unpack_from('I', data, variable + 4)[0]
    size_y = unpack_from('I', data, variable + 8)[0]
    offset_y = unpack_from('H', data, variable + 12)[0]
    result = {}
    first = []
    second = []
    for i in range(size):
        first.append(unpack_from('Q', data, offset_x)[0])
        offset_x += 8
    for j in range(size_y):
        second.append(unpack_from('d', data, offset_y)[0])
        offset_y += 8
    result['D1'] = first
    result['D2'] = second
    return result


def main(data):
    offset = 5
    result = {'A1': unpack_from('b', data, offset)[0],
              'A2': get_bstruct(data, offset + 1),
              'A3': unpack_from('I', data, offset + 13)[0],
              'A4': get_dstruct(data, offset + 17),
              'A5': unpack_from('d', data, offset + 31)[0],
              'A6': unpack_from('b', data, offset + 39)[0]}
    return result


print(main(b'\x8fGCYG\xac-\x00\x00\x00D\x00\x00\x00[\x00\x00\x00-\xfdK*\x02\x00'
           b'\x00\x00r\x00\x00\x00\x02\x00\x00\x00\x82\x00\x80c\xae\x9f\x05B\xaf\xbf'
           b'\xf4\xa1cD`\xe7B`\x1f\xe8?@0)1Z\x1fp\xeb?o\xc2\xa5QO70\xa3\x15\xfe\x1a\xa7'
           b'\xcb?c\xd4<+\xc7\xc7\xb1\xd0\xbf\x1d\x0b\x0c\x1b\x9b\xe1\x0c\xbf\xac'
           b'\xdesP\xdf\xbfD\xc6\x9b\x9a\xd1\xb0\x97\xea?\xbb \x86[\xa1\x11\xa5%_\xdb'
           b'\x7f\x80\x9e(\xd9\xe9J4\x98\x96\x80S\x8fX\xcb\xcf\x93\xbf@\xca'
           b'\xc0\x88\xf1\xe0\xa2?'))

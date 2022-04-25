from enum import Enum
from struct import unpack_from, calcsize


class Types(Enum):
    float = "f"
    uint64 = "Q"
    uint32 = "I"
    uint16 = "H"
    uint8 = "B"
    int64 = "q"
    int32 = "i"
    int16 = "h"
    int8 = "b"
    char = "c"
    double = "d"


class BinaryReader():
    def __init__(self, offset, source):
        self.offset = offset
        self.source = source

    def read(self, pattern):
        pattern = pattern.value
        result = unpack_from(pattern, self.source, self.offset)
        self.offset += calcsize(pattern)
        return result[0]


def a(reader: BinaryReader):
    a11 = reader.read(Types.uint16)
    a1 = c(reader)
    a2 = reader.read(Types.int64)
    a3 = masser_a(5, reader.offset, reader.source, Types.int16)
    a4 = reader.read(Types.uint8)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4)


def b(reader: BinaryReader):
    b1 = masser_b(2, reader.offset, reader.source)
    b2 = masser_c(8, reader.offset, reader.source)
    b3 = reader.read(Types.double)
    b41 = reader.read(Types.uint32)
    b4 = d(reader)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4)


def c(reader: BinaryReader):
    c1 = reader.read(Types.float)
    c2 = reader.read(Types.float)
    return dict(C1=c1, C2=c2)


def d(reader: BinaryReader):
    d11 = reader.read(Types.uint32)
    d12 = reader.read(Types.uint32)
    d1 = masser_a(d11, d12, reader.source, Types.int64)
    d2 = reader.read(Types.uint32)
    d3 = masser_a(2, reader.offset, reader.source, Types.uint16)
    return dict(D1=d1, D2=d2, D3=d3)


def masser_a(size, offset, source, type):
    rez = []
    read = BinaryReader(offset, source)
    for i in range(size):
        rez.append(read.read(type))
    return rez


def masser_b(size, offset, source):
    rez = []
    read = BinaryReader(offset, source)
    while read.offset < offset + size:
        rez.append(c(read))
    return rez


def masser_c(size, offset, source):
    rez = ""
    read = BinaryReader(offset, source)
    while read.offset < offset + size:
        rez += str(read.read(Types.char).decode("ascii"))
    return rez


source = (b'KHTHX\x00:i\xd3\xe3u5<\xcd2\x18\x05\x91\xe5l5\x86\xbe\xd5\x1b6\x00w'
          b'\x18\xb7\xb6H.\xcc\xda\xb6\x0f\xa0\x18\xecW\xc2\x00\x00\x00\x02\x00\x00'
          b'\x00\x1a\x89\x99\xba\xdcP\x83:\x17?K\x10\xe4\xbf\x15\\$\xbeh\x1e\x14\xbex'
          b'\xf4\x86vkaiebyv\xbf\xd2\x08\x07\xb8\xdf\xfd$\x00\x00\x00*')


reader = BinaryReader(offset=5, source=source)
g = a(reader)
print(g)
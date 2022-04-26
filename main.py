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
    a1 = b(reader)
    a2 = reader.read(Types.int32)
    a3 = reader.read(Types.uint16)
    a4 = reader.read(Types.uint64)
    a5 = reader.read(Types.uint32)
    a6 = reader.read(Types.int8)
    a7 = reader.read(Types.int8)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def b(reader: BinaryReader):
    b11 = reader.read(Types.uint16)
    b12 = reader.read(Types.uint32)
    b1 = masser_b1(b11, b12, reader.source)
    b21 = reader.read(Types.uint32)
    b22 = reader.read(Types.uint16)
    b2 = masser_b2(b21, b22, reader.source)
    b3 = reader.read(Types.int32)
    b41 = reader.read(Types.uint32)
    b4 = d(b41, reader.source)
    b5 = reader.read(Types.uint16)
    b6 = reader.read(Types.float)
    b7 = reader.read(Types.int8)
    b8 = reader.read(Types.float)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8)


def c(reader: BinaryReader):
    c1 = reader.read(Types.int8)
    c2 = reader.read(Types.int8)
    c3 = reader.read(Types.float)
    c4 = reader.read(Types.float)
    c51 = reader.read(Types.uint32)
    c52 = reader.read(Types.uint32)
    c5 = masser_c5(c51, c52, reader.source)
    c6 = reader.read(Types.int16)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6)


def d(offset, source):
    reader = BinaryReader(offset, source)
    d1 = reader.read(Types.int16)
    d2 = [reader.read(Types.float), reader.read(Types.float), reader.read(Types.float), reader.read(Types.float),
          reader.read(Types.float), reader.read(Types.float), reader.read(Types.float)]
    d3 = reader.read(Types.int8)
    return dict(D1=d1, D2=d2, D3=d3)


def masser_b1(size, offset, source):
    rez = ''
    read = BinaryReader(offset, source)
    while read.offset < offset + size:
        rez += str(read.read(Types.char).decode("ascii"))
    return rez


def masser_b2(size, offset, source):
    rez = []
    read = BinaryReader(offset, source)
    while read.offset < offset + size * 16:
        rez.append(c(read))
    return rez


def masser_c5(size, offset, source):
    rez = []
    read = BinaryReader(offset, source)
    while read.offset < offset + size * 8:
        rez.append(read.read(Types.uint64))
    return rez


source = (b'\xdeYCPT\x02\x008\x00\x00\x00\x02\x00\x00\x00b\x00\x90\xd2\xe8'
          b'\x1f\x8a\x00\x00\x00\xa0K\nS0\xbfx\x04w\xfe;i\xb6"}\xe8o\xee\xd4'
          b'-\x01\x01\x80d\x94\x98\x0cp\xb7#\x99apK:e\xe5\xfa\x02\x83\xfc\x7fZO!*\x08'
          b'\xffc\xa1\xaf/kd;\t*\x95\x02\x83~\xc3:\xbae<\\xlZd\xccR\xb8\x05\x0f\x90t?'
          b'p_\x82>\x02\x00\x00\x00:\x00\x00\x00=\x01vo\xac\xfa\xed>S\xe1\x00?'
          b'\x03\x00\x00\x00J\x00\x00\x00r\xe6\x16\xbcF\x85\xab>\x0f\xa5\xe3\xbe\n5*?'
          b'6\x0bE>\xa8\xd8K?\xfaxq\xbe\x040!?~')

reader = BinaryReader(offset=5, source=source)
g = a(reader)
print(g)

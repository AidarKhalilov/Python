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


class BinaryReader:
    def __init__(self, offset, source):
        self.offset = offset
        self.source = source

    def read(self, pattern):
        pattern = '>' + pattern.value
        result = unpack_from(pattern, self.source, self.offset)
        self.offset += calcsize(pattern)
        return result[0]


def a(reader: BinaryReader):
    offset = reader.read(Types.uint16)
    a1 = b(offset, reader.source)
    a2 = reader.read(Types.int64)
    a3 = masser_a3(5, reader)
    a4 = reader.read(Types.uint8)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4)


def b(offset, source):
    reader = BinaryReader(offset, source)
    b1 = masser_b(2, reader)
    b2 = (reader.read(Types.char) + reader.read(Types.char) +
          reader.read(Types.char) + reader.read(Types.char) +
          reader.read(Types.char) + reader.read(Types.char) +
          reader.read(Types.char) + reader.read(Types.char)). \
        decode("ascii")
    b3 = reader.read(Types.double)
    reader.offset = reader.read(Types.uint32)
    b4 = d(reader)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4)


def c(reader: BinaryReader):
    c1 = reader.read(Types.float)
    c2 = reader.read(Types.float)
    return dict(C1=c1, C2=c2)


def d(reader: BinaryReader):
    size = reader.read(Types.uint32)
    offset = reader.read(Types.uint32)
    d1 = masser_d1(size, offset, reader.source)
    d2 = reader.read(Types.uint32)
    d3 = masser_d3(2, reader.offset, reader.source)
    return dict(D1=d1, D2=d2, D3=d3)


def masser_a3(size, reader: BinaryReader):
    offset = reader.offset
    rez = []
    while reader.offset < offset + size * 2:
        rez.append(reader.read(Types.int16))
    return rez


def masser_d1(size, offset, source):
    reader = BinaryReader(offset, source)
    rez = []
    while reader.offset < offset + size * 8:
        rez.append(reader.read(Types.int64))
    return rez


def masser_d3(size, offset, source):
    reader = BinaryReader(offset, source)
    rez = []
    while reader.offset < offset + size * 2:
        rez.append(reader.read(Types.uint16))
    return rez


def masser_b(size, reader: BinaryReader):
    offset = reader.offset
    rez = []
    while reader.offset < offset + size * 8:
        rez.append(c(reader))
    return rez


def masser_c(size, offset, source):
    rez = ""
    read = BinaryReader(offset, source)
    while read.offset < offset + size:
        rez += str(read.read(Types.char).decode("ascii"))
    return rez


def main(source):
    reader = BinaryReader(offset=5, source=source)
    return a(reader)

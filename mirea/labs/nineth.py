class main:
    def __init__(self):
        self.currentPoint = 'A'

    def step(self):
        match self.currentPoint:
            case 'A':
                self.currentPoint = 'B'
                return 0
            case 'B':
                self.currentPoint = 'F'
                return 2
            case 'C':
                self.currentPoint = 'D'
                return 3
            case 'D':
                self.currentPoint = 'E'
                return 5
            case 'E':
                self.currentPoint = 'E'
                return 8
            case _:
                raise KeyError

    def put(self):
        match self.currentPoint:
            case 'B':
                self.currentPoint = 'C'
                return 1
            case 'C':
                self.currentPoint = 'E'
                return 4
            case 'D':
                self.currentPoint = 'F'
                return 6
            case 'E':
                self.currentPoint = 'F'
                return 7
            case _:
                raise KeyError
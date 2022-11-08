WHITE = 0
RED = 1
BLUE = 2
PURPLE = 3

class Rect():
    def __init__(self, r1, c1, r2, c2, color):
        self.__al = { 'x':r1, 'y':c1 }
        self.__br = { 'x':r2, 'y':c2 }
        self.__color = color

    @property
    def al(self):
        return self.__al

    @property
    def br(self):
        return self.__br

    @property
    def color(self):
        return self.__color

T = int(input())
for t in range(1, T + 1):
    matrix = [[0] * 10 for _ in range(10)]
    N = int(input())
    rects = []
    for n in range(N):
        r1, c1, r2, c2, color =map(int, input().split())
        rects.append(Rect(r1, c1, r2, c2, color))

    for rect in rects:
        for x in range(rect.al['x'], rect.br['x'] + 1):
            for y in range(rect.al['y'], rect.br['y'] + 1):
                if matrix[x][y] == WHITE:
                    matrix[x][y] = rect.color
                elif matrix[x][y] == BLUE and rect.color == RED:
                    matrix[x][y] = PURPLE
                elif matrix[x][y] == RED and rect.color == BLUE:
                    matrix[x][y] = PURPLE

    count = 0
    for x in range(10):
        for y in range(10):
            if matrix[x][y] == PURPLE:
                count += 1

    print(f'#{t} {count}')

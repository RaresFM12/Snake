import texttable
import random

N = 7

class Board:
    def __init__(self):
        self.__data = []
        for i in range(N):
            self.__data.append([' '] * N)

        self.place_initial_snake(2, 3)
        for i in range(10):
            self.place_random_apples()

        self.refactor_board()

    @property
    def board(self):
        return self.__data

    def refactor_board(self):
        for i in range(N):
            for j in range(N):
                if self.__data[i][j] == '!':
                    self.__data[i][j] = ' '

    def place_initial_snake(self, i, j):
        self.__data[i][j] = '*'
        self.__data[i + 1][j] = '+'
        self.__data[i + 2][j] = '+'

    def place_random_apples(self):
        all_pos = []
        for i in range(N):
            for j in range(N):
                if self.__data[i][j] == ' ':
                    all_pos.append([i, j])

        ok = random.choice(all_pos)
        self.__data[ok[0]][ok[1]] = 'a'
        self.place_not_adj(ok[0], ok[1])

    def place_all_adj_apples(self):
        for i in range(N):
            for j in range(N):
                if self.__data[i][j] == 'a':
                    self.place_not_adj(i, j)

    def place_not_adj(self, i, j):
        if i + 1 != N:
            if self.__data[i + 1][j] == ' ':
                self.__data[i + 1][j] = '!'

        if i - 1 != -1:
            if self.__data[i - 1][j] == ' ':
                self.__data[i - 1][j] = '!'

        if j - 1 != -1:
            if self.__data[i][j - 1] == ' ':
                self.__data[i][j - 1] = '!'

        if j + 1 != N:
            if self.__data[i][j + 1] == ' ':
                self.__data[i][j + 1] = '!'

    def __str__(self):
        t = texttable.Texttable()
        for i in range(N):
            t.add_row(self.__data[i])

        return t.draw()


class Segment:
    def __init__(self, x, y):
        self.__i = x
        self.__j = y

    @property
    def i(self):
        return self.__i

    @property
    def j(self):
        return self.__j

    @i.setter
    def i(self, v):
        self.__i = v

    @j.setter
    def j(self, v):
        self.__j = v

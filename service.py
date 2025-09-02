from domain import Board, Segment


class Service:
    def __init__(self):
        self.__board = Board()
        self.__segments = {}
        self.__last_op = ""
        self.__nr_seg = 3
        self.__over = False

        self.__segments[1] = Segment(2, 3)
        self.__segments[2] = Segment(3, 3)
        self.__segments[3] = Segment(4, 3)

    def get_board(self):
        return self.__board

    def get_last_operation(self):
        return self.__last_op

    def get_over(self):
        return self.__over

    def is_apple(self, i, j):
        if self.__board.board[i][j] == 'a':
            return True

        return False

    def new_segment(self):
        for i in range(self.__nr_seg, 1, -1):
            self.__segments[i] = self.__segments[i - 1]

    def generate_new_apple(self):
        self.__board.place_all_adj_apples()
        self.__board.place_random_apples()
        self.__board.refactor_board()

    def is_over(self, i, j):
        if self.__board.board[i][j] == '+':
            return True

        return False

    def moves_up(self):
        i = self.__segments[1].i
        j = self.__segments[1].j

        if self.__last_op == "down":
            raise ValueError("A snake going down cannot go up!")

        if i - 1 >= 0:
            if self.is_over(i - 1, j):
                self.__over = True
                return

            if self.is_apple(i - 1, j):
                self.__board.board[i - 1][j] = '*'
                self.__board.board[i][j] = '+'
                self.__nr_seg += 1
                self.new_segment()
                self.__segments[1] = Segment(i - 1, j)
                self.generate_new_apple()

            else:
                self.__board.board[i - 1][j] = '*'
                self.__board.board[i][j] = ' '
                self.make_move(1)
                self.__segments[1] = Segment(i - 1, j)
        else:
            self.__over = True
            return

        self.__last_op = "up"

    def moves_down(self):
        i = self.__segments[1].i
        j = self.__segments[1].j

        if self.__last_op == "up" or self.__last_op == "":
            raise ValueError("A snake going up cannot go down!")

        if i + 1 <= 6:
            if self.is_over(i + 1, j):
                self.__over = True
                return

            if self.is_apple(i + 1, j):
                self.__board.board[i + 1][j] = '*'
                self.__board.board[i][j] = '+'
                self.__nr_seg += 1
                self.new_segment()
                self.__segments[1] = Segment(i + 1, j)
                self.generate_new_apple()

            else:
                self.__board.board[i + 1][j] = '*'
                self.__board.board[i][j] = ' '
                self.make_move(1)
                self.__segments[1] = Segment(i + 1, j)
        else:
            self.__over = True
            return

        self.__last_op = "down"

    def moves_left(self):
        i = self.__segments[1].i
        j = self.__segments[1].j

        if self.__last_op == "right":
            raise ValueError("A snake going right cannot go left!")

        if j - 1 >= 0:
            if self.is_over(i, j - 1):
                self.__over = True
                return

            if self.is_apple(i, j - 1):
                self.__board.board[i][j - 1] = '*'
                self.__board.board[i][j] = '+'
                self.__nr_seg += 1
                self.new_segment()
                self.__segments[1] = Segment(i, j - 1)
                self.generate_new_apple()

            else:
                self.__board.board[i][j - 1] = '*'
                self.__board.board[i][j] = ' '
                self.make_move(1)
                self.__segments[1] = Segment(i, j - 1)
        else:
            self.__over = True
            return

        self.__last_op = "left"

    def moves_right(self):
        i = self.__segments[1].i
        j = self.__segments[1].j

        if self.__last_op == "left":
            raise ValueError("A snake going left cannot go right!")

        if j + 1 <= 6:
            if self.is_over(i, j + 1):
                self.__over = True
                return

            if self.is_apple(i, j + 1):
                self.__board.board[i][j + 1] = '*'
                self.__board.board[i][j] = '+'
                self.__nr_seg += 1
                self.new_segment()
                self.__segments[1] = Segment(i, j + 1)
                self.generate_new_apple()

            else:
                self.__board.board[i][j + 1] = '*'
                self.__board.board[i][j] = ' '
                self.make_move(1)
                self.__segments[1] = Segment(i, j + 1)
        else:
            self.__over = True
            return

        self.__last_op = "right"


    def make_move(self, id):
        if id == self.__nr_seg:
            return

        i = self.__segments[id].i
        j = self.__segments[id].j

        self.__board.board[i][j] = '+'

        acc_i = self.__segments[id + 1].i
        acc_j = self.__segments[id + 1].j

        self.__board.board[acc_i][acc_j] = ' '

        self.make_move(id + 1)
        self.__segments[id + 1] = self.__segments[id]


from math import sqrt


class Sudoku:
    puzzle = []

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __len__(self):
        return len(self.puzzle)

    def __str__(self):
        st = ""
        for row in self.puzzle:
            st = st + "\n"+str(row)
        return st

    def get_row(self, row):
        return self.puzzle[row]

    def get_col(self, col):
        return [x[col] for x in self.puzzle]

    def get_block(self, row, col):
        x = col/3
        y = row/3
        size = int(sqrt(len(self)))
        elms = []

        for b in range(size*y, size*y+3):
            for a in range(size*x, size*x+3):
                elms.append(self.puzzle[b][a])
        return elms

    def is_valid(self, num, row, col):

        return not (num in self.get_row(row) or num in self.get_col(col) or num in self.get_block(row, col))

    def get_valids(self, row, col):
        cands = []
        for i in range(1, len(self.puzzle)+1):
            if (self.is_valid(i, row, col)):
                cands.append(i)
        return cands

    def insert(self, val, row, col):
        self.puzzle[row][col] = val

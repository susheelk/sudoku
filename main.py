from solve import *
from sudoku import Sudoku
from time import time

puzzle = [
    ["", "", "", 2, 6, "", 7, "", 1],
    [6, 8, "", "", 7, "", "", 9, ""],
    [1, 9, "", "", "", 4, 5, "", ""],
    [8, 2, "", 1, "", "", "", 4, ""],
    ["", "", 4, 6, "", 2, 9, "", ""],
    ["", 5, "", "", "", 3, "", 2, 8],
    ["", "", 9, 3, "", "", "", 7, 4],
    ["", 4, "", "", 5, "", "", 3, 6],
    [7, "", 3, "", 1, 8, "", "", ""]
]

puzzle1 = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 3, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, ""],
    [7, 6, 3, 4, 1, 8, 2, 5, ""]
]

puzzle2 = [
    [1, 2],
    [2, ""]
]

if __name__ == "__main__":
    start = time()
    sud = Sudoku(puzzle2)
    sud = solve(sud)

    if (sud):
        print 'Solution Exists!\n'+str(sud)
        end = time()
        print '\nSolved in ' + str(end-start) + " seconds"
import copy

def find_empties(puzzle_list):
    master = []
    for y in range(len(puzzle_list)):
        for x in range(len(puzzle_list)):
            if puzzle_list[y][x] == '':
                master.append([x, y])
    return master


def fill(sudoku, to_fill):

    if (len(to_fill) == 0):
        return sudoku

    cords = to_fill[0]
    valids = sudoku.get_valids(cords[1], cords[0])



    if (len(valids) == 0):
        return False

    for cand in valids:
        # sudoku_copy = copy.deepcopy(sudoku)
        # sudoku_copy.insert(cand, cords[1], cords[0])
        sudoku.insert(cand, cords[1], cords[0])
        solved = fill(sudoku, to_fill[1:])
        if(solved):
            return solved
        sudoku.insert("", cords[1], cords[0])

def solve(sudoku):
    n = 9
    empties = find_empties(sudoku.puzzle)
    return fill(sudoku, empties)
    # print empties

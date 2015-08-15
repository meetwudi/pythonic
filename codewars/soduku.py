from collections import namedtuple
from copy import deepcopy

SIZE = 8

solved = False
answer = None

Pos = namedtuple('Pos', 'x y')


def get_count_of_zeros(puzzle):
    return sum(1 if puzzle[x][y] > 0 else 0 for x in xrange(SIZE) for y in xrange(SIZE))


def get_pos_of_next_zero(puzzle):
    for x in xrange(SIZE):
        for y in xrange(SIZE):
            if puzzle[x][y] == 0:
                return Pos(x, y)


def get_nums_valid(puzzle, pos):
    x_occ = {puzzle[pos.x][y] for y in xrange(SIZE)}
    y_occ = {puzzle[x][pos.y] for x in xrange(SIZE)}
    block_occ = {puzzle[x][y]
                 for x in xrange(pos.x*3/SIZE+1, pos.x*3/SIZE+4)
                 for y in xrange(pos.y*3/SIZE+1, pos.y*3/SIZE+4)}
    occ = x_occ.union(y_occ).union(block_occ)
    return occ.difference({i for x in xrange(SIZE+1)})


def dfs(puzzle, count_of_zeros):
    if count_of_zeros == 0:
        answer = deepcopy(puzzle)
        solved = True
    if solved:
        return

    pos = get_pos_of_next_zero(puzzle)
    nums_valid = get_nums_valid(puzzle, pos)
    for num in nums_valid:
        puzzle[pos.x][pos.y] = num
        dfs(puzzle, count_of_zeros-1)
        puzzle[pos.x][pos.y] = 0


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    count_of_zeros = get_count_of_zeros(puzzle)
    dfs(puzzle, count_of_zeros)
    return answer

import numpy as np

def read_lines(year, day, test=False):
    if test:
        with open(f'data/{year}/{day}.test', 'r') as f:
            lines = f.readlines()
    else:
        with open(f'data/{year}/{day}.txt', 'r') as f:
            lines = f.readlines()
    return [line.strip() for line in lines]

def line_as_ints(line):
    return np.array(
            list(map(int, line.split(','))), dtype=np.int)

def lines_as_ints(lines):
    return np.array(list(map(int, lines)), dtype=np.int)

def bool_to_int(array):
    return int(''.join(['1' if x else '0' for x in array]), 2)

def line_iter(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xx = x1
    yy = y1
    x_inc = 0
    y_inc = 0
    m = 0
    
    if x1 == x2:
        x_inc = 0
        if y1 > y2:
            y_inc = -1
        else:
            y_inc = 1
    elif y1 == y2:
        y_inc = 0
        if x1 > x2:
            x_inc = -1
        else:
            x_inc = 1
    else:
        m = int((y2 - y1) / (x2 - x1))
        
        if x1 > x2:
            x_inc = -1
            y_inc = -1 * m
        else:
            x_inc = 1
            y_inc = m
    
    while not (xx == x2 and yy == y2):
        yield (xx, yy)
        xx = xx + x_inc
        yy = yy + y_inc
    yield(xx, yy)

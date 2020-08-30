"""
code_war
Line Safari-Is that line?
date: Wednesday
3ku
neon
"""


# to find the position of x
def find_x(grid):
    return_list = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "X":
                return_list.append((i, j))
            else:
                continue
    return return_list


# setting the end point position
def start_from_x(start_i, start_j, grid):
    if start_i - 1 > 0 and grid[start_i - 1][start_j] == "|" or "X":
        return start_i - 1, start_j, start_i - 2, start_j
    elif start_i + 1 < len(grid) and grid[start_i + 1][start_j] == "|" or "X":
        return start_i + 1, start_j, start_i + 2, start_j
    elif start_j - 1 > 0 and grid[start_i][start_j - 1] == "-" or "X":
        return start_i, start_j - 1, start_i, start_j - 2
    elif start_j + 1 < len(grid) and grid[start_i][start_j + 1] == "-" or "X":
        return start_i, start_j + 1, start_i, start_j + 2
    else:
        return False


# line safari
def safari(start_i, start_j, end_i, end_j, grid):
    global loop
    loop = 1
    while loop == 1:
        if grid[start_i][start_j] == "-" and grid[end_i][end_j] == '-':
            start_i = end_i
            start_j = end_j
            if end_j > start_j and end_j + 1 < len(grid[0]):
                end_j += 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            elif end_j < start_j and end_j - 1 > 0:
                end_j -= 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            else:
                loop = 0
                return False
        elif grid[start_i][start_j] == "-" and grid[end_i][end_j] == '+':
            start_i = end_i
            start_j = end_j
            if grid[end_i + 1][end_j] == "|" or "+" and end_i + 1 <= len(grid):
                end_i += 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            elif grid[end_i - 1][end_j] == "|" or "+" and end_i - 1 >= 0:
                end_i -= 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            elif grid[end_i + 1][end_j] == "X" or grid[end_i - 1][end_j] == "X":
                loop = 0
                return True
            else:
                loop = 0
                return False
        elif grid[start_i][start_j] == "|" and grid[end_i][end_j] == '|':
            start_i = end_i
            start_j = end_j
            if end_i > start_i and end_i + 1 < len(grid):
                end_i += 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            elif end_i < start_i and end_i - 1 > 0:
                end_i -= 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            else:
                loop = 0
                return False
        elif grid[start_i][start_j] == "|" and grid[end_i][end_j] == '+':
            start_i = end_i
            start_j = end_j
            if grid[end_i][end_j + 1] == "-" or "+" and end_j + 1 <= len(grid[0]):
                end_j += 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            elif grid[end_i][end_j - 1] == "-" or "+" and end_j - 1 >= 0:
                end_j -= 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            elif grid[end_i][end_j + 1] == "X" or grid[end_i][end_j - 1] == "X":
                loop = 0
                return True
            else:
                loop = 0
                return False
        elif grid[start_i][start_j] == "+" and grid[end_i][end_j] == '-':
            start_i = end_i
            start_j = end_j
            if end_j > start_j and end_j + 1 < len(grid[0]):
                end_j += 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            elif end_j < start_j and end_j - 1 > 0:
                end_j -= 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            else:
                loop = 0
                return False
        elif grid[start_i][start_j] == "+" and grid[end_i][end_j] == '|':
            start_i = end_i
            start_j = end_j
            if end_i > start_i and end_i + 1 < len(grid):
                end_i += 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            elif end_i < start_i and end_i - 1 > 0:
                end_i -= 1
                if grid[end_i][end_j] == "X":
                    loop = 0
                    return True
            else:
                loop = 0
                return False
        elif grid[start_i][start_j] == "+" and grid[end_i][end_j] == '+':
            if start_i == end_i:
                start_i = end_i
                start_j = end_j
                if grid[end_i + 1][end_j] == "|" or "+" and end_i + 1 <= len(grid):
                    end_i += 1
                    if grid[end_i][end_j] == "X":
                        loop = 0
                        return True
                elif grid[end_i - 1][end_j] == "|" or "+" and end_i - 1 >= 0:
                    end_i -= 1
                    if grid[end_i][end_j] == "X":
                        loop = 0
                        return True
                elif grid[end_i + 1][end_j] == "X" or grid[end_i - 1][end_j] == "X":
                    loop = 0
                    return True
                else:
                    loop = 0
                    return False
            elif start_j == end_j:
                start_i = end_i
                start_j = end_j
                if grid[end_i][end_j + 1] == "-" or "+" and end_j + 1 <= len(grid[0]):
                    end_j += 1
                    if grid[end_i][end_j] == "X":
                        loop = 0
                        return True
                elif grid[end_i][end_j - 1] == "-" or "+" and end_j - 1 >= 0:
                    end_j -= 1
                    if grid[end_i][end_j] == "X":
                        loop = 0
                        return True
                elif grid[end_i][end_j + 1] == "X" or grid[end_i][end_j - 1] == "X":
                    loop = 0
                    return True
                else:
                    loop = 0
                    return False
        else:
            loop = 0
            return False


# main function
def line(grid):
    start_list = find_x(grid)
    start_i, start_j = start_list[0]
    start_i, start_j, end_i, end_j = start_from_x(start_i, start_j, grid)
    return safari(start_i, start_j, end_i, end_j, grid)

# end


"""
print
"""


"""
def line(grid):
    g = {(r, c): v for r, row in enumerate(grid) for c, v in enumerate(row) if v.strip()}
    ends = [k for k in g if g[k] == 'X']
    if len(ends) != 2: return False

    for start, finish in [ends, ends[::-1]]:
        path = [start]
        while path[-1] != finish:
            r, c = path[-1]
            d, V, H = g[path[-1]], [(r + 1, c), (r - 1, c)], [(r, c - 1), (r, c + 1)]
            moves = {'+': V if len(path) > 1 and path[-1][0] == path[-2][0] else H, '|': V, '-': H, 'X': H + V}[d]
            possibles = {p for p in moves if p in g and p not in path and (
                        d == '+' or (p[0] == r and g[p] != '|') or (p[1] == c and g[p] != '-'))}

            if len(possibles) != 1: break
            path.append(possibles.pop())
        if len(g) == len(path): return True
    return False
"""

def create_spiral(n):
    if type(n) != int or n < 0: return []
    x = 0
    y = 0
    dir_x = 0
    dir_y = 0
    output = [[0] * n for _ in range(n)]
    for item in range(1, (n * n) + 1):
        x += dir_x
        y += dir_y

        if x not in range(0, n) or y not in range(0, n):
            return output

        output[y][x] = item

        if (x == 0 or output[y][x - 1] != 0) and (y == 0 or output[y - 1][x] != 0):
            dir_x = 1
            dir_y = 0

        if x == n - 1 or output[y][x + 1] != 0 and (y == 0 or output[y - 1][x] != 0):
            dir_x = 0
            dir_y = 1

        if (y == n - 1 or output[y + 1][x] != 0) and (x == n - 1 or output[y][x + 1] != 0):
            dir_x = -1
            dir_y = 0

        if (x == 0 or output[y][x - 1] != 0) and (y == n - 1 or output[y + 1][x] != 0) and output[y - 1][x] == 0:
            dir_x = 0
            dir_y = -1

    return output


print(create_spiral(4))

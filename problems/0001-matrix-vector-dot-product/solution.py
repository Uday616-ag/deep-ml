def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    lst = []
    row = len(a)
    col = len(a[0])

    if col == len(b):
        for i in range(row):
            total = 0

            for j in range(col):
                total += a[i][j] * b[j]

            lst.append(total)

        return lst
    else:
        return -1
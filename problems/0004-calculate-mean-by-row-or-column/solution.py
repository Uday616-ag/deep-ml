def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    row = len(matrix)
    col = len(matrix[0])
    means = []

    if mode == 'column':
        for i in range(col):
            total = 0
            for j in range(row):
                total += matrix[j][i]

            mean = total / row
            means.append(mean)

    else:
        for i in range(row):
            total = 0
            for j in range(col):
                total += matrix[i][j]

            mean = total / col
            means.append(mean)

    return means
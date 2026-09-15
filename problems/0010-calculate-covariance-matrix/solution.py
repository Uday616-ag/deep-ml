def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    
    row = len(vectors)
    col = len(vectors[0])

    # Calculate mean of every row
    means = []

    for i in range(row):
        total = 0

        for j in range(col):
            total += vectors[i][j]

        means.append(total / col)

    # Create covariance matrix
    covariance_matrix = []

    for i in range(row):

        current_row = []

        for j in range(row):

            cov = 0

            for k in range(col):
                cov += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])

            cov = cov / (col - 1)

            current_row.append(cov)

        covariance_matrix.append(current_row)

    return covariance_matrix
def k_nearest_neighbors(points, query_point, k):
    temp_lst = []

    for i, point in enumerate(points):
        sq = (query_point[0] - point[0])**2 + (query_point[1] - point[1])**2
        root = sq**0.5
        temp_lst.append((root, i))

    temp_lst.sort(key=lambda x: x[0])

    out_lst = []

    for i in range(k):
        out_lst.append(points[temp_lst[i][1]])

    return out_lst
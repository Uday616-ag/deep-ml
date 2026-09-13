def confusion_matrix(data):

    tp = 0
    fp = 0
    fn = 0
    tn = 0

    for i in range(len(data)):
        if data[i][0] == 1 and data[i][1] == 1:
            tp += 1
        elif data[i][0] == 1 and data[i][1] == 0:
            fn += 1
        elif data[i][0] == 0 and data[i][1] == 1:
            fp += 1
        else:
            tn += 1

    return [[tp, fn],
            [fp, tn]]
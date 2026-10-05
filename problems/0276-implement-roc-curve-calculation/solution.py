import numpy as np

def compute_roc_curve(y_true: list, y_scores: list) -> tuple:
    y_true = np.array(y_true)
    y_scores = np.array(y_scores)

    thresholds = thresholds = np.sort(np.unique(y_scores))[::-1]
    thresholds=np.insert(thresholds,0,np.inf)

    tpr = []
    fpr = []

    for threshold in thresholds:
        y_pred = (y_scores >= threshold).astype(int)

        tp = np.sum((y_true == 1) & (y_pred == 1))
        tn = np.sum((y_true == 0) & (y_pred == 0))
        fn = np.sum((y_true == 1) & (y_pred == 0))
        fp = np.sum((y_true == 0) & (y_pred == 1))

        Tpr = tp / (tp + fn) if (tp + fn) != 0 else 0
        Fpr = fp / (tn + fp) if (tn + fp) != 0 else 0

        tpr.append(Tpr)
        fpr.append(Fpr)

    return np.array(fpr), np.array(tpr)
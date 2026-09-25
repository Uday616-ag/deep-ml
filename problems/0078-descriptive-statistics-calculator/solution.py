import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    data = np.array(data)

    mean = np.mean(data)
    median = np.median(data)

    value, count = np.unique(data, return_counts=True)
    mode = value[np.argmax(count)]

    variance = np.var(data)
    std = np.std(data)

    q1 = np.percentile(data, 25)
    q2 = median
    q3 = np.percentile(data, 75)

    iqr = q3 - q1

    vals = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": std,
        "25th_percentile": q1,
        "50th_percentile": q2,
        "75th_percentile": q3,
        "interquartile_range": iqr
    }

    return vals
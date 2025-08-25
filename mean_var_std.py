import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(lst).reshape(3, 3)

    mean_axis0 = np.mean(arr, axis=0).tolist()
    mean_axis1 = np.mean(arr, axis=1).tolist()
    mean_flat = float(np.mean(arr))

    var_axis0 = np.var(arr, axis=0).tolist()
    var_axis1 = np.var(arr, axis=1).tolist()
    var_flat = float(np.var(arr))

    std_axis0 = np.std(arr, axis=0).tolist()
    std_axis1 = np.std(arr, axis=1).tolist()
    std_flat = float(np.std(arr))

    max_axis0 = np.max(arr, axis=0).tolist()
    max_axis1 = np.max(arr, axis=1).tolist()
    max_flat = float(np.max(arr))

    min_axis0 = np.min(arr, axis=0).tolist()
    min_axis1 = np.min(arr, axis=1).tolist()
    min_flat = float(np.min(arr))

    sum_axis0 = np.sum(arr, axis=0).tolist()
    sum_axis1 = np.sum(arr, axis=1).tolist()
    sum_flat = float(np.sum(arr))


    calculations = {
        "mean": [mean_axis0, mean_axis1, mean_flat],
        "variance":[var_axis0, var_axis1,var_flat],
        "standard deviation": [std_axis0, std_axis1, std_flat],
        "max": [max_axis0, max_axis1, max_flat],
        "min" : [min_axis0, min_axis1, min_flat],
        "sum" : [sum_axis0, sum_axis1,sum_flat]


    }




    return calculations
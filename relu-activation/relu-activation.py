import numpy as np

def relu(x):
    arr=np.array(x)
    return np.maximum(0, arr)
import numpy as np

def sigmoid(x):
    arr=np.array(x)
    return 1/(1+np.exp(-arr))
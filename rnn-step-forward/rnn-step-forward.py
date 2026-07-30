import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    affine=np.dot(x_t,Wx)+np.dot(h_prev,Wh)+b
    return np.tanh(affine)

import numpy as np
from calculate_costFunction import compute_cost
import math, copy

def compute_gradient(x,y,w,b):
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0

    for i in range(m):
        f_wb = w*x[i] + b
        dj_dw_i = (f_wb - y[i])*x[i]
        dj_db_i = (f_wb - y[i])
        dj_dw += dj_dw_i
        dj_db += dj_db_i
    
    return dj_dw , dj_db


def gradient_descent(x, y, w_in, b_in, alpha, num_iters, compute_gradient):
    # store cost J and w's at each iteration primarily for graphing later
    j_histpry = []
    p_history = []
    b = b_in
    w = w_in

    for i in range(num_iters):
        # Calculate the gradient and update the parameters using gradient_function
        dj_dw , dj_db = compute_gradient(x, y, w , b)

        b = b - alpha * dj_db           
        w = w - alpha * dj_dw
        cost_i = compute_cost(x, y, w, b)
        if i<10000: # just to prevent resource exaustion
            j_histpry.append(cost_i)
            p_history.append([w,b])   
              

    return w, b, j_histpry, p_history

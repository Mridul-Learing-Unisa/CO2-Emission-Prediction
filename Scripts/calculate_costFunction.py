import numpy as np
from data_processing import get_data

def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost_sum = 0
    for i in range(m):
        f_wb = w*x[i] + b
        cost = (f_wb-y[i])**2
        cost_sum += cost
    total_cost = (1/2*m)*cost_sum
    return round(total_cost,2)

    
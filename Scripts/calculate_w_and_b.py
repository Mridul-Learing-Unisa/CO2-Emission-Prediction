import numpy as np
from data_processing import get_data

def get_w_b(filename):
    # Load just Fuel Consumption as X and CO2 Emissions as y
    X, y = get_data(filename)
    x = X['Fuel Consumption'].to_numpy()
    y = y.to_numpy()

    # Manually compute w (slope) and b (intercept) with Normal Equation
    w = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean())**2)
    b = y.mean() - w * x.mean()

    # Round for clean output
    w = round(w, 2)
    b = round(b, 2)

    print(f"intercept (b): {b}\nw (Fuel Consumption): {w}")
    return w, b


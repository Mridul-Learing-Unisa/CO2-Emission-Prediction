import sys
sys.path.append('./Scripts')

from Scripts.data_processing import get_data
from Scripts.calculate_costFunction import compute_cost
from Scripts.Gradient_Descent import gradient_descent, compute_gradient
import numpy as np

def predict(fuel_consumption, w, b):
    return round(w * fuel_consumption + b, 2)

# === Load & Prepare Data ===
filename = "DataSets/CO2 Emissions_Canada.csv"
X, y = get_data(filename)

x_train = X['Fuel Consumption'].to_numpy()
y_train = y.to_numpy()

# === Normalize x ===
mean_x = np.mean(x_train)
std_x = np.std(x_train)
x_norm = (x_train - mean_x) / std_x

# === Initialize parameters ===
w_init = 0
b_init = 0
iterations = 10000
tmp_alpha = 1e-4

# === Train using Gradient Descent ===
w_final, b_final, J_hist, p_hist = gradient_descent(x_norm, y_train, w_init, b_init, tmp_alpha, iterations, compute_gradient)

# === Recalculate cost using final model ===
cost = compute_cost(x_norm, y_train, w_final, b_final)

# === Make prediction for a new value (remember to normalize it!) ===
test_value = 8.5
test_value_norm = (test_value - mean_x) / std_x
prediction = predict(test_value_norm, w_final, b_final)
print(f"Aprox Predicted CO2 Emission for {test_value} L/100km: {prediction} g/km")
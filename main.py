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

print('Please Wait running Data Set')
# === Train using Gradient Descent ===
w_final, b_final, J_hist, p_hist = gradient_descent(x_norm, y_train, w_init, b_init, tmp_alpha, iterations, compute_gradient)

print()
print("Welcome to the CO₂ Emission Predictor CLI")
print("Enter fuel consumption in L/100km (type 'q' to quit)\n")

while True:
    user_input = input("Enter fuel consumption (L/100km): ")
    if user_input.lower() == 'q':
        print("Exiting the predictor. See you!")
        break
    try:
        fuel = float(user_input)
        fuel = (fuel - mean_x) / std_x
        result = predict(fuel, w_final, b_final)
        print(f"Predicted CO2 Emission: {round(result, 1)} g/km\n")
    except ValueError:
        print("Please enter a valid number (e.g., 10.5), or 'q' to quit.\n")

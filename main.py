import sys
sys.path.append('./Scripts')

from Scripts.data_processing import get_data
from Scripts.calculate_w_and_b import get_w_b
from Scripts.calculate_costFunction import compute_cost
import numpy as np

filename = "DataSets/CO2 Emissions_Canada.csv"

X, y = get_data(filename)

x_train = X['Fuel Consumption'].to_numpy()
y_train = y.to_numpy()

w, b = get_w_b(filename)

cost = compute_cost(x_train, y_train, w, b)
print(f"Squared Error Cost Function: {cost}")
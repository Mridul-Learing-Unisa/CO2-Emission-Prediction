from Scripts.data_processing import get_data

X, y = get_data("DataSets/CO2 Emissions_Canada.csv")

print(X.head())
print(y.head())
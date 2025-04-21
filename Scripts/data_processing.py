import pandas as pd

def get_data(filename):
    df = pd.read_csv(filename)

    # Remaning Columns
    df = df.rename(columns={
        'Engine Size(L)': 'Engine Size',
        'Fuel Consumption Comb (L/100 km)': 'Fuel Consumption',
        'CO2 Emissions(g/km)': 'CO2 Emissions'
    })

    # Dropping empty values
    df = df.dropna(subset=['Engine Size', 'Fuel Consumption', 'CO2 Emissions'])
    

    X = df[['Engine Size', 'Fuel Consumption']]
    y = df['CO2 Emissions']

    return X, y

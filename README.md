# 🚗 CO₂ Emission Predictor

A beginner-friendly Machine Learning linear regression Moedl that predicts CO₂ emissions (in g/km) based on a vehicle's fuel consumption (L/100km) using **univariate linear regression**. Built from scratch using Python and **gradient descent**,


## 📈 Graphs
- ### Engine Size vs CO2 Emission Data Graphs
    ![alt text](/Graph%20Screenshots/Engine%20VS%20CO2%20Emissions.png)
- ### Fuel Consumption vs CO2 Emission Data Graphs
    ![alt text](/Graph%20Screenshots/Fuel%20Consumption%20VS%20CO2%20Emissions.png)

    > 📌 *Note: Currently, only Fuel Consumption is used as a feature.*

- ### Regression Model
    ![alt text](/Graph%20Screenshots/Model.png)

- ### Gradient descent on Cost function
    ![alt text](/Graph%20Screenshots/Gradient%20Descent.png)

## 🚀 Features

- 🔢 **Model**: Linear Regression (ŷ = w·x + b)  
- 🧠 **Training**: Custom implementation of **gradient descent**  
- 📊 **Data**: CO₂ Emissions in Canada ([Kaggle Dataset](https://www.kaggle.com/datasets/debajyotipodder/co2-emission-by-vehicles))  
- 🖥️ **Interface**: CLI to enter fuel consumption and get instant predictions  
- 📈 **Feature Used**: Fuel Consumption (L/100km)


## 🚧 Development Status

This project is **still under development**:
- ✅ Fully functional with one feature (Fuel Consumption)
- 🔜 Upcoming: multivariate regression using **Engine Size**, **Vehicle Class**, and more


## 📦 Installation

```bash
git clone https://github.com/Mridul-Learning-Unisa/CO2-Emission-Prediction.git
cd CO2-Emission-Prediction
python main.py
```


## How It Works
1) Data is loaded and normalized
2) Gradient descent optimizes w and b to minimize squared error
3) The CLI takes input, normalizes it, applies the trained model
4) Output is printed with the predicted emission value

### 🧪 Sample Output
``` bash
Enter fuel consumption (L/100km): 10.5
Predicted CO2 Emission: 245.3 g/km
```

## 📚 Resources

- [Machine Learning Specialization – Stanford & DeepLearning.AI](https://www.coursera.org/specializations/machine-learning-introduction)  
- [Kaggle Dataset – CO₂ Emissions in Canada](https://www.kaggle.com/datasets/debajyotipodder/co2-emission-by-vehicles)  

## 💬 Contact Me

📧 Email: mridulchopra23@gmail.com  
💼 LinkedIn: [Mridul Chopra](https://www.linkedin.com/in/mridul-chopra23/)

## License
> Copyright (c) 2025 Mridul Chopra

# Linear Regression from Scratch

A simple implementation of Linear Regression from scratch in Python without relying on machine learning libraries like scikit-learn. This project is aimed at understanding the fundamentals of how linear regression works under the hood.

## 📚 Overview

This repository contains a minimal and educational implementation of the Linear Regression algorithm using just NumPy for numerical computations. It walks through the process of training a linear regression model with gradient descent.

## 🚀 Features

- Linear Regression implementation without ML frameworks.
- Uses gradient descent to optimize the model parameters.
- Supports data visualization (optional) using matplotlib.
- Easy to follow and modify for learning purposes.

## 🛠️ Technologies Used

- Python 3.x
- NumPy
- Matplotlib (optional, for plotting results)

## 📂 Project Structure

```
Linear_Regression_Scratch/
├── data/
│   └── (Optional CSV or generated dataset files)
├── main.py
└── README.md
```

- `LR_Scratch.py`: Script to load data, train the model, and evaluate results.
- `data/`: Put your csv file into same file with python code.

## 🧑‍💻 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/Estaed/Linear_Regression_Scratch.git
   cd Linear_Regression_Scratch
   ```

2. **Install dependencies**

   ```bash
   pip install matplotlib, pandas
   ```

3. **Run the main script**

   ```bash
   python LR_Scratch.py
   ```

## 🧠 Concepts Covered

- Hypothesis function for linear regression
- Cost function (Mean Squared Error)
- Gradient Descent optimization
- Model evaluation

## 🎨 Example Output (if plots are included)

- Data points and fitted regression line
- Cost function convergence over epochs

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

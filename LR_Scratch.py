import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("study_hours_vs_exam_scores.csv")


def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].Study
        y = points.iloc[i].Score
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))


def gradient_descent(m_now, b_now, points, learning_rate):
    m_gradient = 0
    b_gradient = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i].Study
        y = points.iloc[i].Score

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - learning_rate * m_gradient
    b = b_now - learning_rate * b_gradient

    return m, b


m = 0
b = 0
learning_rate = 0.01
epochs = 1000


for i in range(epochs):
    if i % 100 == 0:  
        print(f"Epoch {i}, Loss: {loss_function(m, b, data)}")
    m, b = gradient_descent(m, b, data, learning_rate)

print(f"Final Parameters: m = {m}, b = {b}")

# Plot results
plt.scatter(data.Study, data.Score, color="black", label="Data")
plt.plot(data.Study, m * data.Study + b, color="red", label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.show()

import numpy as np

# Sample data
X = np.array([
    [2, 8, 4],   # study, sleep, practice
    [3, 7, 5],
    [5, 6, 8],
    [6, 5, 9]
])

y = np.array([70, 80, 95, 100])

# Parameters (weights)
w = np.zeros(X.shape[1])  # [0,0,0]
b = 0

# Hyperparameters
learning_rate = 0.01
epochs = 1000

n = len(X)

for epoch in range(epochs):

    # Prediction
    y_pred = X @ w + b

    # Error
    error = y_pred - y

    # Loss (MSE)
    loss = np.mean(error ** 2)

    # Gradients
    dw = (2/n) * X.T @ error
    db = (2/n) * np.sum(error)

    # Update parameters
    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.2f}")

print("\nLearned Parameters")
print("Weights:", w)
print("Bias:", b)
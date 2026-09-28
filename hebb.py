import numpy as np

inputs = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])

outputs = np.array([1, -1, -1, -1])

weights = np.array([0, 0])
bias = 0

for i in range(len(inputs)):

    weights = weights + inputs[i] * outputs[i]
    bias = bias + outputs[i]

print("Final Weights:")
print(weights)

print("Final Bias:")
print(bias)

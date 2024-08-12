print("JERIL JOY 23MCA034 C1_P12_X_Y")
import numpy as np;
X = np.array([[1, 2],
[3, 4]])
Y = np.random.rand(*X.shape)
result = X * 2 + 2 * Y
print(result)
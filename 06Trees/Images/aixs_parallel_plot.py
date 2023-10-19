import numpy as np
from matplotlib import pyplot as plt


np.random.seed(42)
# Data points for each class
n_points = 100

# Generate synthetic feature vectors and target 
X1_class0 = np.random.normal(2, 1, n_points)
X2_class0 = np.random.normal(2, 1, n_points)
Y_class0 = np.full(n_points, 0)

X1_class1 = np.random.normal(5, 1, n_points)
X2_class1 = np.random.normal(5, 1, n_points)
Y_class1 = np.full(n_points, 1)

X1_class2 = np.random.normal(8, 1, n_points)
X2_class2 = np.random.normal(2, 1, n_points)
Y_class2 = np.full(n_points, 2)

X1_class3 = np.random.normal(2, 1, n_points)
X2_class3 = np.random.normal(8, 1, n_points)
Y_class3 = np.full(n_points, 3)

# Concatenate feature vectors and target variables for all classes
X1 = np.concatenate([X1_class0, X1_class1, X1_class2, X1_class3])
X2 = np.concatenate([X2_class0, X2_class1, X2_class2, X2_class3])
Y = np.concatenate([Y_class0, Y_class1, Y_class2, Y_class3])

# thresholds
t1, t2 = 3.5, 4.5


plt.figure(figsize=(7, 6))

# Instances plot
plt.scatter(X1_class0, X2_class0, c='blue', label='Class 1', alpha=0.6)
plt.scatter(X1_class1, X2_class1, c='red', label='Class 2', alpha=0.6)
plt.scatter(X1_class2, X2_class2, c='green', label='Class 3', alpha=0.6)
plt.scatter(X1_class3, X2_class3, c='purple', label='Class 4', alpha=0.6)

# Label the regions
plt.text(0, 10, '$\mathcal{D}_1$', fontsize=22)
plt.text(6.5, 8, '$\mathcal{D}_2$', fontsize=22)
plt.text(0, 0, '$\mathcal{D}_3$', fontsize=22)
plt.text(10, 0, '$\mathcal{D}_4$', fontsize=22)

# Decision boundaries plot
plt.axvline(x=t1, color='gray', linestyle='--', label=f'$X_1 = {t1}$')
plt.axhline(y=t2, color='orange', linestyle='--', label=f'$X_2 = {t2}$')

plt.xlabel('$\\mathbf{X}_1$')
plt.ylabel('$\\mathbf{X}_2$')
plt.legend()
plt.title('Axis-Parallel Method')
plt.show()
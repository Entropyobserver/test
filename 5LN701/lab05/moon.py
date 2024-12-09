import matplotlib.pyplot as plt
from sklearn.datasets import make_circles, make_classification, make_moons

# 生成 make_circles 数据集
X_circles, y_circles = make_circles(n_samples=200, noise=0.1, factor=0.5)
# 生成 make_classification 数据集
X_classification, y_classification = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1)
# 生成 make_moons 数据集
X_moons, y_moons = make_moons(n_samples=200, noise=0.1)

# 绘制 make_circles 数据集
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.scatter(X_circles[:, 0], X_circles[:, 1], c=y_circles, cmap='viridis')
plt.title('make_circles')

# 绘制 make_classification 数据集
plt.subplot(1, 3, 2)
plt.scatter(X_classification[:, 0], X_classification[:, 1], c=y_classification, cmap='viridis')
plt.title('make_classification')

# 绘制 make_moons 数据集
plt.subplot(1, 3, 3)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=y_moons, cmap='viridis')
plt.title('make_moons')

plt.show()

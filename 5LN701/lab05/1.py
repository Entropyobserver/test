import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles, make_classification, make_moons

def make_datasets():
    n_samples = 200
    data = list()
    data.append({'title': "2 classes",
                 'data': make_classification(n_samples=n_samples, n_classes=2,
                                             n_features=2, n_redundant=0, n_informative=2,
                                             random_state=3, n_clusters_per_class=1)})
    data.append({'title': "3 classes",
                 'data': make_classification(n_samples=n_samples, n_classes=3,
                                             n_features=2, n_redundant=0, n_informative=2,
                                             random_state=3, n_clusters_per_class=1)})
    data.append({'title': "Moons",
                 'data': make_moons(n_samples=n_samples, noise=0.1, random_state=0)})
    data.append({'title': "Circles",
                 'data': make_circles(n_samples=n_samples, noise=0.05, factor=0.5, random_state=0)})
    
    theta = np.linspace(np.pi/2, np.pi*3/2, num=n_samples//2)
    X = np.concatenate([np.zeros((n_samples//2, 2)), np.column_stack([np.cos(theta), np.sin(theta)])])
    y = np.concatenate([np.zeros(n_samples//2), np.ones(n_samples//2)])
    X += np.random.normal(scale=0.1, size=X.shape)
    data.append({'title': "Moon and blob",
                 'data': (X, y)})
    
    X = np.random.uniform(-1, 1, size=(n_samples, 2))
    y = np.asarray([1 if (X[i, 0]>0 or X[i, 1]>0) and not (X[i, 0]>0 and X[i, 1]>0) else 0 for i in range(n_samples)])
    data.append({'title': "XOR",
                 'data': (X, y)})
    return data

def plot_datasets(datasets):
    plt.figure(figsize=(15, 10))
    
    for i, dataset in enumerate(datasets, 1):
        plt.subplot(2, 3, i)
        X, y = dataset['data']
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
        plt.title(dataset['title'])
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
    
    plt.tight_layout()
    plt.show()
    plt.savefig('data_plot.png')

# 生成并可视化数据集
#datasets = make_datasets()
#plot_datasets(datasets)

#打印出数据的样子
datasets = make_datasets()
print(datasets)
for dataset in datasets:
    print(f"\n{dataset['title']} 数据集:")
    X, y = dataset['data']
    print("特征数据 (前5行):")
    print(X[:5])
    print("\n标签 (前5个):")
    print(y[:5])
    print(f"总样本数: {len(X)}")
    print("-" * 40)
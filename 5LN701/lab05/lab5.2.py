#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fredrik Wahlberg <fredrik.wahlberg@lingfil.uu.se>
"""
import numpy as np
import matplotlib.pyplot as plt

def make_datasets():
    from sklearn.datasets import make_circles, make_classification, make_moons
    
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
    y = np.asarray([1 if (X[i, 0]>0 or X[i, 1]>0) and not (X[i, 0]>0 and X[i, 1]>0) else 0 
                    for i in range(n_samples)])
    data.append({'title': "XOR",
                'data': (X, y)})
    
    return data

def plot_classification(dataset, classifier=None, ax=None):
    """Plots a dataset as a scatterplot
    
    classifier: Points as a contour plot of predictions.
    ax: Axis for plotting, creates a new axis if none is provided.
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    markers = ['o', 's', 'd']
    X, y = dataset['data']
    
    # 获取数据范围
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    
    # 如果有分类器，先画出决策边界
    if classifier is not None:
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                            np.linspace(y_min, y_max, 200))
        if hasattr(classifier, "decision_function"):
            Z = classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
        else:
            Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.3)
    
    # 画出数据点
    for j, label in enumerate(np.unique(y)):
        mask = y == label
        ax.scatter(X[mask, 0], X[mask, 1], 
                  c=[plt.cm.coolwarm(label)], 
                  marker=markers[j], 
                  s=50,
                  edgecolor='k',
                  label=f'Class {label}')
    
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title(dataset['title'])
    ax.legend()
    
    # 保持坐标轴比例一致
    ax.set_aspect('equal')
    
    if ax is None:
        plt.show()

def main():
    # 生成数据集
    datasets = make_datasets()
    
    # 创建2x3的子图布局
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()
    
    # 在每个子图中画出一个数据集
    for dataset, ax in zip(datasets, axes):
        plot_classification(dataset, ax=ax)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
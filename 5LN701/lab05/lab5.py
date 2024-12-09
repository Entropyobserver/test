#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fredrik Wahlberg <fredrik.wahlberg@lingfil.uu.se>
"""
import numpy as np
import matplotlib.pyplot as plt


#%% Create the datasets
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
    y = np.asarray([1 if (X[i, 0]>0 or X[i, 1]>0) and not (X[i, 0]>0 and X[i, 1]>0) else 0 for i in range(n_samples)])
    data.append({'title': "XOR", 
                 'data': (X, y)})
    return data


def plot_classification(dataset, classifier=None, ax=None):
    """Plots a dataset as a scatterplot
    
    classifier: Points as a contour plot of predictions.
    ax: Axis for plotting, creates a new axis if none is provided."""
    if ax is None:
        fig, axis = plt.subplots(1, 1)
    else:
        axis = ax
    markers = ['o', 's', 'd']
    X, y = dataset['data']
    for j, label in enumerate(set(y)):
            axis.scatter(X[y==label, 0], X[y==label, 1], c=y[y==label], s=50, 
                       marker=markers[j], edgecolor='k', cmap='coolwarm', 
                       vmin=y.min(), vmax=y.max())
    x_min, x_max, y_min, y_max = axis.axis('equal')
    if classifier is not None:
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, num=200), np.linspace(y_min, y_max, num=200))
        Z = classifier.predict(np.column_stack([xx.ravel(), yy.ravel()]))
        # if hasattr(classifier, "decision_function"):
        #     Z = classifier.decision_function(np.column_stack([xx.ravel(), yy.ravel()]))
        # else:
        #     Z = classifier.predict_proba(np.column_stack([xx.ravel(), yy.ravel()]))[:, 1]
        Z = Z.reshape(xx.shape)
        axis.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.8, zorder=-1)
        # TODO Fix 3 class contour
    axis.set_title(dataset['title'])
    if ax is None:
        fig.show()
"""
# Create the data
from lab5 import make_datasets
datasets = make_datasets()
# Pick one dataset
title = datasets[0]['title']
X, y = datasets[0]['data']
# Plot a dataset
from lab5 import plot_classification
plot_classification(datasets[0])

#from lab5 import make_datasets, plot_classification 
#import matplotlib.pyplot as plt 
#datasets = make_datasets() 
#plot_classification(datasets[0]) 
#plt.savefig('plot1.png')

# 打印数据结构
def print_dataset_info(data):
   for i, dataset in enumerate(data):
       print(f"\nDataset {i+1}:")
       print(f"Title: {dataset['title']}")
       X, y = dataset['data']
       print(f"X shape: {X.shape}")
       print(f"y shape: {y.shape}")
       print(f"Unique labels in y: {np.unique(y)}")
       print("First few samples:")
       print("X[:5] =")
       print(X[:5])
       print("y[:5] =")
       print(y[:5])
       print("-" * 50)

# 生成数据
datasets = make_datasets()

# 打印信息
print_dataset_info(datasets)
"""
def main():

    # 生成数据集
    datasets = make_datasets()
    
    # 创建2x3的子图布局
    #fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    #axes = axes.ravel()
    
    # 在每个子图中画出一个数据集
    #for dataset, ax in zip(datasets, axes):
    #    plot_classification(dataset, ax=ax)
    
    #plt.tight_layout()
    #plt.show()
    #plt.savefig('plots.png')

    #from sklearn.neural_network import MLPClassifier
    #model = MLPClassifier(1500)
    #for dataset in datasets:
    #    X, y = dataset['data']
    #    model.fit(X, y)
    #    print("Accuracy on the dataset '%s' was %.1f%%" %
     #     (dataset['title'], 100 * model.score(X, y)))

    from sklearn.neural_network import MLPClassifier

    # Define the iteration points
    iteration_points = [500, 1000, 1500,2000,2500,3000,3500,4000,4500, 5000,5500,6000,7500,8000,8500,9000,9500,10000]

    # Loop through each dataset
    for dataset in datasets:
        X, y = dataset['data']
        title = dataset['title']
    
        # Loop through each iteration point
        for max_iter in iteration_points:
            model = MLPClassifier(max_iter=max_iter)
            model.fit(X, y)
            accuracy = 100 * model.score(X, y)
            print(f"Accuracy on the dataset '{title}' with max_iter={max_iter} was {accuracy:.1f}%")

if __name__ == '__main__':
    main()


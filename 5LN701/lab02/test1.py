# Create the data
from lab5 import make_datasets
datasets = make_datasets()
# Pick one dataset
title = datasets[0]['title']
X, y = datasets[0][data]
# Plot a dataset
from lab5 import plot_classification
plot_classification(datasets[0])
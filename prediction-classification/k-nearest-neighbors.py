#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
K Nearest Neighbor Classification
=========================================================

The first plot displays the iris classification training data.
The second one shows the predictions given a new dataset.

If you don't see anything, try Alt+Tab or Cmd+Tab to switch to the plot window.

Close all plot windows to finish the program.

"""
print(__doc__)

import numpy as np

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap

from sklearn import neighbors
from sklearn import datasets

def plotIrisData(figure, X, y):
	plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
	plt.xlabel('Sepal length')
	plt.ylabel('Sepal width')

	plt.xlim(x_min, x_max)
	plt.ylim(y_min, y_max)
	plt.xticks(np.arange(x_min, x_max, (x_max - x_min)/10))
	plt.yticks(np.arange(y_min, y_max, (y_max - y_min)/10))

def plotDecisionBoundary(figure, X, Y, Z):
	# Create color maps
	cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
	cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

	# Put the result into a color plot
	Z = Z.reshape(xx.shape)

	plt.pcolormesh(X, Y, Z, cmap=cmap_light)

# Load the dataset.
iris = datasets.load_iris()

X = iris.data[:, :2]  # We only take the first two features.
Y = iris.target

# Calculate min and max values for the axes.
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

knn = neighbors.KNeighborsClassifier()

# Train the model.
knn.fit(X, Y) 

# Create new data points.
newData = np.array([[4, 2],[6,3],[7,3.5],[3,4],[5,2.5],[5,4],[5,2]])

# Do predictions.
prediction = knn.predict(newData)

h = .02
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict values for descision boundary.
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

# Create first figure.
figure = plt.figure()

# Plot decision boundary.
plotDecisionBoundary(figure, xx, yy, Z)

# Plot training points.
plotIrisData(figure, X, Y)

# Create second figure.
figure = plt.figure()

# Plot decision boundary.
plotDecisionBoundary(figure, xx, yy, Z)

# Plot predicted points.
plotIrisData(figure, newData, prediction)

plt.show()
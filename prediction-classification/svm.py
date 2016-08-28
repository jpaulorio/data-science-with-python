#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
SVM Classification
=========================================================

The first plot displays the iris classification training data.
The second one shows the predictionLinears given a new dataset.

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

from sklearn import svm
from sklearn import datasets

def plotIrisData(figure, X, y):
	plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
	plt.xlabel('Sepal length')
	plt.ylabel('Sepal width')

	plt.xlim(x_min, x_max)
	plt.ylim(y_min, y_max)
	plt.xticks(np.arange(x_min, x_max, (x_max - x_min)/10))
	plt.yticks(np.arange(y_min, y_max, (y_max - y_min)/10))


def plotDecisionBoundary(figure, X, Y, Z_Linear):
	# Create color maps
	cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
	cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

	# Put the result into a color plot
	Z_Linear = Z_Linear.reshape(xx.shape)

	plt.pcolormesh(X, Y, Z_Linear, cmap=cmap_light)

def plotModel(X, Y, Z, testData, testTarget, newData, prediction):
		# Create first figure.
	figure = plt.figure()

	# Plot decision boundary.
	plotDecisionBoundary(figure, X, Y, Z)

	# Plot training points.
	plotIrisData(figure, testData, testTarget)

	# Create second figure.
	figure = plt.figure()

	# Plot decision boundary.
	plotDecisionBoundary(figure, X, Y, Z)

	# Plot predicted points.
	plotIrisData(figure, newData, prediction)

# Load the dataset.
iris = datasets.load_iris()

X = iris.data[:, :2]  # We only take the first two features.
Y = iris.target

# Calculate min and max values for the axes.
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

# Train a linear model.
svcLinear = svm.SVC(kernel='linear')
svcLinear.fit(X, Y) 

# Train a polynomial model.
svcPoly = svm.SVC(kernel='poly')
svcPoly.fit(X, Y) 

# Train a RBF model.
svcRBF = svm.SVC(kernel='rbf')
svcRBF.fit(X, Y) 

# Create new data points.
newData = np.array([[4, 2],[6,3],[7,3.5],[3,4],[5,2.5],[5,4],[5,2]])

# Do predictions.
predictionLinear = svcLinear.predict(newData)
predictionPoly = svcPoly.predict(newData)
predictionRBF = svcRBF.predict(newData)

h = .02
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict values for descision boundary.
Z_Linear = svcLinear.predict(np.c_[xx.ravel(), yy.ravel()])
Z_Poly = svcPoly.predict(np.c_[xx.ravel(), yy.ravel()])
Z_RBF = svcRBF.predict(np.c_[xx.ravel(), yy.ravel()])

plotModel(xx, yy, Z_Linear, X, Y, newData, predictionLinear)

plotModel(xx, yy, Z_Poly, X, Y, newData, predictionPoly)

plotModel(xx, yy, Z_RBF, X, Y, newData, predictionRBF)

plt.show()
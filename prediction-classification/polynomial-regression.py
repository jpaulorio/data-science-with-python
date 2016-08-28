#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
Polynomial Regression Example
=========================================================
This example generates a fake dataset (black dots), in order to illustrate a two-dimensional plot of this regression technique. 

The polynomial curve (yellow) can be seen in the plot, showing how polynomial regression attempts to draw a curve 
that will best minimize the residual sum of squares between the observed responses in the dataset, 
and the responses predicted by the polynomial approximation.

We also fit a linear model (blue) in order to show the benefits of polynomial regression for non linear data.

The coefficients, the residual sum of squares and the variance score are also calculated for both models.

If you don't see anything, try Alt+Tab or Cmd+Tab to switch to the plot window.

Close all plot windows to finish the program.

"""
print(__doc__)


# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=3)

# Generate the fake dataset (input and output).
numSamples = 50
features = np.linspace(0, 10, numSamples)[:, np.newaxis]
randomNoise = (np.random.rand(numSamples)[:, np.newaxis] * 10)
targetValues = (features * features) + np.sqrt(features) + randomNoise

# Generate polynomial features.
polynomialFeatures = poly.fit_transform(features)

# Create linear regression object
linearRegression = linear_model.LinearRegression()
polynomialRegression = linear_model.LinearRegression()

# Train the model using the input datasets
linearRegression.fit(features, targetValues)
polynomialRegression.fit(polynomialFeatures, targetValues)

# Predict.
predicted = linearRegression.predict(features)
predictedPoly = polynomialRegression.predict(polynomialFeatures)

print('\nLinear regression metrics: \n')
# The coefficients
print('Coefficients: \n', linearRegression.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((predicted - targetValues) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % linearRegression.score(features, targetValues))

print('\nPolynomial regression metrics: \n')
# The coefficients
print('Coefficients: \n', polynomialRegression.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((predictedPoly - targetValues) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % polynomialRegression.score(polynomialFeatures, targetValues))


# Plot outputs
x_min, x_max = features.min(), features.max()
y_min, y_max = targetValues.min(), targetValues.max()
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.scatter(features, targetValues,  color='black')
plt.plot(features, predicted, color='blue', linewidth=2.0)
plt.plot(features, predictedPoly, color='yellow', linewidth=2.0)
plt.xlabel('X (input)')
plt.ylabel('y (output)')
plt.xticks(np.arange(x_min, x_max, (x_max - x_min)/10))
plt.yticks(np.arange(y_min, y_max, (y_max - y_min)/10))

plt.show()

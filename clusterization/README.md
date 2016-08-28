## About the Python examples

If you have faced the following error: 

**"ValueError: unknown locale: UTF-8"** 

on MacOS X, here's the quick fix, add these lines to your **~/.bash_profile**:

**export LC_ALL=en_US.UTF-8**

**export LANG=en_US.UTF-8**

## A Tutorial on Clustering Algorithms

[Source: http://home.deib.polimi.it/matteucc/Clustering/tutorial_html/](http://home.deib.polimi.it/matteucc/Clustering/tutorial_html/)


## Clustering: An Introduction

### What is Clustering?

Clustering can be considered the most important _unsupervised learning_ problem; so, as every other problem of this kind, it deals with finding a _structure_ in a collection of unlabeled data.  

A loose definition of clustering could be “the process of organizing objects into groups whose members are similar in some way”.  
A _cluster_ is therefore a collection of objects which are “similar” between them and are “dissimilar” to the objects belonging to other clusters.  
We can show this with a simple graphical example:

![Clustering](http://home.deib.polimi.it/matteucc/Clustering/tutorial_html/images/clustering.gif)

In this case we easily identify the 4 clusters into which the data can be divided; the similarity criterion is _distance_: two or more objects belong to the same cluster if they are “close” according to a given distance (in this case geometrical distance). This is called _distance-based clustering_.  

Another kind of clustering is _conceptual clustering_: two or more objects belong to the same cluster if this one defines a concept _common_ to all that objects. In other words, objects are grouped according to their fit to descriptive concepts, not according to simple similarity measures.</font>

### The Goals of Clustering

So, the goal of clustering is to determine the intrinsic grouping in a set of unlabeled data. But how to decide what constitutes a good clustering? It can be shown that there is no absolute “best” criterion which would be independent of the final aim of the clustering. Consequently, it is the user which must supply this criterion, in such a way that the result of the clustering will suit their needs.  

For instance, we could be interested in finding representatives for homogeneous groups (_data reduction_), in finding “natural clusters” and describe their unknown properties (_“natural” data types_), in finding useful and suitable groupings (_“useful” data classes_) or in finding unusual data objects (_outlier detection_).

### Possible Applications

Clustering algorithms can be applied in many fields, for instance:


*   _Marketing_: finding groups of customers with similar behavior given a large database of customer data containing their properties and past buying records;

*   _Biology_: classification of plants and animals given their features;

*   _Libraries_: book ordering;

*   _Insurance_: identifying groups of motor insurance policy holders with a high average claim cost; identifying frauds;

*   _City-planning_: identifying groups of houses according to their house type, value and geographical location;

*   _Earthquake studies_: clustering observed earthquake epicenters to identify dangerous zones;

*   _WWW_: document classification; clustering weblog data to discover groups of similar access patterns.

### Requirements
The main requirements that a clustering algorithm should satisfy are:


*   scalability;

*   dealing with different types of attributes;

*   discovering clusters with arbitrary shape;

*   minimal requirements for domain knowledge to determine input parameters;

*   ability to deal with noise and outliers;

*   insensitivity to order of input records;

*   high dimensionality;

*   interpretability and usability.


### Problems

There are a number of problems with clustering. Among them:

*   current clustering techniques do not address all the requirements adequately (and concurrently);

*   dealing with large number of dimensions and large number of data items can be problematic because of time complexity;

*   the effectiveness of the method depends on the definition of “distance” (for distance-based clustering);

*   if an _obvious_ distance measure doesn’t exist we must “define” it, which is not always easy, especially in multi-dimensional spaces;

*   the result of the clustering algorithm (that in many cases can be arbitrary itself) can be interpreted in different ways.

* * *
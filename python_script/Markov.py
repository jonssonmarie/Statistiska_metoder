#!/usr/bin/env python
# coding: utf-8


# Importing standard libraries
import numpy as np  # used for random number generator
from scipy.stats import norm  # extension of numpy for stat analysis
from scipy.stats import gamma  # extension of numpy for stat analysis
import pandas as pd  # used for data manipulation
import matplotlib.pyplot as plt  # used for quick plotting
import seaborn as sns  # used to plot distributions
import warnings  # used to ignore displot warning

warnings.filterwarnings('ignore')

# Random walk
# Define parameters for the walk
dims = 1
step_n = 100
step_set = [-1, 1]
origin = np.zeros((1, dims))

# Simulate steps in 1D
step_shape = (step_n, dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
start = path[:1]
stop = path[-1:]

# Plot the path
fig = plt.figure(figsize=(8, 4), dpi=200)
ax = fig.add_subplot(111)
ax.scatter(np.arange(step_n + 1), path, c='blue', alpha=0.25, s=0.05)
ax.plot(path, alpha=0.5, lw=0.5, ls='-', c='blue')
ax.plot(0, start, marker='+', c='red')
ax.plot(step_n, stop, c='black', marker='o')
plt.title('1D Random Walk')
plt.tight_layout(pad=0)
plt.show()
#plt.savefig(‘plots/random_walk_1d.png’,dpi=250);

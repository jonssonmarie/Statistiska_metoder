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

# Define an array for 20,000 samples per each sample size
samples_2 = np.zeros(20000)
samples_5 = np.zeros(20000)
samples_10 = np.zeros(20000)
samples_100 = np.zeros(20000)
samples_250 = np.zeros(20000)

# Defining parameters from our population distribution
mu, sigma = 15, 2

# Defining parameters from our population distribution
mu, sigma = 15, 2
# Creating for loop for sample size 2
for x in range(20000):
    sample = np.random.normal(mu, sigma, 2)
    x_bar_2 = sample.mean()
    samples_2[x] = np.sqrt(2) * (x_bar_2 - 15) / 2

# Creating for loop for sample size 5
for a in range(20000):
    sample = np.random.normal(mu, sigma, 5)
    x_bar_5 = sample.mean()
    samples_5[a] = np.sqrt(5) * (x_bar_5 - 15) / 2

# Creating for loop for sample size 10
for b in range(20000):
    sample = np.random.normal(mu, sigma, 10)
    x_bar_10 = sample.mean()
    samples_10[b] = np.sqrt(10) * (x_bar_10 - 15) / 2

# Creating for loop for sample size 100
for c in range(20000):
    sample = np.random.normal(mu, sigma, 100)
    x_bar_100 = sample.mean()
    samples_100[c] = np.sqrt(100) * (x_bar_100 - 15) / 2

# Creating for loop for sample size 250
for d in range(20000):
    sample = np.random.normal(mu, sigma, 250)
    x_bar_250 = sample.mean()
    samples_250[d] = np.sqrt(250) * (x_bar_250 - 15) / 2


# Combining arrays into a dataframe to plot
df = pd.DataFrame(np.vstack((samples_2, samples_5, samples_10,
                             samples_100, samples_250)))
df = df.T
df.columns = ['2', '5', '10', '100', '250']

# Plotting Distributions
plt.figure(figsize=(20, 10))
sns.distplot(df['2'])
# sns.distplot(df['5'])
# sns.distplot(df['10'])
sns.distplot(df['100'])
# sns.distplot(df['250'])
plt.title('Students per Classroom Distribution', fontsize=20)
plt.xlabel('Standardized Sample Mean', fontsize=20)
plt.ylabel('Density', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(df, fontsize=20)
plt.show()


# Define an array for 20,000 samples per each sample size
samples_2 = np.zeros(20000)
samples_5 = np.zeros(20000)
samples_10 = np.zeros(20000)
samples_100 = np.zeros(20000)
samples_250 = np.zeros(20000)

# Defining parameters from our population distribution
beta = 1

# Creating for loop for sample size 2
for x in range(20000):
    sample = np.random.exponential(beta, 2)
    x_bar_2 = sample.mean()
    samples_2[x] = np.sqrt(2) * (x_bar_2 - 1)

    # Creating for loop for sample size 5
for a in range(20000):
    sample = np.random.exponential(beta, 5)
    x_bar_5 = sample.mean()
    samples_5[a] = np.sqrt(5) * (x_bar_5 - 1)

# Creating for loop for sample size 10
for b in range(20000):
    sample = np.random.exponential(beta, 10)
    x_bar_10 = sample.mean()
    samples_10[b] = np.sqrt(10) * (x_bar_10 - 1)

# Creating for loop for sample size 100
for c in range(20000):
    sample = np.random.exponential(beta, 100)
    x_bar_100 = sample.mean()
    samples_100[c] = np.sqrt(100) * (x_bar_100 - 1)

# Creating for loop for sample size 250
for d in range(20000):
    sample = np.random.exponential(beta, 250)
    x_bar_250 = sample.mean()
    samples_250[d] = np.sqrt(250) * (x_bar_250 - 1)


# Combining arrays into a dataframe to plot
df = pd.DataFrame(np.vstack((samples_2, samples_5, samples_10,
                             samples_100, samples_250)))
df = df.T
df.columns = ['2', '5', '10', '100', '250']

# Plotting Distributions
plt.figure(figsize=(20, 10))
sns.distplot(df['2'])
# sns.distplot(df['5'])
# sns.distplot(df['10'])
sns.distplot(df['100'])
# sns.distplot(df['250'])
plt.title('CLT for exponential distribution', fontsize=20)
plt.xlabel('Standardized Sample Mean', fontsize=20)
plt.ylabel('Density', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(df, fontsize=20)
plt.show()

# Define an array for 20,000 samples per each sample size
samples_2 = np.zeros(20000)
samples_5 = np.zeros(20000)
samples_10 = np.zeros(20000)
samples_100 = np.zeros(20000)
samples_250 = np.zeros(20000)


# Defining parameters from our population distribution
lo, hi = 0, 2

# Creating for loop for sample size 2
for x in range(20000):
    sample = np.random.uniform(lo, hi, 2)
    x_bar_2 = sample.mean()
    samples_2[x] = np.sqrt(2 * 3) * (x_bar_2 - 1)

    # Creating for loop for sample size 5
for a in range(20000):
    sample = np.random.uniform(lo, hi, 5)
    x_bar_5 = sample.mean()
    samples_5[a] = np.sqrt(5 * 3) * (x_bar_5 - 1)

# Creating for loop for sample size 10
for b in range(20000):
    sample = np.random.uniform(lo, hi, 10)
    x_bar_10 = sample.mean()
    samples_10[b] = np.sqrt(10 * 3) * (x_bar_10 - 1)

# Creating for loop for sample size 100
for c in range(20000):
    sample = np.random.uniform(lo, hi, 100)
    x_bar_100 = sample.mean()
    samples_100[c] = np.sqrt(100 * 3) * (x_bar_100 - 1)

# Creating for loop for sample size 250
for d in range(20000):
    sample = np.random.uniform(lo, hi, 250)
    x_bar_250 = sample.mean()
    samples_250[d] = np.sqrt(250 * 3) * (x_bar_250 - 1)

# Combining arrays into a dataframe to plot
df = pd.DataFrame(np.vstack((samples_2, samples_5, samples_10,
                             samples_100, samples_250)))
df = df.T
df.columns = ['2', '5', '10', '100', '250']

# Plotting Distributions
plt.figure(figsize=(20, 10))
sns.distplot(df['2'])
# sns.distplot(df['5'])
# sns.distplot(df['10'])
# sns.distplot(df['100'])
# sns.distplot(df['250'])
plt.title('CLT for uniform distribution', fontsize=20)
plt.xlabel('Standardized Sample Mean', fontsize=20)
plt.ylabel('Density', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(df, fontsize=20)
plt.show()

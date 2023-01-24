#!/usr/bin/env python
# coding: utf-8

# Kapitel 10 Chitvå-test

# importera paket
import numpy as np
import scipy.stats as scs

# Läskpreferenser
print(scs.chisquare([34, 45, 42, 19]))

# Poissonexemplet
print(scs.chisquare([10, 11, 14, 15, 5], f_exp=[12.37, 12.97, 12.26, 8.70, 8.69], ddof=1))

# Normalfördelningsexemplet
print(scs.chisquare([6, 6, 8, 9, 6, 5], f_exp=[6.348, 6.852, 6.800, 6.800, 6.852, 6.348], ddof=2))

# p-värdet i gymexemplet
print(1 - scs.chi2.cdf(14.945, df=2))

# Gymexemplet med scipy.stats
obs = np.array([[24, 72, 44], [84, 88, 88]])

testfun, p, dof, forvantat = scs.chi2_contingency(obs)

print(testfun, p)

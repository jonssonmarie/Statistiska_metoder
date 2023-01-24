#!/usr/bin/env python
# coding: utf-8

# Kapitel 11 Icke-parametriska Hypotestest

# importera paket
import scipy.stats as scs

# Wilcoxons teckenrangtest
scs.wilcoxon([12.56, -38.32, 36.29, 16.96, 1.71, 16.89, 32.16, 13.47, 3.17, 5.99]
             , [0.09, -35.97, 19.58, 14.28, 1.00, 15.00, 32.85, 13.05, -1.03, 16.75])

#Mann-Whitney, utbildningsbetyg, män vs. kvinnor
print(scs.mannwhitneyu([9, 7, 6, 7, 5, 5, 7, 8, 7, 4, 5], [4, 4, 6, 5, 8, 7, 4, 5, 6, 5, 3, 4, 5]))

# Kruskal-Wallis, butiks-layouter
print(scs.kruskal([1246, 1148, 1300, 1404, 1396, 1450]
            , [1267, 1228, 1450, 1351, 1280]
            , [1581, 1649, 981, 1877, 1629, 1800, 1423]
            , [1623, 1550, 1936, 1800, 1750]))

# p-värdet i exemplet om populationsvarians på ppt
print(1 - scs.chi2.cdf(10.5, df=9))

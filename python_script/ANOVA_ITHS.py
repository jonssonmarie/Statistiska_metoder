#!/usr/bin/env python
# coding: utf-8


# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import f
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd  # För Tukeys metod behöver vi ett paket från statsmodels

tillamook = [0.0571, 0.0813, 0.0831, 0.0976, 0.0817, 0.0859, 0.0735,
             0.0659, 0.0923, 0.0836]

newport = [0.0873, 0.0662, 0.0672, 0.0819, 0.0749, 0.0649, 0.0835,
           0.0725]

petersburg = [0.0974, 0.1352, 0.0817, 0.1016, 0.0968, 0.1064, 0.105]

tot_mean = (len(tillamook) * np.mean(tillamook) + len(newport) * np.mean(newport) + len(petersburg) * np.mean(
    petersburg)) / \
           (len(tillamook) + len(newport) + len(petersburg))

SSW = (len(tillamook) - 1) * np.var(tillamook, ddof=1) + (len(newport) - 1) * np.var(newport, ddof=1) + (
        len(petersburg) - 1) * np.var(petersburg, ddof=1)

SSB = len(tillamook) * (np.mean(tillamook) - tot_mean) ** 2 + len(newport) * (np.mean(newport) - tot_mean) ** 2 + len(
    petersburg) * (np.mean(petersburg) - tot_mean) ** 2

N = len(tillamook) + len(newport) + len(petersburg)
print(N)

MSW = SSW / 22
MSB = SSB / 2

F = MSB / MSW
print(F)

p = 1 - f.cdf(F, 2, 22)
print(p)

print(scs.f_oneway(tillamook, newport, petersburg))

# p-värde i butikslayoutexemplet

print(1 - scs.f.cdf(8.1199, 2, 27))

# Butikslayout med scipy stats
# Customers, Major, Gig = None, None, None
Store_Layout, Interaction, Blockdata = None, None, None
with pd.ExcelFile(r"/Users/mariejonsson/GitHub/Statistiska_metoder_Marie_Jonsson/data/Kap9.xlsx") as reader:
    Store_Layout = pd.read_excel(reader, sheet_name='Store_Layout')
    Interaction = pd.read_excel(reader, sheet_name='Interaction')
    Blockdata = pd.read_excel(reader, sheet_name='Blockdata')

print(Store_Layout.head())

print(Store_Layout.describe())

print(scs.f_oneway(Store_Layout['Layout 1'], Store_Layout['Layout 2'], Store_Layout['Layout 3']))

# Store_Layout till långformat
df = Store_Layout.stack().reset_index(name='Score')
print(df)

tukey = pairwise_tukeyhsd(endog=df['Score'],
                          groups=df['level_1'],
                          alpha=0.05)

# display results
print(tukey)

# Lön vs. yrkesgrupp och utbildning
print(Interaction.head())

# perform two-way ANOVA
model = ols('Lön ~ C(Utbildningsnivå) + C(Yrkesgrupp) + C(Utbildningsnivå):C(Yrkesgrupp)', data=Interaction).fit()
sm.stats.anova_lm(model, typ=2)

# Blockdata
# perform two-way ANOVA
model = ols('Lön ~ C(Yrkesgrupp) + C(Utbildningsnivå)', data=Blockdata).fit()
sm.stats.anova_lm(model, typ=2)

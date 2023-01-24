#!/usr/bin/env python
# coding: utf-8

# Kapitel 8 Hypotestest för två populationer

# importera paket och exempeldata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import t
from scipy.stats import norm
from statsmodels.stats import proportion

Gold_Oil, Food_Calories = None, None
with pd.ExcelFile(r"/Users/mariejonsson/GitHub/Statistiska_metoder_Marie_Jonsson/data/Kap8.xlsx") as reader:
    Gold_Oil = pd.read_excel(reader, sheet_name='Gold_Oil')
    Drink_Calories = pd.read_excel(reader, sheet_name='Drink_Calories')
#        Gig=pd.read_excel(reader, sheet_name='Gig')


# with pd.ExcelFile(r"/Users/mariejonsson/GitHub/Statistiska_metoder_Marie_Jonsson/data/Kap1.xlsx") as reader:
#        Customers=pd.read_excel(reader, sheet_name='Customers')
#        Major=pd.read_excel(reader, sheet_name='Major')
#        Gig=pd.read_excel(reader, sheet_name='Gig')

# p-värdet i exemplet med fonderna
print(1 - scs.f.cdf(1.7522, 35, 35))

# Guld och olja
print(scs.ttest_ind(Gold_Oil['Gold'], Gold_Oil['Oil'], equal_var=False))


print(scs.ttest_ind(Gold_Oil['Gold'], Gold_Oil['Oil'], equal_var=True))

# p-värdet i dryckesexemplet från kafékedjan
print(1 - scs.t.cdf(1.629, 39))

# Data från kafékedjan med scipy stats
print(Drink_Calories.head())



print(scs.ttest_rel(Drink_Calories['Before'], Drink_Calories['After']))

# Hmmmm? Tvåsidigt "by default" så dela p-värdet med två
result = scs.ttest_rel(Drink_Calories['Before'], Drink_Calories['After'])
print(result.statistic, result.pvalue / 2)


x = np.arange(0, 10, .01)
plt.plot(x, scs.f.pdf(x, dfn=3, dfd=3), color='r', lw=2)
plt.plot(x, scs.f.pdf(x, dfn=5, dfd=5), color='b', lw=2)
plt.plot(x, scs.f.pdf(x, dfn=10, dfd=10), color='y', lw=2)
plt.title('Täthetsfunktioner för F-fördelningar')
plt.legend(['df=3', 'df=5', 'df=10'])
plt.show()

# p-värdet i exemplet om populationsvarians på ppt

print(1 - scs.chi2.cdf(10.5, df=9))

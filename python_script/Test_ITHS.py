#!/usr/bin/env python
# coding: utf-8

# Kapitel 7 Hypotestest

# importera paket och exempeldata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import t
from scipy.stats import norm
from statsmodels.stats import proportion

Customers, Major, Gig = None, None, None
with pd.ExcelFile(r"/Users/mariejonsson/GitHub/Statistiska_metoder_Marie_Jonsson/data/Kap1.xlsx") as reader:
    Customers = pd.read_excel(reader, sheet_name='Customers')
    Major = pd.read_excel(reader, sheet_name='Major')
    Gig = pd.read_excel(reader, sheet_name='Gig')

print(Gig.head())

# Testa på 5% signifkansnivå om medellönen bland "Construction-arbetare" som också är "Sales Rep" är skild från 40 dollar
# Eftersom $\sigma$ är okänd ska vi använda t-test: $\frac{{\bar x}-\mu_0}{\frac{s}{\sqrt{n}}}$

till_test = Gig[Gig['Industry'].isin(['Construction']) & Gig['Job'].isin(['Sales Rep'])][['Wage']]

#Med tidigare kända funktioner
test_fun = (np.mean(till_test['Wage']) - 40) / (np.std(till_test['Wage'], ddof=1) / np.sqrt(len(till_test['Wage'])))

print(test_fun)

p_värde = 2 * scs.t.cdf(test_fun, len(till_test['Wage']) - 1)

print(p_värde)

# Med test från Scipy.Stats

result = scs.ttest_1samp(till_test['Wage'], 40)
print(result.statistic, result.pvalue)

# Test om andelen "Construction-arbetare" är mindre än 70%

Gig['Construction indicator'] = (Gig['Industry'].isin(['Construction']))

# Med kända funktioner
p_bar = np.sum(Gig['Construction indicator']) / len(Gig['Construction indicator'])
n = len(Gig['Construction indicator'])

test_fun = (p_bar - 0.7) / np.sqrt(0.7 * 0.3 / n)
print(p_bar, test_fun, n)


p_val = norm.cdf(test_fun)
print(p_val)

# Med Statsmodels
proportion.proportions_ztest(np.sum(Gig['Construction indicator']), len(Gig['Construction indicator']), value=0.70,
                             prop_var=0.70)

# p-värdet i dekan-exemplet på ppt
print(2 * (1 - scs.t.cdf(1.9444, df=34)))

# Täthetsfunktioner för chi-2-fördelningar
x = np.arange(0, 30, .05)
plt.plot(x, scs.chi2.pdf(x, df=3), color='r', lw=2)
plt.plot(x, scs.chi2.pdf(x, df=5), color='b', lw=2)
plt.plot(x, scs.chi2.pdf(x, df=10), color='y', lw=2)
plt.title('Täthetsfunktioner för chi-2-fördelningar')
plt.legend(['df=3', 'df=5', 'df=10'])
plt.show()

# p-värdet i exemplet om populationsvarians på ppt
print(1 - scs.chi2.cdf(10.5, df=9))

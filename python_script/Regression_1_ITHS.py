# Kapitel 12 Introduktion till Regression och korrelation

# importera paket och exempeldata
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import t
from scipy.stats import norm
from statsmodels.stats import proportion
import statsmodels.api as sm
from statsmodels.formula.api import ols

Debt_Payments = None

target_path = '../data'

with pd.ExcelFile(os.path.join(target_path, "Kap12.xlsx")) as reader:
    Debt_Payments = pd.read_excel(reader, sheet_name='Debt_Payments')

print(Debt_Payments.head())

# Scatter plot av Debt vs. Income
plt.scatter(Debt_Payments['Income'], Debt_Payments['Debt'])
plt.show()

# Gör regression med statsmodels
model = ols('Debt ~ Income', data=Debt_Payments).fit()
print(model.summary())

# Notes: Standard Errors assume that the covariance matrix of the errors is correctly specified.
# Korrelation med Pandas
print(Debt_Payments[['Income', 'Debt']].corr())

# Korrelation med scipy.stats
r, p = scs.pearsonr(Debt_Payments['Income'], Debt_Payments['Debt'])
print(r)

# In sample-prediktion
ypred = model.predict(Debt_Payments['Income'])
print(ypred)

fig, ax = plt.subplots()
ax.plot(Debt_Payments['Income'], Debt_Payments['Debt'], "o", label="Data")
ax.plot(Debt_Payments['Income'], ypred, "r", label="OLS prediction")
ax.legend(loc="best")
plt.show()

# Out of sample-prediktion
Income_new = pd.DataFrame([92, 103, 202], columns=['Income'])
ypred = model.predict(Income_new)
print(ypred)

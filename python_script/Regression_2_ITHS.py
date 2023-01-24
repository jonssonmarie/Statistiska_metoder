# Kapitel 13 Mer om Regressionsanalys

# importera paket och exempeldata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import t
from scipy.stats import norm
from statsmodels.stats import proportion
import statsmodels.api as sm
from statsmodels.formula.api import ols

debt_Ppyments = None
reader = "/Users/mariejonsson/GitHub/Statistiska_metoder_Marie_Jonsson/data/Kap12.xlsx"
debt_payments = pd.read_excel(reader, sheet_name='Debt_Payments')

print(debt_payments.head())

# Korrelationstest med scipy.stats

r, p = scs.pearsonr(debt_payments['Income'], debt_payments['Debt'])
print(p)

# Konfidensintervall och hypotestest för koefficienterna i regressionsmodellen

model = ols('Debt ~ Income', data=debt_payments).fit()
print(model.summary())

ypred = model.predict(debt_payments['Income'])
print(ypred)

# Prediktionsintervall in sample-prediktion
predictions = model.get_prediction(debt_payments['Income'])
frame = predictions.summary_frame(alpha=0.05)
print(frame[['obs_ci_lower', 'obs_ci_upper']])

fig, ax = plt.subplots()
ax.plot(debt_payments['Income'], debt_payments['Debt'], "o", label="Data")
ax.plot(debt_payments['Income'], ypred, "r", label="OLS prediction")
ax.plot(debt_payments['Income'], frame['obs_ci_lower'], "r--", label="lower pred lim")
ax.plot(debt_payments['Income'], frame['obs_ci_upper'], "r--", label="upper pred lim")
ax.legend(loc="best")
plt.show()

# Prediktionsintervall out of sample-prediktion
Income_new = pd.DataFrame([92, 103, 202], columns=['Income'])
predictions = model.get_prediction(Income_new)
frame = predictions.summary_frame(alpha=0.05)
print(frame[['obs_ci_lower', 'obs_ci_upper']])

# Multipelregression
model = ols('Debt ~ Income+Unemployment', data=debt_payments).fit()
print(model.summary())

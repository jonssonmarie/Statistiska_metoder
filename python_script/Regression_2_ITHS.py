# Kapitel 13 Mer om Regressionsanalys

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

# Korrelationstest med scipy.stats
r, p = scs.pearsonr(Debt_Payments['Income'], Debt_Payments['Debt'])
print(p)

# Konfidensintervall och hypotestest för koefficienterna i regressionsmodellen
model = ols('Debt ~ Income', data=Debt_Payments).fit()
print(model.summary())

ypred = model.predict(Debt_Payments['Income'])
print(ypred)

# Prediktionsintervall in sample-prediktion
predictions = model.get_prediction(Debt_Payments['Income'])
frame = predictions.summary_frame(alpha=0.05)
print(frame[['obs_ci_lower', 'obs_ci_upper']])

fig, ax = plt.subplots()
ax.plot(Debt_Payments['Income'], Debt_Payments['Debt'], "o", label="Data")
ax.plot(Debt_Payments['Income'], ypred, "r", label="OLS prediction")
ax.plot(Debt_Payments['Income'], frame['obs_ci_lower'], "r--", label="lower pred lim")
ax.plot(Debt_Payments['Income'], frame['obs_ci_upper'], "r--", label="upper pred lim")
ax.legend(loc="best")
plt.show()

# Prediktionsintervall out of sample-prediktion
Income_new = pd.DataFrame([92, 103, 202], columns=['Income'])
predictions = model.get_prediction(Income_new)
frame = predictions.summary_frame(alpha=0.05)
print(frame[['obs_ci_lower', 'obs_ci_upper']])

# Multipelregression
model = ols('Debt ~ Income+Unemployment', data=Debt_Payments).fit()
print(model.summary())

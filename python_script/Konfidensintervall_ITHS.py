# Kapitel 6 Konfidensintervall

# importera paket och exempeldata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import t
from scipy.stats import norm
from statsmodels.stats import proportion
import os

Customers, Major, Gig = None, None, None

target_path = '../data'

with pd.ExcelFile(os.path.join(target_path, "Kap1.xlsx")) as reader:
    Customers = pd.read_excel(reader, sheet_name='Customers')
    Major = pd.read_excel(reader, sheet_name='Major')
    Gig = pd.read_excel(reader, sheet_name='Gig')

print(Gig.head())

"""
Konstruera ett 95% KI för medellönen bland "Construction-arbetare" som också är "Sales Rep"
Eftersom 

 är okänd ska vi använda 

"""

till_ki = Gig[Gig['Industry'].isin(['Construction']) & Gig['Job'].isin(['Sales Rep'])][['Wage']]
# Med tidigare kända funktioner
undre_gräns = np.mean(till_ki['Wage']) - t.ppf(0.975, len(till_ki['Wage']) - 1) * np.std(till_ki['Wage'],
                                                                                         ddof=1) / np.sqrt(
    len(till_ki['Wage']))

övre_gräns = np.mean(till_ki['Wage']) + t.ppf(0.975, len(till_ki['Wage']) - 1) * np.std(till_ki['Wage'],
                                                                                        ddof=1) / np.sqrt(
    len(till_ki['Wage']))
print(undre_gräns, övre_gräns)

# Med KI-funktion från Scipy.Stats
print(t.interval(alpha=0.95, df=len(till_ki['Wage']) - 1, loc=np.mean(till_ki['Wage']), scale=scs.sem(till_ki['Wage'])))

# Konstruera ett 95% KI för andelen "Construction-arbetare"
Gig['Construction indicator'] = (Gig['Industry'].isin(['Construction']))
print(Gig.head())

# Med kända funktioner
p_bar = np.sum(Gig['Construction indicator']) / len(Gig['Construction indicator'])

n = len(Gig['Construction indicator'])

print(p_bar)

undre_gräns = p_bar - norm.ppf(0.975) * np.sqrt(p_bar * (1 - p_bar) / n)

övre_gräns = p_bar + norm.ppf(0.975) * np.sqrt(p_bar * (1 - p_bar) / n)

print(undre_gräns, övre_gräns)

# Med Statsmodels
print(
    proportion.proportion_confint(np.sum(Gig['Construction indicator']), len(Gig['Construction indicator']), alpha=0.05,
                                  method='normal'))

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import scipy as scs 
from scipy.stats import f

customers, major, gig = None, None, None
with pd.ExcelFile("Kap1 (1).xlsx") as reader:
    customers = pd.read_excel(reader, sheet_name='Customers')
    major = pd.read_excel(reader, sheet_name= 'Major')
    gig = pd.read_excel(reader, sheet_name='Gig')


print(customers.head(5))
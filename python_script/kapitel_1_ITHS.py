import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as scs
from scipy.stats import skew as skew
import seaborn as sns

Customers, Major, Gig = None, None, None
with pd.ExcelFile(r"/Users/mariejonsson/GitHub/Statistiska_metoder_Marie_Jonsson/data/Kap1.xlsx") as reader:
    Customers = pd.read_excel(reader, sheet_name='Customers')
    Major = pd.read_excel(reader, sheet_name='Major')
    Gig = pd.read_excel(reader, sheet_name='Gig')


def info_file(customers, major, gig):
    """print(customers.head(5))
    print(major.head())
    print(gig.head())"""
    print("Typvärde: ", major.mode().head(1))
    print("\n value counts", major["Major"].value_counts())
    print("\n Median Wage", gig['Wage'].median())
    print("\n Medelvärde Wage", gig['Wage'].mean())
    print("\n Medelvärde Wage numpy ", np.mean(gig["Wage"]))
    print("\n stickprovsstandardavvikelsen", gig["Wage"].std())
    print("\n stickprovsstandardavvikelsen numpy", np.std(gig["Wage"], ddof=1))  # ddof behövs för att få 1/n-1
    # medelabsolutavvikelsen
    print("medelabsolutavvikelsen", pd.DataFrame([8, 3, 7, 9]).mad())
    print(gig["Wage"].describe())


info_file(Customers, Major, Gig)

# Lägesmått eller mått på centraltendens
# Typvärdet för en datamängd är det vanligast förekommande värdet i datamängden
# Exempel: Vad är typvärdet för datamängden {Röd, Röd, Gul, Grön}?
# Vad är typvärdet av utbildningar i datamängden 'Major'?
print(Major['Major'].mode())
print(Major['Major'].value_counts())

# Medianen för en datamängd är det värde som hamnar "i mitten" om värdena ordnas efter storlek
# Exempel: Vad är medianen för datamängden {8, 3, 6, 7, 9}?
# Lösning: I storleksordning: 3,6,7,8,9 så medianen är 7
# Exempel: Vad är medianen för datamängden {8, 3, 7, 9}?
# Lösning: I storleksordning: 3,7,8,9 så medianen är medelvärdet av 7 och 8, alltså 7.5
# Vad är medianen av timlön (Wage) i datamängden 'Gig'?

# Direkt på "framen" med Pandas:
print(Gig['Wage'].median())

# med numpy
print(np.median(Gig['Wage']))

# direkt på "framen"
print(Gig['Wage'].mean())

# med numpy
print(np.mean(Gig['Wage']))

# via pandas
print(Gig['Wage'].var())

# via numpy
print(np.var(Gig['Wage'], ddof=1))

# Reflektion: Vad gör "ddof"?

# med pandas
print(Gig['Wage'].std())

# med numpy
print(np.std(Gig['Wage'], ddof=1))

# Medelabsolutavvikelsen för en datamängd ges av
# med pandas
print(pd.DataFrame([8, 3, 7, 9]).mad())

sns.set_theme()
bins = np.linspace(24, 52, 7)
plt.rcParams["figure.figsize"] = (15, 10)
plt.hist(Gig["Wage"], bins, density=False, histtype='bar', facecolor='b', alpha=0.5)

plt.title("fördelning för timlöner", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlabel("timlön i dollar", fontsize=16)
plt.xticks(fontsize=16, ha='left')
plt.yticks(fontsize=10, rotation=90, ha='left')
plt.show()

print("skevhetsmåttet ", Gig["Wage"].skew())
print(skew(Gig["Wage"], bias=False))  # bias =  False då ingen systematisk snedvridning

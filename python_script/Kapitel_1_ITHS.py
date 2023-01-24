# Kapitel 1
# importera paket och exempeldata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import f
import os
import seaborn as sns

Customers, Major, Gig = None, None, None

target_path = '../data'

with pd.ExcelFile(os.path.join(target_path, "Kap1.xlsx")) as reader:
    Customers = pd.read_excel(reader, sheet_name='Customers')
    Major = pd.read_excel(reader, sheet_name='Major')
    Gig = pd.read_excel(reader, sheet_name='Gig')

print(Major.head())

print(Gig.head())
"""
Lägesmått eller mått på centraltendens
Typvärdet för en datamängd är det vanligast förekommande värdet i datamängden
Exempel: Vad är typvärdet för datamängden {Röd, Röd, Gul, Grön}?
Vad är typvärdet av utbildningar i datamängden 'Major'?"""

print(Major['Major'].mode())

print(Major['Major'].value_counts())

"""Medianen för en datamängd är det värde som hamnar "i mitten" om värdena ordnas efter storlek
Exempel: Vad är medianen för datamängden {8, 3, 6, 7, 9}?
Lösning: I storleksordning: 3,6,7,8,9 så medianen är 7
Exempel: Vad är medianen för datamängden {8, 3, 7, 9}?
Lösning: I storleksordning: 3,7,8,9 så medianen är medelvärdet av 7 och 8, alltså 7.5
Vad är medianen av timlön (Wage) i datamängden 'Gig'?"""

# Direkt på "framen" med Pandas
print(Gig['Wage'].median())

# Med numpy:
print(np.median(Gig['Wage']))

"""Medelvärdet för en datamängd är "snittet", alltså summan av alla värden dividerat med hur många värden som finns i datamängde
 Exempel: Vad är medelvärdet för datamängden {8, 3, 6, 7, 9}?
Lösning: 

Vad är medelvärdet av timlön (Wage) i datamängden 'Gig'?"""
# Direkt på \"framen\" med Pandas:
print(Gig['Wage'].mean())

# Med numpy:
print(np.mean(Gig['Wage']))

"""
Reflektion: Kan man räkna typvärden, medianer och medelvärden för alla datatyper?
Spridningsmått
Variansen för ett stickprov ges av
 
Exempel: Vad är variansen för stickprovet 8, 3, 7, 9 ?
Lösning: Medelvärdet är 6.75 så vi får att variansen är:
 
Reflektion: Vilken enhet får variansen om enheten på data är kronor?
Vad är stickprovsvariansen av timlön (Wage) i datamängden 'Gig'?"""
# Direkt på "framen" med Pandas:
print(Gig['Wage'].var())

# Med numpy:
print(np.var(Gig['Wage'], ddof=1))

"""
Reflektion: Vad gör "ddof"?
Standardavvikelsen är roten ur variansen:
Vad är stickprovsstandardavvikelsen av timlön (Wage) i datamängden 'Gig'?"""

# Direkt på "framen" med Pandas:
print(Gig['Wage'].std())

# Med numpy:
print(np.std(Gig['Wage'], ddof=1))

"""
Medelabsolutavvikelsen för en datamängd ges av
 
Exempel: Vad är MAD för datamängden {8, 3, 7, 9}?
Lösning: Medelvärdet är 6.75 så vi får att MAD är:"""

# Med Pandas:
print(pd.DataFrame([8, 3, 7, 9]).mad())

"""En bra funktion i Pandas
Kan man få fram mer än ett deskriptivt mått från en "frame", t ex för "Wage" i "Gig"?
"""
print(Gig['Wage'].describe())

"""
Reflektion: "50%" är medianen
Medelvärde, median och skevhet"""

sns.set_theme()
bins = np.linspace(24, 52, 7)

plt.rcParams["figure.figsize"] = (15, 10)
plt.hist(Gig['Wage'], bins,
         density=False,
         histtype='bar',
         facecolor='b',
         alpha=0.5)

plt.title("Fördelning för timlöner", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlabel('Timlön i dollar', fontsize=16)
plt.ylabel('Antal löntagare', fontsize=16)
plt.xticks(fontsize=16, ha="left")
plt.yticks(fontsize=16)
plt.show()

"""Fördelningen är skev åt vänster, alltså vänstersvanden är tyngra än högersvansner, eller medelvärdet är mindre än medianen
Man kan mäta skevheten med
 
Talet blir negativt om fördelningen är skev åt vänster och positivt om fördelningen är skev åt höger"""

# Med Pandas
print(Gig['Wage'].skew())

# Med Scipy Stats
print(scs.skew(Gig['Wage']))

# Hmmmm???
print(scs.skew(Gig['Wage'], bias=False))

"""Klasser och stapeldiagram
Vi kanske vill göra ett stapeldiagram av 'Job' i 'Gig'. Hur kan man göra det i Python?"""
print(Gig.head())

Gig['Job'].value_counts().plot(kind='bar', x='Job')
plt.title("Fördelning mellan jobb", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlabel('Jobb', fontsize=16)
plt.ylabel('Antal arbetande', fontsize=16)
# plt.xticks(fontsize=16,ha="left")
plt.xticks(fontsize=16, rotation=-45, ha="left")
plt.yticks(fontsize=16)
plt.show()

"""Om man vill gruppera på industrisektorer då? En lösning är att göra en korstabell mha Pandas och sedan plotta den"""
# pd.crosstab(Gig['Industry'],Gig['Job']).plot(kind='bar',stacked=True)

pd.crosstab(Gig['Industry'], Gig['Job']).plot(kind='bar', stacked=False)

plt.title("Fördelning mellan jobb", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlabel('Industry', fontsize=16)
plt.ylabel('Antal arbetande', fontsize=16)
# plt.xticks(fontsize=16,ha="left")
plt.xticks(fontsize=16, rotation=-45, ha="left")
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.show()

print(pd.crosstab(Gig['Industry'], Gig['Job']))

"""
Deskriptiv statistik för grupperade data
Antag att vi gjort en undersökning på 200 hushåll och fått reda på att antal medlemmar i hushållet fördelar sig som:
"""
df = pd.DataFrame(Customers['HHSize'].value_counts().rename('Antal Hushåll'))

df.index = df.index.set_names(['Antal medlemmar'])

print(df)

"""
Vad är medelvärde, median och standardavvikelse för dessa (grupperade) data?
Vi tar det "lättaste" först, medianen. Det finns 200 observationer så medianen är 3 eftersom om vi 
skulle ordna data i storleksordning skulle talen på position 100 och 101 vara 3
Medelvärdet beräknar vi enligt
 
 
För att få standardavvikelsen beräknar vi först variansen enligt
 
 
 
Standardavvikelsen är alltså 
"""

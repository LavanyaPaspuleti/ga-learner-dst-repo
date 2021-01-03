# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
plt.bar(gender_count.index, gender_count)
plt.show()

alignment = data['Alignment'].value_counts()
plt.figure(figsize=(6,6))
plt.bar(alignment.index, alignment)
plt.title('Character alignment')
plt.show()

scdf = data[['Strength','Combat']].copy()
sc_covariance = scdf.cov().iloc[0,1]
sc_strength = scdf['Strength'].std()
sc_combat = scdf['Combat'].std()

icdf = data[['Intelligence','Combat']].copy()
ic_covariance = icdf.cov().iloc[0,1]
ic_intelligence = icdf['Intelligence'].std()
ic_combat = icdf['Combat'].std()

sc_pearson = round(sc_covariance/(sc_strength*sc_combat), 2)
print("Pearson's Correlation Coefficient between Strength and Combat : ",sc_pearson)

ic_pearson = round(ic_covariance/(ic_intelligence*ic_combat), 2)
print("Pearson's Correlation Coefficient between Intelligence and Combat : ", ic_pearson)


#Find out who are the best of the best in this superhero universe by finding the value of quantile =0.99 for the Total colum and subset the df whose Total is higher than this quantile.
total_high = data['Total'].quantile(q=0.99)

super_best = data[data['Total'] > total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)
# Code starts here




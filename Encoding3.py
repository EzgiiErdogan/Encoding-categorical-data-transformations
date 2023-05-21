# -*- coding: utf-8 -*-
"""
Created on Fri May 19 00:44:47 2023

@author: 90539
"""

#kütüphane kurma işlemi
import numpy as np
import pandas as pd
import matplotlib as mp


#data yükleme işlemi
df = pd.read_csv('bike_buyers_clean.csv')
print(df)

#veri setimizden çıkartılması gereken veriler çıkarıldı
df = df.dropna()
df = df.drop('Occupation' , axis = 1 )
df = df.drop('Home Owner' , axis = 1 )
df = df.drop('Commute Distance' , axis = 1 )
df = df.drop('Region' , axis = 1 )
df = df.drop('Purchased Bike' , axis = 1 )
df = df.drop('ID' , axis = 1 )

#veri setimizde eksik veri olup olmadığını kontrol ettik
print(df.isnull().sum())


#kategorik veri dönüşümü
#Öncelikle medeniyet durumu ile başladık
Med = df.iloc[:,0:1].values
print(Med)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

Med[:,0]= le.fit_transform(df.iloc[:,0])
print(Med)

#matris formatına ceviriyoruz
ohe= preprocessing.OneHotEncoder()
Med = ohe.fit_transform(Med).toarray()
print(Med)

#çevirdiğimiz formatı data sete uygun hale getiriyoruz.
print(list(range(1000)))
sonuc=pd.DataFrame(data=Med, index = range(1000), columns = ['Married','Single'])
print(sonuc)

'''
#Cinsiyet durumu için dönüşüm
Gender = df.iloc[:,1:2].values
print(Gender)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

Gender[:,0]= le.fit_transform(df.iloc[:,1:2])
print(Gender)

#matris formatına ceviriyoruz

ohe= preprocessing.OneHotEncoder()
Gender = ohe.fit_transform(Gender).toarray()
print(Gender)

#çevirdiğimiz formatı data sete uygun hale getiriyoruz.
print(list(range(1000)))
sonuc2=pd.DataFrame(data=Gender, index = range(1000), columns = ['Female','Male'])
print(sonuc2)
'''

#Eğitim kolonu için dönüşüm


categories=pd.Categorical(df['Education'],categories=['High School','Partial High School',
                                                      'Partial College','Graduate Degree','Bachelors'],ordered=True)
print(categories)

Education,unique=pd.factorize(categories,sort=True)
df['Education']=Education
df['Education']


#dönüştürülen verilerin birleştirilmesi
Gender = df.iloc[:,1:2].values
print(Gender)

sonuc1=pd.DataFrame(data=Gender, index=range(1000), columns=['Gender'])
print(sonuc1)

Edu = df.iloc[:,2:7].values
print(Education)

sonuc4=pd.DataFrame(data=Edu, index=range(1000), columns=['Income','Children','Education','Cars','Age'])
print(sonuc4)


s=pd.concat([sonuc,sonuc1], axis=1)
print(s)

s2=pd.concat([s,sonuc4], axis=1)
print(s2)



'''
Edu = df.iloc[:,4:5].values
print(Edu)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

Edu[:,0]= le.fit_transform(df.iloc[:,4:5])
print(Edu)

#matris formatına ceviriyoruz

ohe= preprocessing.OneHotEncoder()
Edu = ohe.fit_transform(Edu).toarray()
print(Edu)


#çevirdiğimiz formatı data sete uygun hale getiriyoruz.
print(list(range(1000)))
sonuc3=pd.DataFrame(data=Edu, index = range(1000), columns = ['Bachelors','Graduate Degree', 'High School','Partial College','Partial High School'])
print(sonuc3)

'''


















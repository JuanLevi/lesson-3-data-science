import pandas as pd

data = pd.read_csv('titanic.csv')

data1 = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Pclass': [1, 2, 3], 'Fare': [72.50, 15.75, 8.05]}

df = pd.DataFrame(data1)


#print(data.head()) # head is first 5 
#print(data.tail()) # head is last 5
print(data.info()) #overall info
#print(data.describe()) # statisctical info
#print(data.dtypes) # only data types of each column


NameAge = data[['Name','Age']]
above35 = NameAge[NameAge['Age']>45]
print(above35.head())


MaleNameClass1 = data[['Name','Sex','Pclass']]
maleNames= MaleNameClass1[(MaleNameClass1['Sex']=='male')&(MaleNameClass1['Pclass']==1)]

print(maleNames.head())




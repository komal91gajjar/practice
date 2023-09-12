import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\\excel data\\houseprize advanced\\train.csv")
print(df)

df.columns
df.isnull().sum()

#plt.plot(df["MSSubClass"],df["SalePrice"])
#plt.show()

sns.barplot(x = df["MSZoning"],y = df["SalePrice"])

sns.catplot(df["SalePrice"])
plt.show()

sns.histplot(df["SaleCondition"])
plt.show()
import sklearn
from sklearn.model_selection import train_test_split

print(df.columns)

df.drop("SaleType", axis = 1, inplace = True)
df = df.drop(columns=['Functional', 'MoSold','MiscFeature'])

print(df)

sns.histplot(df["YrSold"])
plt.show()

print(df.columns)

df["Totalarea"] = df["LotFrontage"+"LotArea"+"Street"]
print(df)
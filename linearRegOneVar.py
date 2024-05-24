from sklearn import linear_model
import pandas as pd

df = pd.read_csv("dataset1.csv")

model = linear_model.LinearRegression()

 


model.fit(df[['year']], df.pci)

model.predict()
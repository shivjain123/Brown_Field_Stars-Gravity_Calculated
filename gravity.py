import pandas as pd

df = pd.read_csv('Stars/cleaned.csv')

df.drop(["Unnamed: 0"], axis = 1, inplace = True)

df['Mass']=df['Mass'].astype('float')
df["Mass"] *= 1.989e+30

df["Radius"] = df["Radius"].astype(float)
df["Radius"] *= 6.957e+8

mass_list = df["Mass"].tolist()
radius_list = df["Radius"].tolist()

gravity_list = []

for index in range(len(mass_list)):
    gravity = (6.674e-11*mass_list[index])/(radius_list[index]*radius_list[index])
    gravity_list.append(gravity)

df["Gravity"] = gravity_list

df.to_csv("Stars/Stars_with_Gravity.csv")
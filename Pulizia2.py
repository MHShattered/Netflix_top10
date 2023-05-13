import pandas as pd
types=['films','films-non-english','tv','tv-non-english']

df2= pd.DataFrame()

for type in types:
    df=pd.read_csv(f"C:/Users/User_/OneDrive/Desktop/Netflix Green/{type}_clean.csv")
    df['type']= type
    df2= pd.concat([df2, df])

mask = df2['Title'].str.startswith('Stranger Things') & df2['Title'].str.match('.*\d$')

# Create a new column 'Season' with the extracted number and replace 'Title' value
df2.loc[mask, 'Season'] = df2.loc[mask, 'Title'].str[-1]
df2.loc[mask, 'Title'] = 'Stranger Things'
df2['Season'] = df2.apply(lambda row: 0 if (row['type'] == 'films' or row['type'] == 'films-non-english') else 1 if pd.isna(row['Season']) else row['Season'], axis=1)
df2['Season']=df2['Season'].astype(int)

df2.to_csv("C:/Users/User_/OneDrive/Desktop/Netflix Green/United.csv", index=False)

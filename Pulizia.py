import pandas as pd

types=['films','films-non-english','tv','tv-non-english']
first_date='2021-07-04'

for type in types:
    df=pd.read_csv(f"C:/Users/User_/OneDrive/Desktop/Netflix Green/{type}.csv")
    df['Weeks in Top 10'] = df['Weeks in Top 10'].astype(str).str.extract('(\d+)')
    df['Season'] = df['Title'].str.extract('(Season|Part)\s*(\d+)', expand=False)[1]

    # rimuovi la stagione o parte dalla colonna 'Title'
    df['Title'] = df['Title'].str.replace('(Season|Part)\s*\d+', '', regex=True)
    df['Title'] = df['Title'].str.strip()
    df['Season'] = df['Season'].str.strip()
    df['Title'] = df['Title'].str.rstrip(':')

    df2=df[(df['Date'] >= first_date)]
    df2.to_csv(f'C:/Users/User_/OneDrive/Desktop/Netflix Green/{type}_clean.csv', index=False)


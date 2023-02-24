import pandas as pd

df = pd.read_csv('prix-carburants-fichier-instantane-test-ods-copie.csv', sep=";")

df[['latitude', 'longitude']] = df['geom'].str.split(',', expand=True)
df = df.drop('geom', axis=1)
print(df[['latitude', 'longitude']].head())
df[['ville', 'latitude', 'longitude', 'prix_valeur', 'prix_nom']].to_csv('data.csv');

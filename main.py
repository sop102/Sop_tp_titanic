# Importation des bibliothèques 
import pandas as pd
from sqlalchemy import create_engine

# Lecture des données du fichier csv
df = pd.read_csv(r'C:\Users\Emma\Downloads\archive_2\train_and_test2.csv')

# Suppression des columns inutiles
df.drop(['zero', 'zero.1',
       'zero.2', 'zero.3', 'zero.4', 'zero.5', 'zero.6', 'Parch', 'zero.7',
       'zero.8', 'zero.9', 'zero.10', 'zero.11', 'zero.12', 'zero.13',
       'zero.14', 'Pclass', 'zero.15', 'zero.16', 'Embarked', 'zero.17',
       'zero.18',], axis=1, inplace=True)
print(df.columns)
colonnes = ['id_passenger', 'age', 'fare', 'sex', 'sibsp', 'survived']
df.columns = colonnes

print(df.columns)

# Etablir la connexion à la base données
engine = create_engine('mysql+pymysql://root:@localhost/bd_titanic')

# Remplacement 'table_name' par le nom de notre table'passagers'
df.to_sql ('passagers', con=engine, if_exists ='append', index=False)

print("Connexion réussie!")

import pandas as pd
from datetime import time

df = pd.read_csv('data/dataset_asimov.csv')


df['Valor Pago'] = df['Valor Pago'].apply(lambda x: x.split(' ')[1])
df['Valor Pago'] = df['Valor Pago'].apply(lambda x: float(x))

df['Duração da chamada'] = df['Duração da chamada'].apply(lambda x: str(x))
df['Duração da chamada'] = df['Duração da chamada'].apply(lambda x: time.fromisoformat(x))
df['Horas'] = df['Duração da chamada'].apply(lambda x: x.hour)
df['Minutos'] = df['Duração da chamada'].apply(lambda x: x.minute)
df.drop(columns=['Duração da chamada'], axis=1, inplace=True)
df['Duração da chamada (min)'] = df['Horas'].apply(lambda x: x*60) + df['Minutos']
df.drop(columns=['Horas', 'Minutos'], axis=1, inplace=True)

lista_meses = df['Mês'].unique().tolist()
lista_meses.append("Ano Todo")
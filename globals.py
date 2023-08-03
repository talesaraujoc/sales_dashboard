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

lista_meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez", "Ano Todo"]

lista_equipes = df['Equipe'].unique().tolist()
lista_equipes.append("Todas")

#new dataset meses numero
dff = pd.read_csv('data/dataset_asimov.csv')
dff['Valor Pago'] = dff['Valor Pago'].apply(lambda x: x.split(' ')[1])
dff['Valor Pago'] = dff['Valor Pago'].apply(lambda x: float(x))


dff['Mês'] = dff['Mês'].map({'Jan': 1, 'Fev': 2, 'Mar':3, 'Abr':4, 'Mai':5, 'Jun':6, 'Jul':7, 'Ago':8, 'Set':9, 'Out':10, 'Nov':11, 'Dez':12})

#gráfico r2/c2/r2
df_vendas_geral = dff.groupby('Mês').agg({'Valor Pago':'sum'})
df_vendas_geral = df_vendas_geral.reset_index()

df_vendas_geral_equipe_1 = dff.loc[dff['Equipe']=='Equipe 1']
df_vendas_geral_equipe_1 = df_vendas_geral_equipe_1.groupby('Mês').agg({'Valor Pago':'sum'})
df_vendas_geral_equipe_1 = df_vendas_geral_equipe_1.reset_index()

df_vendas_geral_equipe_2 = dff.loc[dff['Equipe']=='Equipe 2']
df_vendas_geral_equipe_2 = df_vendas_geral_equipe_2.groupby('Mês').agg({'Valor Pago':'sum'})
df_vendas_geral_equipe_2 = df_vendas_geral_equipe_2.reset_index()

df_vendas_geral_equipe_3 = dff.loc[dff['Equipe']=='Equipe 3']
df_vendas_geral_equipe_3 = df_vendas_geral_equipe_3.groupby('Mês').agg({'Valor Pago':'sum'})
df_vendas_geral_equipe_3 = df_vendas_geral_equipe_3.reset_index()

df_vendas_geral_equipe_4 = dff.loc[dff['Equipe']=='Equipe 4']
df_vendas_geral_equipe_4 = df_vendas_geral_equipe_4.groupby('Mês').agg({'Valor Pago':'sum'})
df_vendas_geral_equipe_4 = df_vendas_geral_equipe_4.reset_index()

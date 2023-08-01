from dash import dash, html, dcc, Output, Input, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

import plotly as plt
from datetime import date
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import dash_ag_grid as dag


# Servidor
load_figure_template("bootstrap")

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# DataFrame =================

from globals import *


# Pré-layout ================


# Layout    =================
app.layout = html.Div([
    dbc.Row([
        dbc.Row([dbc.Col([], lg=2), dbc.Col([dcc.Graph(id='grafico-01-consultores-mes')], lg=7), dbc.Col(dbc.Row(dbc.Card(dbc.CardBody([html.H6('Escolha o mês:'), dcc.RadioItems(id='radio-meses', options=lista_meses, value=lista_meses[0]), html.Div(id='disparador-meses')]))), lg=3)]),
        
        
        dbc.Row(),
        dbc.Row()
    ])
])


# Callbacks ================
@app.callback(
    Output('grafico-01-consultores-mes', 'figure'),
    Input('radio-meses', 'value')
)
def update_grafico_01(mes):
    if mes == 'Ano Todo':
        df_target = df.groupby(['Equipe','Consultor']).agg({'Valor Pago':'sum'})
    
    else:
        df_target = df.loc[df['Mês']==mes]
    
    df_target = df_target.reset_index()
        
    df_target_equipe_1 = df_target.loc[df_target['Equipe']=='Equipe 1']
    df_target_equipe_1 = df_target_equipe_1.sort_values(by='Valor Pago', ascending=False)

    df_target_equipe_2 = df_target.loc[df_target['Equipe']=='Equipe 2']
    df_target_equipe_2 = df_target_equipe_2.sort_values(by='Valor Pago', ascending=False)

    df_target_equipe_3 = df_target.loc[df_target['Equipe']=='Equipe 3']
    df_target_equipe_3 = df_target_equipe_3.sort_values(by='Valor Pago', ascending=False)

    df_target_equipe_4 = df_target.loc[df_target['Equipe']=='Equipe 4']
    df_target_equipe_4 = df_target_equipe_4.sort_values(by='Valor Pago', ascending=False)
        
    consultor_1 = df_target_equipe_1.iloc[0]['Consultor']
    valor_1 = df_target_equipe_1.iloc[0]['Valor Pago']

    consultor_2 = df_target_equipe_2.iloc[0]['Consultor']
    valor_2 = df_target_equipe_2.iloc[0]['Valor Pago']

    consultor_3 = df_target_equipe_3.iloc[0]['Consultor']
    valor_3 = df_target_equipe_3.iloc[0]['Valor Pago']

    consultor_4 = df_target_equipe_4.iloc[0]['Consultor']
    valor_4 = df_target_equipe_4.iloc[0]['Valor Pago']
        
    lista_consultores = [consultor_1, consultor_2, consultor_3, consultor_4]
    lista_valores = [valor_1, valor_2, valor_3, valor_4]
        
    df_grafico = pd.DataFrame({'Consultor':lista_consultores, 'Valor Pago':lista_valores})
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(x=df_grafico['Consultor'], y=df_grafico['Valor Pago']))
    
    return fig
        


@app.callback(
    Output('disparador-meses', 'children'),
    Input('radio-meses', 'value')
)
def update_div_children(mes):
    children = html.H2(mes)
    return children

# Servidor =================
if __name__ == '__main__':
    app.run_server(debug=True)
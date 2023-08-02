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
update_grafico = {'margin': {'l':0, 'r':0, 't': 10, 'b':0}}

# Layout    =================
app.layout = html.Div([
    dbc.Row([
        dbc.Row([
            dbc.Col([], lg=2), 
            dbc.Col(dbc.Row(dbc.Card(dbc.CardBody([dcc.Graph(id='grafico-01-consultores-mes')]))), lg=7), 
            dbc.Col(dbc.Row(dbc.Card(dbc.CardBody([html.H6('Escolha o mês:'), dcc.RadioItems(id='radio-meses', options=lista_meses, value=lista_meses[0]), html.Div(id='disparador-meses', style={'margin-top':'30px', 'margin-bottom':'30px'})]))), lg=3)
            ]),
        
        
        dbc.Row([dbc.Col([dbc.Row(dcc.Graph(id='grafico-r2/c1/r1')), dbc.Row(dcc.Graph(id='grafico-r2/c1/r2'))], lg=5), dbc.Col([dbc.Row([dbc.Col([], lg=6), dbc.Col([], lg=6)]), dbc.Row()], lg=4), dbc.Col([], lg=3)]),
        
        
        dbc.Row([dbc.Col([], lg=2), dbc.Col([], lg=5), dbc.Col([], lg=3), dbc.Col([html.H6('Escolha o mês:'), dcc.RadioItems(id='radio-equipes', options=lista_equipes, value=lista_equipes[0]), html.Div(id='disparador-equipes', style={'margin-top':'30px', 'margin-bottom':'30px'})], lg=2)])
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
        df_target = df_target.groupby(['Equipe','Consultor']).agg({'Valor Pago':'sum'})
    
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
    
    fig = make_subplots(rows=1, cols=2,specs=[[{"type": "bar"}, {"type": "pie"}]],)

    
    fig.add_trace(go.Bar(x=df_grafico['Consultor'], y=df_grafico['Valor Pago'], showlegend=False), row=1, col=1)
    fig.add_trace(go.Pie(labels=lista_consultores, values=lista_valores, hole=0.6, showlegend=False), row=1, col=2)
    
    fig.update_layout(height=220)
    fig.update_layout(update_grafico)
    
    
    return fig
        

@app.callback(
    Output('disparador-meses', 'children'),
    Input('radio-meses', 'value')
)
def update_div_children(mes):
    if mes == 'Jan':
        children = html.H2('JANEIRO')
    elif mes == 'Fev':
        children = html.H2('FEVEREIRO')
    elif mes == 'Mar':
        children = html.H2('MARÇO')
    elif mes == 'Abr':
        children = html.H2('ABRIL')
    elif mes == 'Mai':
        children = html.H2('MAIO')
    elif mes == 'Jun':
        children = html.H2('JUNHO')
    elif mes == 'Jul':
        children = html.H2('JULHO')
    elif mes == 'Ago':
        children = html.H2('AGOSTO')
    elif mes == 'Set':
        children = html.H2('SETEMBRO')
    elif mes == 'Out':
        children = html.H2('OUTUBRO')
    elif mes == 'Nov':
        children = html.H2('NOVEMBRO')
    elif mes == 'Dez':
        children = html.H2('DEZEMBRO')
    elif mes == 'Ano Todo':
        children = html.H2('ANO')
        
    return children

@app.callback(
    Output('disparador-equipes', 'children'),
    Input('radio-equipes', 'value')
)
def update_div_children(equipe):
    children = html.H2(equipe)

    return children

@app.callback(
    Output('grafico-r2/c1/r1', 'figure'),
    [Input('radio-meses', 'value'),
    Input('radio-equipes', 'value')]
)
def update_grafico_02(mes, equipe):
    if mes == 'Ano Todo':
        if equipe == 'Todas':
            df_y = df
        else:
            df_y = df
            df_y = df_y.loc[df_y['Equipe']==equipe]
    
    else:
        if equipe == 'Todas':
            df_y = df.loc[df['Mês']==mes]
        else:
            df_y = df.loc[df['Mês']==mes]
            df_y = df_y.loc[df_y['Equipe']==equipe]
        
    
    df_y = df_y.groupby('Dia').agg({'Chamadas Realizadas':'sum'})
    df_y = df_y.reset_index()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=df_y['Dia'], y=df_y['Chamadas Realizadas'], mode='lines', fill='tonexty'))
    fig.add_annotation(text=f"Média : {round(df_y['Chamadas Realizadas'].mean(), 2)}", xref="paper", yref="paper", font=dict(size=15, color='gray'), align="center", bgcolor="rgba(0, 0, 0, 0.8)", x=0.05, y=0.55, showarrow=False)
    
    fig.update_layout(height=180)
    fig.update_layout(update_grafico)
    
    return fig


@app.callback(
    Output('grafico-r2/c1/r2', 'figure'),
    Input('radio-equipes', 'value')
)
def update_grafico_03(equipe):
    df_alpha = df.loc[df['Equipe']==equipe]
    
    df_alpha = df_alpha.groupby('Mês').agg({'Chamadas Realizadas':'sum'})

    df_alpha = df_alpha.reset_index()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=df_alpha['Mês'], y=df_alpha['Chamadas Realizadas'], mode='lines', fill='tonexty'))
    fig.add_annotation(text=f"Média : {round(df_alpha['Chamadas Realizadas'].mean(), 2)}", xref="paper", yref="paper", font=dict(size=15, color='gray'), align="center", bgcolor="rgba(0, 0, 0, 0.8)", x=0.05, y=0.55, showarrow=False)
    fig.update_layout(height=180)
    fig.update_layout(update_grafico)
    
    return fig

# Servidor =================
if __name__ == '__main__':
    app.run_server(debug=True)
from dash import dcc, html, dash_table, Input, Output, callback
from dash_extensions.enrich import ServersideOutput
import dash_bootstrap_components as dbc

import pandas as pd

from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()

import utils.funtionsGraph as fg 

Page1Graph1 = dbc.Row(children=[
    html.Div([
        dcc.Graph(id='page1_grafico1', figure={})
    ]),
])
@callback(
    Output('page1_grafico1', 'figure'),
    Input('original_data', 'data'),
    )
def display_value(data):
    data = pd.read_json(data)
    g = data.copy()
    g[["recency_s", "frequency_s", "monetary_s"]] = mms.fit_transform(g[['recency','frequency','monetary']])
    g = g.groupby('group', as_index=False)[['recency','frequency','monetary','recency_s','frequency_s','monetary_s']].mean()
    g_long_rfm = pd.melt(g, id_vars=['group','recency','frequency','monetary'], value_vars=["recency_s", "frequency_s", "monetary_s"])
    g_long_rfm.rename(columns={'group':'model'}, inplace=True)
    return fg.snake(g_long_rfm)


Page1Graph2 = dbc.Row(children=[
    html.Div([
        dcc.Graph(id='page1_grafico2', figure={}),
        dcc.Graph(id='page1_grafico3', figure={}),
        dcc.Graph(id='page1_grafico4', figure={})
    ]),
])
@callback(
    Output('page1_grafico2', 'figure'),
    Output('page1_grafico3', 'figure'),
    Output('page1_grafico4', 'figure'),
    Input('original_data', 'data'),
    )
def display_value(data):
    data = pd.read_json(data)
    fig_recency, fig_frequency, fig_monetary = fg.rfm_graph(data, 'group')
    return fig_recency, fig_frequency, fig_monetary
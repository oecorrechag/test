from dash import html

import dash_bootstrap_components as dbc

from components.CallbacksPage1 import Page1Graph1, Page1Graph2

layout1 = dbc.Container([

    dbc.Row(children=[
        Page1Graph1
    ]),

    dbc.Row(children=[
        Page1Graph2
    ]),

    
    ], id="layout1", style={'margin': '0px 50px 0px 50px'}
)

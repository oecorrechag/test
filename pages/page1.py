from dash import dcc, html, Input, Output, callback, dash_table

from components import menu

layout1 = html.Div([

    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Home', href='/'), 

    menu.layout_menu,
    html.H3('Page 1'),

    menu.layout_menu1,
    menu.layout_menu2,
    menu.layout_menu3,

])
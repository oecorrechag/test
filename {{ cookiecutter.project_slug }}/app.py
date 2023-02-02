import pandas as pd

import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from pages import page1

df = pd.read_csv('data/rfm.csv')  #, parse_dates=['Date'], dayfirst=True

data_store = html.Div([dcc.Store(id="original_data", data=df.to_json()),
                       dcc.Store(id="intermediate")
                       ])

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    dbc.icons.BOOTSTRAP,
    "https://codepen.io/chriddyp/pen/bWLwgP.css"
]

app = Dash(__name__, title = 'Dashboard test',
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)
server = app.server


app.layout = dbc.Container([

    dcc.Location(id='url'),
    data_store,

    # Header
    dbc.Row([
        dbc.Col(html.A(
            html.Img(src=app.get_asset_url("logo.png"), className="img-fluid brand-other"),
            id="logo",
            href="https://www.google.com/", target="blank"
        ), width=12, class_name='justify-content-end d-flex'),
    ]),

    # Pagina
    html.Div(id='page-content'),

    # Footer
    html.A(html.Img(src=app.get_asset_url("logo_hld0.png"),
                    className="img-fluid brand"),
            id="logo-empresarial",
            href="https://humanld.io/", target="blank"),

], fluid=True)


@callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def routing(path):
    if path == "/":
        return page1.layout1


if __name__ == '__main__':
    app.run_server(debug=True)
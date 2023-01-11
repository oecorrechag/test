
import pandas as pd

import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from components.layouts import header, footer
from pages import home, page1, page2

import glob
import os
ROOT_FOLDER = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
SRC_FOLDER = os.path.join(ROOT_FOLDER, "src/")
DATA_FOLDER = os.path.join(ROOT_FOLDER, "data/")
ASSETS_FOLDER = os.path.join(SRC_FOLDER, "assets")

df = pd.read_csv('data/df.csv')

data_store = html.Div([dcc.Store(id="filter_data", data=df.to_json()),
                       #dcc.Store(id="goals-df", data=goals.to_json())
                       ])

external_style_sheet = glob.glob(os.path.join(
    ASSETS_FOLDER, "bootstrap/css") + "/*.css")
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER,
                                  "css") + "/*.css")
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER,
                                  "fonts") + "/*.css")

app = dash.Dash(__name__, title="First test",
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP] + external_style_sheet,
                suppress_callback_exceptions=True,
                )

server = app.server



app.layout = html.Div([

    dcc.Location(id='url'),
    data_store,

    # Header
    html.Div(id='header'),

    # Pagina
    html.Div(id='page-content'),

    # Footer
    html.Div(id='footer'),

])


@callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def routing(path):
    if path == "/":
        return home.home
    elif path == "/page1":
        return page1.layout1
    elif path == "/page2":
        return page2.layout2



@callback(Output('header', 'children'),
          Output('footer', 'children'),
          Input('url', 'pathname'))
def display_page(path):
    return  header, footer


if __name__ == '__main__':
    app.run_server(debug=True)
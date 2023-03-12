import dash
from dash import html, dcc
from dash import Input, State, Output
from dash.exceptions import PreventUpdate

import pandas as pd

import dash_bootstrap_components as dbc

layout = dbc.Container([
    dcc.Store(id="store_questions"),
    dcc.Store(id="store_response"),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(dbc.Input(id="input_n_questions",type="number"),width=1,align="center"),
            dbc.Col(dbc.Button("Load Questions",id="btn_load_question",className="btn btn-warning",size="sm"),width=2,align="center"),
        ],
        justify="center"
    ),
    # Question
    html.Br(),
    dbc.Alert(id="display_question",style={"height":"20vh"},color="dark"),
    html.Hr(),
    # Options
    html.Div([
        dbc.RadioItems(
            id="radio_option"
        )
    ],id="display_options",style={"height":"40vh"}),
    html.Hr(),
    dbc.Row([
        dbc.Col(
            dbc.Button("Next",id="btn_next_question",size="sm",className="btn btn-dark mx-1",n_clicks=0),
            width=1
            ),
        dbc.Col(
            dbc.Button("Submit",id="btn_submit_response",size="sm",className="btn btn-success mx-1", disabled=True),
            width=1
            ),
        dbc.Col(
            dbc.Button("Report",id="btn_analyse_result",size="sm",className="btn btn-primary mx-1", disabled=True),
            width=1
            ),
    ],
    className="g-0",
    justify="center",
    ),
    dbc.Row(
        id="display_result"
    ),
    html.Hr(),
    dbc.Row(
        id="display_qna"
    ),
],
className="overflow_height"
)
import dash
from dash import html, dcc
from dash import Input, State, Output
from dash.exceptions import PreventUpdate

import pandas as pd

import dash_bootstrap_components as dbc

layout = dbc.Col([
    dbc.InputGroup([dbc.InputGroupText("Question"),dbc.Textarea(id="input_question",size="sm")],className="my-3"),
    dbc.RadioItems(options=[
                {"label": "Select one", "value": 0},
                {"label": "Multiple choice", "value": 1},
            ],id="radio_muliplechoice",value=0,inline=True,className="m-3"),
    dbc.InputGroup([dbc.InputGroupText("Options"),dbc.Textarea(id="input_options",size="sm")],className="mb-3"),
    dbc.InputGroup([dbc.InputGroupText("Answer"),dbc.Textarea(id="input_answer",size="sm")],className="mb-3"),
    dbc.InputGroup([dbc.InputGroupText("Reference"),dbc.Textarea(id="input_reference",size="sm")],className="mb-3"),
    dbc.InputGroup([dbc.InputGroupText("Explanation"),dbc.Textarea(id="input_explanation",size="sm")],className="mb-3"),
    dbc.Button("Insert",id="btn_insert_qna",n_clicks=0),
    dcc.Loading(html.H3(id="out_log")),
    dcc.Interval(id="interval_1sec",n_intervals=0,interval=1000),
    html.Div(id="output_logs"),
]
)
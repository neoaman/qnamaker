from dash import html, dcc
from dash_extensions.enrich import Output, Input, State, ALL, MATCH
from dash import get_app,get_asset_url
import dash_bootstrap_components as dbc



layout =  dbc.Stack(
    [
        dbc.Row([dbc.Col(dbc.InputGroupText("DATA URL"),width=4),dbc.Col(dbc.Input(),width=8)],className="g-0"),
    ],
    gap=2,
    className="ps-2 mt-2"

)
import dash
from dash import html, dcc
from dash import Input, State, Output
from dash.exceptions import PreventUpdate
from IPython.core.display import display, HTML

import pandas as pd

import dash_bootstrap_components as dbc


# LOCAL
import components as cmp

app = dash.get_app()

dash.register_page(
    __name__,
    name="Home",
    path="/"
    # top_nav=True,
)



content = dbc.Row([
    ]
)

def layout():
    return dbc.Row(
        [
            # Sidebar
            dbc.Col(
                cmp.home_sidebar,
                width=3,
                id="left_sidebar"
            ),
            # Main content
            dbc.Col(
                content,
                width=9,  
                id="main_content"
            ),
            # Right sidebar
            # dbc.Col(
            #     "Hello",
            #     width=1,  
            #     id="right_sidebar"
            # )
        ],
        id="home_layout"
        
    )


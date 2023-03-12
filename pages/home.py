import dash
from dash import DiskcacheManager
from dash import html, dcc
from dash import Input, State, Output
from dash.exceptions import PreventUpdate
from pymongo import MongoClient

import diskcache

import pandas as pd

import dash_bootstrap_components as dbc

import logging
import sys

# Set loggings
logging.basicConfig(filename='qnamaker.log', level=logging.INFO)
logger = logging.getLogger("qnamaker")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


# Background callback
cache = diskcache.Cache()
background_callback_manager = DiskcacheManager(cache)

# LOCAL
import components as cmp
import utility as utl

app = dash.get_app()

dash.register_page(
    __name__,
    name="Home",
    path="/"
    # top_nav=True,
)



content = cmp.home_content

def layout():
    return dbc.Row(
        [
            # Sidebar
            dbc.Col(
                # cmp.home_sidebar,
                width=2,
                id="left_sidebar"
            ),
            # Main content
            dbc.Col(
                content,
                width=8,
                id="main_content",
            ),
            # Right sidebar
            dbc.Col(
                # "Hello",
                width=2,  
                id="right_sidebar"
            )
        ],
        id="home_layout",
    )

@app.callback(
    Output("out_log","children"),
    Input("btn_insert_qna","n_clicks"),
    State("input_question","value"),
    State("radio_muliplechoice","value"),
    State("input_options","value"),
    State("input_answer","value"),
    State("input_reference","value"),
    State("input_explanation","value"),
)
def insert_questions(btn_insert,*args):
    if btn_insert:
        conn = MongoClient("mongodb+srv://neoaman:n30m0ng0passw0rd@oneo.easy3.mongodb.net/test")
        db,collection = "qna","gcp_mle"
        table = conn[db][collection]
        uuid = utl.insert_qna(table,*args)

    return uuid

@app.callback(
    Output("output_logs","children"),
    Input("interval_1sec","n_intervals"),
    # background=True,
    # manager=background_callback_manager,
)
def render_log(*args):
    with open("qnamaker.log") as qlog:
        logs = qlog.readlines()
    logs.reverse()
    return [html.Div(i) for i in (logs)]
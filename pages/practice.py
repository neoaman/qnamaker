import dash
from dash import DiskcacheManager
from dash import html, dcc
from dash import Input, State, Output, no_update, ctx
from dash.exceptions import PreventUpdate
from pymongo import MongoClient
import random

import diskcache

import pandas as pd

import dash_bootstrap_components as dbc

import logging
import sys

logger = logging.getLogger("qnamaker")


# Background callback
cache = diskcache.Cache()
background_callback_manager = DiskcacheManager(cache)

# LOCAL
import components as cmp
import utility as utl

app = dash.get_app()

dash.register_page(
    __name__,
    name="Practice",
    path="/practice"
    # top_nav=True,
)



content = cmp.practice_content

def layout():
    return dbc.Row(
        [
            # Sidebar
            dbc.Col(
                # cmp.home_sidebar,
                width=2,
                # id="left_sidebar"
            ),
            # Main content
            dbc.Col(
                content,
                width=8,  
                # id="main_content"
            ),
            # Right sidebar
            dbc.Col(
                # "Hello",
                width=2,  
                # id="right_sidebar"
            )
        ],
        # id="home_layout"
        
    )

@app.callback(
    Output("store_questions","data"),
    Output("btn_load_question","style"),
    Output("input_n_questions","style"),
    Input("btn_load_question","n_clicks"),
    State("input_n_questions","value"),
)
def insert_questions(btn_insert,number_of_q):
    conn = MongoClient("mongodb+srv://neoaman:n30m0ng0passw0rd@oneo.easy3.mongodb.net/test")
    db,collection = "qna","gcp_mle"
    table = conn[db][collection]

    qna_list = utl.get_qna(table)
    selected_question = random.choices(qna_list,k=number_of_q)

    return selected_question,{"display":"none"},{"display":"none"}

@app.callback(
    Output("display_question","children"),
    Output("radio_option","options"),
    Output("store_response","data"),
    Output("radio_option","value"),
    Output("btn_next_question","n_clicks"),
    Input("store_questions","data"),
    State("radio_option","value"),
    State("store_response","data"),
    Input("btn_next_question","n_clicks"),
)
def insert_questions(question_list,current_option,ans_response,btn_state):

    if ans_response == None : ans_response = {} 

    if (
        (not ctx.triggered_id == "store_questions") 
        and (not current_option)
        ):
        return no_update, no_update, no_update, None, btn_state -1
    try:
        current_question = question_list[btn_state]
        question = [f"Q {btn_state+1} : "]+current_question["question"]
        available_options = current_question["options"]
        radio_option = [{"label":i,"value":i} for i in available_options]
        ans_response.update({btn_state:current_option})
    except: 
        ans_response.update({btn_state:current_option})
        return no_update, no_update, ans_response, None, btn_state -1

    if ctx.triggered_id == "store_questions":
        return question, radio_option, no_update, None, btn_state

    if ctx.triggered_id == "store_questions":
        return question, radio_option, no_update, None, btn_state
        
    return question, radio_option, ans_response, None, btn_state

@app.callback(
    Output("display_result","children"),
    Output("btn_analyse_result","disabled"),
    State("store_questions","data"),
    State("store_response","data"),
    Input("btn_submit_response","n_clicks"),
    prevent_initial_callback=True
)
def evaluate_reslt(question_data,response_data,*args):
    # logger.warning(response_data)
    answers = [q_a["answer"][0] for q_a in question_data]
    no_correct = sum([answers[int(i)-1]==j for i,j in response_data.items()])

    return  "{}/{} correct answer".format(no_correct,len(response_data)),False

@app.callback(
    Output("btn_submit_response","disabled"),
    Input("btn_next_question","n_clicks"),
    State("input_n_questions","value"),
    prevent_initial_callback=True
)
def evaluate_reslt(btn_next,number_question):

    if btn_next+1 == number_question:
        return False
    else:
        raise PreventUpdate
    
@app.callback(
    Output("display_qna","children"),
    Input("btn_analyse_result","n_clicks"),
    State("store_questions","data"),
    State("store_response","data"),
    prevent_initial_callback=True
)
def evaluate_reslt(btn_analyse,questions,responses):

    children = [
        dbc.Container([
            html.Div([
                dbc.Alert(["Q ",id," : "]+q["question"],color="light"),
                html.Hr(),
                html.Div(
                    [
                        dbc.Alert(i, color=(
                            "success" if (i==q["answer"][0] and i==responses[str(id+1)]) 
                            else "danger" if (i==responses[str(id+1)])
                            else "info" if (i==q["answer"][0])
                            else "light"
                            )) 
                        for i in 
                        q["options"]
                    ]
                ),
            html.Hr()
            ]) 
            for id,q in enumerate(questions)
        ])
    ]
    return children
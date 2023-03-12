# INTERNAL

# EXTERNAL
import dash
from dash import Dash, Input, Output, State
from dash import dcc, html 
from dash import ALL, MATCH
import dash_bootstrap_components as dbc

# LOCAL
import components as cmp

#-----------------------------------------------------------------------------------------------
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP],prevent_initial_callbacks=True)


APP_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
APP_NAME = "QnA-Maker"

#---------------------------------------Base Layout---------------------------------------------
app.layout =  html.Div([
    # Navbar
    dbc.Navbar(

        [
            dbc.Row(
                [
                dbc.Col(html.Img(src=APP_LOGO, height="30px")),
                dbc.Col(dbc.NavbarBrand(APP_NAME, className="ms-2")), 
                dbc.Col(dbc.Button(
                    html.I(className="bi bi-layout-text-sidebar text-light"),id="nav-btn-sidebar",n_clicks=0,className="btn-secondary btn-sm")),
                ],
                align="center",
                className="g-0",
            ),
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink(page["name"], href=page["path"], active="exact"),className="btn btn-sm") 
                    for page in dash.page_registry.values()
                ],
                vertical=False,
                pills=True,
                className="ms-5",
            )
        ],
        className="ps-2",
        id="app_navbar",
        dark="true",
        color="dark"

    ),
    # Offcanvas sidebar
    dbc.Offcanvas(cmp.offcanvas_sidebar,id="offcanvas-leftbar"),
    # Page container
    dbc.Row(
        dash.page_container,
    ),
],
id="app_layout",
)

#----------------------------------------Callbacks----------------------------------------------

@app.callback(
    Output('offcanvas-leftbar','is_open'),
    [State('offcanvas-leftbar','is_open')],
    [Input('nav-btn-sidebar','n_clicks')],
)
def open_sidebar(status,*args):
    return not status


if __name__ == "__main__":
    app.run_server(debug=True)
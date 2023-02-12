import dash
from dash import get_app, get_asset_url
from dash import html, dcc
from dash_extensions.enrich import Output, Input, State, ALL, MATCH
from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc


# LOCAL
import components as cmp

app = get_app()

dash.register_page(
    __name__,
    name="FAQ",
    # top_nav=True,
)


def layout():
    return html.Div(
        [
            # Sidebar
            # dbc.Offcanvas(cmp.sidebar,id="offcanvas-leftbar"),
            "FAQ Page",
            #
        ]
    )

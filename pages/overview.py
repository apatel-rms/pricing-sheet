import dash_html_components as html
import dash_core_components as dcc
from components import make_dash_table, make_ep_graph, Header


def get_overview_page(company_facts, key_losses):
    
    page = html.Div([
        Header(),
        html.Div([
            html.Div([
                html.H6('Summary', className="gs-header gs-text-header padded"),
                html.Br([]),
                html.P('This is a bunch of text about the submission')
            ], className="six columns"),

            html.Div([
                html.H6('Key info', className="gs-header gs-text-header padded"),
                html.Table(make_dash_table(company_facts))
            ], className="six columns")
        ], 
        className="row "),

        html.Div([
            

            html.Div([
                html.H6('Key Losses', className="gs-header gs-text-header padded"),
                html.Table(make_dash_table(key_losses, display_header=True))
            ], className="six columns"),

            html.Div([
                html.H6('Losses to us', className="gs-header gs-text-header padded"),
                # dcc.Input(id='my-share', type='number', value=100),
                dcc.Slider(
                    id='share-slider',
                    min=0,
                    max=100,
                    step=0.1,
                    value=100
                ),
                html.Div(id='our-losses-table'),
                # html.Table(make_dash_table(key_losses, display_header=True))
            ], className="six columns")
        ], 
        className="row "),

        ], className="page")

        
    return page
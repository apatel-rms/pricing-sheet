import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_table

from pages import register_callbacks, get_no_page, get_overview_page, get_exposure_summary_page, get_ep_curve_page, get_portfolio_impact_page

app = dash.Dash(__name__)
server=app.server
server.secret_key = os.environ.get('secret_key', 'secret')
app.config['suppress_callback_exceptions']=True

def load_dataframe(filename):
    df_ = pd.read_csv(filename)
    return df_  

# df = load_dataframe('account.csv')
company_facts = load_dataframe('data/company_a_facts.csv')
ep_curves = load_dataframe('data/company_a_ep_curves.csv')
loc = load_dataframe('data/loc.csv')
key_losses = load_dataframe('data/keylosses.csv')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

register_callbacks(app, key_losses)

@app.callback(dash.dependencies.Output('page-content', 'children'),
            [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return get_overview_page(company_facts, key_losses)
    if pathname == '/exposure-summary':
        return get_exposure_summary_page(loc)
    if pathname == '/ep-curves':
        return get_ep_curve_page(ep_curves)
    if pathname == '/portfolio-impact':
        return get_portfolio_impact_page()
    else:
        return get_no_page()



external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css", #responsive
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css", # component layouts
                "https://codepen.io/bcd/pen/KQrXdb.css",] # majority of the styling
for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == '__main__':
    app.run_server(debug=True)
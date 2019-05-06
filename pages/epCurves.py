import dash_html_components as html
from components import make_dash_table, make_ep_graph, Header

def get_ep_curve_page(ep_curves):
    page = html.Div([
        Header(),

        html.Div([
            html.Div([
                    html.H6('All Perils EP', className="gs-header gs-text-header padded"),
                    html.Table(make_dash_table(
                        ep_curves[['Return Period', 'groundup (AEP | ALL) (USD)', 'groundup (OEP | ALL) (USD)']]
                        .sort_values('Return Period', ascending=False),
                        display_header=True))
                ], className="six columns"),

                html.Div([
                    html.H6('All Perils EP Curve', className="gs-header gs-text-header padded"),
                    make_ep_graph(ep_curves[['Return Period', 'groundup (AEP | ALL) (USD)', 'groundup (OEP | ALL) (USD)']])
                ], className="six columns")
            ], 
            className="row "),

        html.Div([
            html.Div([
                    html.H6('EQ EP', className="gs-header gs-text-header padded"),
                    html.Table(make_dash_table(ep_curves[['Return Period', 'groundup (AEP | Earthquake) (USD)', 'groundup (OEP | Earthquake) (USD)']]
                    .sort_values('Return Period', ascending=False),
                    display_header=True))
                ], className="six columns"),

                html.Div([
                    html.H6('EQ EP Curve', className="gs-header gs-text-header padded"),
                    make_ep_graph(ep_curves[['Return Period', 'groundup (AEP | Earthquake) (USD)', 'groundup (OEP | Earthquake) (USD)']])
                ], className="six columns")
            ], 
            className="row "),

        html.Div([
            html.Div([
                    html.H6('WS EP', className="gs-header gs-text-header padded"),
                    html.Table(make_dash_table(ep_curves[['Return Period', 'groundup (AEP | Windstorm) (USD)', 'groundup (OEP | Windstorm) (USD)']]
                    .sort_values('Return Period', ascending=False),
                    display_header=True))
                ], className="six columns"),

                html.Div([
                    html.H6('WS EP Curve', className="gs-header gs-text-header padded"),
                    make_ep_graph(ep_curves[['Return Period', 'groundup (AEP | Windstorm) (USD)', 'groundup (OEP | Windstorm) (USD)']])
                ], className="six columns")
            ], 
            className="row ")

        ], className="page")
    return page
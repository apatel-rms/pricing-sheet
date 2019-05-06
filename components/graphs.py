import dash_core_components as dcc
import plotly.graph_objs as go

def make_ep_graph(dataframe):
        
    graph = dcc.Graph(
        figure = go.Figure(
            data=[
                go.Scatter(
                    x=dataframe['Return Period'],
                    y=dataframe.iloc[:,1],
                    name='AEP'
                ),
                go.Scatter(
                    x=dataframe['Return Period'],
                    y=dataframe.iloc[:,2],
                    name='OEP'
                )
            ],
            layout={
                'xaxis': {'title': 'Return Period'},
                'yaxis': {'title': 'Loss'}
            }
        )
    )
    return graph

def make_tiv_bar_graph(dataframe, facet):
    graph = dcc.Graph(
        figure = go.Figure(
            data=[
                go.Bar(
                    x=dataframe[facet],
                    y=dataframe['TIV']
                )
            ],
            layout={
                'xaxis': {'title': facet},
                'yaxis': {'title': 'TIV'}
            }
        )
    )
    return graph
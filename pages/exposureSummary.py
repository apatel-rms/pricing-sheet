import dash_html_components as html
from components import make_dash_table, Header, make_tiv_bar_graph
import pandas as pd

def get_exposure_subset(loc):
    exposureSubset = loc[['LOCNUM', 'STATECODE', 'BLDGSCHEME', 'BLDGCLASS', 'OCCSCHEME', 'OCCTYPE', 'EQCV1VAL', 'EQCV2VAL', 'EQCV3VAL', 'EQCV4VAL', 'WSCV4VAL', 'WSCV6VAL', 'WSCV7VAL']]
    exposureSubset = exposureSubset.fillna(value=0)
    exposureSubset['EQTOTAL'] = exposureSubset.apply(lambda row: row.EQCV1VAL + row.EQCV2VAL + row.EQCV3VAL + row.EQCV4VAL, axis=1)
    exposureSubset['WSTOTAL'] = exposureSubset.apply(lambda row: row.WSCV4VAL + row.WSCV6VAL + row.WSCV7VAL, axis=1)
    exposureSubset['TOTAL'] = exposureSubset.apply(lambda row: row.EQTOTAL + row.WSTOTAL, axis=1)
    return exposureSubset

def enrich_with_occupancy(dataframe):
    occType = pd.read_csv('data/occtype.csv')
    merged = pd.merge(dataframe, occType, how='left', on='OCCTYPE')
    return merged

def enrich_with_construction(dataframe):
    consClass = pd.read_csv('data/consclass.csv')
    merged = pd.merge(dataframe, consClass, how='left', on='BLDGCLASS')
    return merged

def get_exposure_summary_page(loc):
    exposureSubset = get_exposure_subset(loc)
    exposureSubset.rename(columns={'TOTAL':'TIV'}, inplace=True)
    enriched = enrich_with_occupancy(exposureSubset)
    enriched = enrich_with_construction(enriched)

    tiv_by_state = enriched.groupby('STATECODE').sum().sort_values('TIV', ascending=False)
    tiv_by_state['State'] = tiv_by_state.index
    tiv_by_state = tiv_by_state[['State', 'TIV']]

    
 
    tiv_by_occupancy = enriched.groupby('OccDesc').sum().sort_values('TIV', ascending=False)
    tiv_by_occupancy['Occupancy'] = tiv_by_occupancy.index
    tiv_by_occupancy = tiv_by_occupancy[['Occupancy', 'TIV']]

    tiv_by_construction= enriched.groupby('ConsDesc').sum().sort_values('TIV', ascending=False)
    tiv_by_construction['Construction'] = tiv_by_construction.index
    tiv_by_construction = tiv_by_construction[['Construction', 'TIV']]
    
    page = html.Div([
        Header(),
        html.Div([
            html.Div([
                    html.H6('TIV by State', className="gs-header gs-text-header padded"),
                    html.Table(make_dash_table(
                        tiv_by_state,
                        display_header=True))
                ], className="six columns"),
            
            html.Div([
                    html.H6('TIV by State', className="gs-header gs-text-header padded"),
                    make_tiv_bar_graph(tiv_by_state, 'State')
                ], className="six columns")
                
            ], 
            className="row "),
        
        html.Div([
            html.Div([
                    html.H6('TIV by Occupancy', className="gs-header gs-text-header padded"),
                    html.Table(make_dash_table(
                        tiv_by_occupancy,
                        display_header=True))
                ], className="six columns"),
            
            html.Div([
                    html.H6('TIV by Occupancy', className="gs-header gs-text-header padded"),
                    make_tiv_bar_graph(tiv_by_occupancy, 'Occupancy')
                ], className="six columns")
                
            ], 
            className="row "),

        html.Div([
            html.Div([
                    html.H6('TIV by Construction', className="gs-header gs-text-header padded"),
                    html.Table(make_dash_table(
                        tiv_by_construction,
                        display_header=True))
                ], className="six columns"),
            
            html.Div([
                    html.H6('TIV by Construction', className="gs-header gs-text-header padded"),
                    make_tiv_bar_graph(tiv_by_construction, 'Construction')
                ], className="six columns")
                
            ], 
            className="row "),

    ], className="page")
    return page
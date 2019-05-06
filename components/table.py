import dash_html_components as html

def make_dash_table(df, display_header = False, print_index = False):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    table = []
    if display_header == True:
        a = []
        if print_index == True:
            a.append(html.Th(df.index.name))
        [a.append(html.Th(col)) for col in df.columns]
        table.append(html.Tr(a))
    for index, row in df.iterrows():
        html_row = []
        if print_index == True:
            html_row.append(html.Td(index))
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
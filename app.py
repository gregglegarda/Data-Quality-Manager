import dash
from dash import html
from dash import dcc



############ Import modules
import initialize
beer_fig = initialize.setup_chart()


########### Initiate the app
app = dash.Dash(__name__)
server = app.server
app.title = initialize.tabtitle
theme = {
    'dark': True,
    'detail':'#007439',
    'primary':'#00EA64',
    'secondary':'#6E6E6E',
}

########### Set up the layout
app.layout = html.Div(children=[

    #########################   NAV BAR CONTAINER  #########################
    html.Div([
        html.Img(src=app.get_asset_url("logo.png"),style={'height':'50px', 'display':'inline-block', 'vertical-align':'middle'}),
        html.H6([initialize.myheading], style = {'color':'white', 'margin-left':'20px', 'display':'inline-block', 'vertical-align':'middle'}),
    ], style = {'background-color':'#464646', 'margin-bottom':'20px', 'padding':'10px'}),


    #########################   CONTROLS CONTAINER   #########################
    html.Div([
        html.Div([
                dcc.Dropdown(id='dropdown',
                             options=[{}],
                             value = 'sample')
        ],),
    ],style={'display':'inline-block', 'width':'29%', 'vertical-align':'top'}),

    #########################   TAB AND GRAPH CONTAINER   #########################
    html.Div([
        dcc.Tabs(id='tabs',value='tab1',children=[
            dcc.Tab(label='Chart1', value = 'tab1'),
            dcc.Tab(label='Chart2', value = 'tab2'),
        ]),
        dcc.Loading(id='loading', type = 'default'),
        dcc.Graph(
                id='chart',
                figure=beer_fig
            ),
    ],style={'display':'inline-block', 'width':'70%'}),


    ]
)

if __name__ == '__main__':
    app.run_server()

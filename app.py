import dash
from dash import html
from dash import dcc



############ Import modules
import initialize
beer_fig = initialize.setup_chart()


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title= initialize.tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(initialize.myheading),
    dcc.Graph(
        id='chart',
        figure=beer_fig
    ),
    ]
)

if __name__ == '__main__':
    app.run_server()

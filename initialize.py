import plotly.graph_objs as go



################################# Define your paths #################################
path = "C:/Users/gregglegarda/dataqualitymanager/"

################################# Define your variables #################################
tabtitle='Data Quality Viewer'
myheading='Data Quality Viewer by Gregg Legarda'
chart_height = 600
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Directory Name'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'





#################################  Set up the chart #################################
def setup_chart():
    bitterness = go.Scatter(
        x=beers,
        y=ibu_values,
        name=label1,
        mode='lines+markers',
        marker={'color':color1}
    )
    alcohol = go.Scatter(
        x=beers,
        y=abv_values,
        name=label2,
        mode = 'lines+markers',
        marker={'color':color2}
    )

    beer_data = [bitterness, alcohol]
    beer_layout = go.Layout(
        barmode='group',
        title = mytitle,
        height = chart_height
    )

    beer_fig = go.Figure(data=beer_data, layout=beer_layout)
    return beer_fig

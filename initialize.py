import plotly.graph_objs as go



################################# Define your paths #################################
path = "C:/Users/gregglegardaapth/dataqualitymanager/"

################################# Define your variables #################################
tabtitle='beer tab title!'
myheading='Data Quality Manager'
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
    bitterness = go.Bar(
        x=beers,
        y=ibu_values,
        name=label1,
        marker={'color':color1}
    )
    alcohol = go.Bar(
        x=beers,
        y=abv_values,
        name=label2,
        marker={'color':color2}
    )

    beer_data = [bitterness, alcohol]
    beer_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    beer_fig = go.Figure(data=beer_data, layout=beer_layout)
    return beer_fig

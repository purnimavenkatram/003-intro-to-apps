######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
states=['California', 'Texas', 'Florida', 'New York','Pennsylvania','Alaska', 'Montana' , 'New Mexico']
#Size values
s_values=[163694.74, 268596.46, 65757.70, 54554.98, 46054.34, 665384.04, 147039.71 , 121590.30]
#Population values
p_values=[39237836, 29527941, 21781128, 19835913, 12964056, 732673, 1104271, 2115877]

color1='green'
color2='blue'
mytitle='Size vs Population comparison of top 5 biggest and most populous states'

label1='Size'
label2='Population'

########### Set up the chart

def make_that_cool_barchart(beers, ibu_values, abv_values, color1, color2, mytitle):
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


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(states, s_values, p_values, color1, color2, mytitle)
    fig.write_html('docs/state_stats.html')
    print('We successfully updated the barchart!')

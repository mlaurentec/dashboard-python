# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Usuarios": [4104 , 7393, 9873, 2000, 5000, 8000],
    "City": ["Tokio", "Paris", "Lima", "Buenos Aires", "Bruselas", "Malaga"]
})

fig = px.bar(df, x="City", y="Usuarios", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Dashboard de usuarios'),

    html.Div(children='''
        Segmentación de usurios de la aplicación por ciudades.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

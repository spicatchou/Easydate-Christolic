import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("/Users/dangnguyenviet/Desktop/Master 2 SISE/cours/python-data project/data_cleaned.csv",index_col=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Label(['Choisissez une variable']),
        dcc.Dropdown(
         id='id_dropdown',
         options=[{'label': i, 'value': i} for i in df.columns],
          value='match',
          multi = False,
          style={"width":"50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph')]),
])

@app.callback(
   Output(component_id='the_graph',component_property='figure'),
   [Input(component_id='id_dropdown',component_property='value')]
)

def update_graph(id_dropdown):
  dff = df
  piechart = px.pie(
      data_frame = dff,
      names = id_dropdown,
      hole = .2,
  )
  return (piechart)

if __name__ == '__main__':
    app.run_server(port=3050,debug=True)
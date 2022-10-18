from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd



df = pd.read_csv("/Users/dangnguyenviet/Desktop/Master 2 SISE/cours/python-data project/data_cleaned.csv",index_col=0)


app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H4('Nuage de points interactif'),
        dcc.Graph(id="scatter-plot"),
        html.P("Filter by fun_o:"),
        dcc.RangeSlider(
         id='range-slider',
         min=0, max=10, step=1,
         marks={0:'0',10:'10'},
         value=[0,10]
        
          
        ),
    ]),

])

@app.callback(
   Output(component_id="scatter-plot",component_property='figure'),
   [Input(component_id='range-slider',component_property='value')]
)

def update_graph(slider_range):
  dff = df
  low,high = slider_range
  mask = (dff['fun_o'] > low) & (dff['fun_o'] < high)
  scatter_plot = px.scatter(
    dff[mask], x='age', y='age_o',
    color="match", size='condtn',
    hover_data = ['fun_o']
  )
  return (scatter_plot)

if __name__ == '__main__':
    app.run_server(port=3050,debug=True)
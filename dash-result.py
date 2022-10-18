import dash
from dash import Input, Output,html,dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("/Users/dangnguyenviet/Desktop/Master 2 SISE/cours/python-data project/submission 1 - score 0.50670/my_submission.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label(['Choose id number']),
    dcc.Dropdown(
        id='id_dropdown',
        options=[{'label': i, 'value': i} for i in df.iid_pid]
        ),
    html.Div(id='output'),
    
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.Label(['Result analysis']),
    dcc.Dropdown(
        id='id_result',
        options=[{'label': 'Pie Chart Result', 'value': "target"}]
        ),
   
   html.Div([
        dcc.Graph(id='the_graph')])

])

@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('id_dropdown', 'value')])
def update_children(value):
    if value in (k for k in df.loc[df["target"]==1,["iid_pid"]]["iid_pid"]):
        return ("Match")
    else:
        return("No Match")

@app.callback(
    dash.dependencies.Output('the_graph', 'figure'),
    [dash.dependencies.Input('id_result', 'value')])
def update_graph(id_result):
  dff = df
  piechart = px.pie(
      data_frame = dff,
      names = id_result,
      hole = .2,
  )
  return (piechart)
        
if __name__ == '__main__':
    app.run_server(debug=True)


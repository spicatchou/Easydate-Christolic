import dash
from dash import Input, Output,html,dcc
import plotly.express as px
import pandas as pd
from PIL import Image

df = pd.read_csv("data_cleaned.csv",index_col=0)
df_result = pd.read_csv("my_submission.csv")
logo=Image.open("logo.png")

app = dash.Dash(__name__)
server=app.server

app.layout = html.Div([
    html.Div([
        html.Img(src=logo, height="300",width="1200"),
        
        html.H2("Data Explorer", className="display-5"),
        html.Hr(),
        
        html.H4('Pie Chart'),
        html.Br(),
        
        html.Label(['Choisissez une variable']),
        dcc.Dropdown(
         id='id_dropdown_pie',
         options=[{'label': i, 'value': i} for i in df.columns],
          value='match',
          multi = False,
          style={"width":"50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph_pie')]),
    
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.H4('Bar Chart'),
    html.Br(),
    
    html.Div([
        html.Label(['Choisissez une variable']),
        dcc.Dropdown(
         id='id_dropdown_bar',
         options=[
             {'label': 'Race', 'value': 'race'},
             {'label': 'Age', 'value': 'age'},
             {'label': 'Career', 'value': 'career_c'},
             {'label': 'Income', 'value': 'income'},
             {'label': 'Go-out', 'value': 'go_out'},
             {'label': 'Gender', 'value': 'gender'},
             {'label': 'Fun', 'value': 'fun_o'},
             {'label': 'Share', 'value': 'shar_o'},
             {'label': 'Attrative', 'value': 'attr_o'},
             {'label': 'Intelligent', 'value': 'intel_o'}
             ],
          value='age'
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph_bar')]),
    
    html.Br(),
    html.Br(),
    html.Br(),
    
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
    
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.H2("Result Explorer", className="display-5"),
    html.Hr(),
    
     html.Label(['Choose id number']),
    dcc.Dropdown(
        id='id_dropdown_result',
        options=[{'label': i, 'value': i} for i in df_result.iid_pid]
        ),
    html.Div(id='output_result'),
    
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.Label(['Result analysis']),
    dcc.Dropdown(
        id='id_result',
        options=[{'label': 'Pie Chart Result', 'value': "target"}]
        ),
   
   html.Div([
        dcc.Graph(id='the_graph_result')])
    
])

@app.callback(
   Output(component_id='the_graph_pie',component_property='figure'),
   [Input(component_id='id_dropdown_pie',component_property='value')]
)
def update_graph_pie(id_dropdown_pie):
  dff = df
  piechart = px.pie(
      data_frame = dff,
      names = id_dropdown_pie,
      hole = .2,
  )
  return (piechart)


@app.callback(
   Output(component_id='the_graph_bar',component_property='figure'),
   [Input(component_id='id_dropdown_bar',component_property='value')]
)
def select_graph_bar(value):
    dff = df
    if value == 'race':
        fig1 = px.histogram(
        data_frame = dff,
        x="race",
        color="match",
        barmode='group')
        return fig1
    
    elif value =="age":
        fig2 = px.histogram(
        data_frame = dff,
        x="age",
        color="match",
        barmode='group')
        return fig2
    
    elif value =="career_c":
        fig3 = px.histogram(
        data_frame = dff,
         x="career_c",
         color="match",
        barmode='group')
        return fig3
    elif value =="income":
        fig4 = px.histogram(
        data_frame = dff,
         x="income",
        color="match",
        barmode='group')
        return fig4
    
    elif value =="gender":
        fig5 = px.histogram(
        data_frame = dff,
         x="gender",
        color="match",
        barmode='group')
        return fig5
    
    elif value =="fun_o":
        fig6 = px.histogram(
        data_frame = dff,
         x="fun_o",
        color="match",
        barmode='group')
        return fig6
    
    elif value =="shar_o":
        fig7 = px.histogram(
        data_frame = dff,
         x="shar_o",
        color="match",
        barmode='group')
        return fig7
    
    elif value =="attr_o":
        fig8 = px.histogram(
        data_frame = dff,
         x="attr_o",
        color="match",
        barmode='group')
        return fig8
    
    elif value =="intel_o":
        fig9 = px.histogram(
        data_frame = dff,
         x="intel_o",
        color="match",
        barmode='group')
        return fig9
    
    else:
        fig10 = px.histogram(
        data_frame = dff,
         x="go_out",
        color="match",
        barmode='group')
        return fig10

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

@app.callback(
    dash.dependencies.Output('output_result', 'children'),
    [dash.dependencies.Input('id_dropdown_result', 'value')])
def update_children(value):
    if value in (k for k in df_result.loc[df_result["target"]==1,["iid_pid"]]["iid_pid"]):
        return ("Match")
    else:
        return("No Match")

@app.callback(
    dash.dependencies.Output('the_graph_result', 'figure'),
    [dash.dependencies.Input('id_result', 'value')])
def update_graph_result(id_result):
  dff_result = df_result
  piechart_result = px.pie(
      data_frame = dff_result,
      names = id_result,
      hole = .2,
  )
  return (piechart_result)

if __name__ == '__main__':
    app.run_server(debug=True)
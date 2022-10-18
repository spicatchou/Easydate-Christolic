import dash
from dash import Input, Output,dcc,html
import plotly.express as px
import pandas as pd

df = pd.read_csv("/Users/dangnguyenviet/Desktop/Master 2 SISE/cours/python-data project/data_cleaned.csv",index_col=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Label(['Choisissez une variable']),
        dcc.Dropdown(
         id='id_dropdown',
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
        dcc.Graph(id='the_graph')]),
])

@app.callback(
   Output(component_id='the_graph',component_property='figure'),
   [Input(component_id='id_dropdown',component_property='value')]
)

def select_graph(value):
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

if __name__ == '__main__':
    app.run_server(port=4050,debug=True)
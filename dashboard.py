"""Interactive dashboard for the official IBM SpaceX course snapshot."""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
ROOT=Path(__file__).resolve().parent
df=pd.read_csv(ROOT/'data'/'spacex_launch_dash.csv')
app=Dash(__name__)
app.layout=html.Div([
 html.H1('SpaceX launch outcomes',style={'color':'#0B1930'}),
 html.P('IBM historical course snapshot. Green/blue points indicate Class=1. This dashboard contains 56 launches; the modeling dataset contains 90.'),
 html.Label('Launch site'),
 dcc.Dropdown(id='site-dropdown',options=[{'label':'All sites','value':'ALL'}]+[{'label':s,'value':s} for s in sorted(df['Launch Site'].unique())],value='ALL',clearable=False),
 dcc.Graph(id='success-pie-chart'),
 html.Label('Payload range (kg)'),
 dcc.RangeSlider(id='payload-slider',min=0,max=10000,step=500,value=[0,10000],marks={x:str(x) for x in range(0,10001,1000)}),
 dcc.Graph(id='success-payload-scatter-chart'),
 html.P(id='filter-summary')],style={'maxWidth':'1180px','margin':'24px auto','fontFamily':'Arial','padding':'0 25px'})
@app.callback(Output('success-pie-chart','figure'),Output('success-payload-scatter-chart','figure'),Output('filter-summary','children'),Input('site-dropdown','value'),Input('payload-slider','value'))
def update(site,payload):
 filtered=df[df['Payload Mass (kg)'].between(*payload)]
 if site!='ALL':filtered=filtered[filtered['Launch Site'].eq(site)]
 if site=='ALL':
  counts=filtered.groupby('Launch Site',as_index=False)['class'].sum();pie=px.pie(counts,values='class',names='Launch Site',title='Share of successful landings by site')
 else:
  counts=filtered['class'].value_counts().reindex([0,1],fill_value=0).rename_axis('Class').reset_index(name='Count');counts['Outcome']=counts.Class.map({0:'Class 0',1:'Class 1'})
  pie=px.pie(counts,values='Count',names='Outcome',title=f'{site}: landing success and failure')
 scatter=px.scatter(filtered,x='Payload Mass (kg)',y='class',color='Booster Version Category',hover_data=['Launch Site','Flight Number'],title='Payload and landing outcome by booster category')
 scatter.update_yaxes(tickvals=[0,1],ticktext=['Class 0','Class 1'])
 return pie,scatter,f'{len(filtered)} launches shown; {int(filtered["class"].sum())} successful. Payload {payload[0]:,} to {payload[1]:,} kg.'
if __name__=='__main__':app.run(host='127.0.0.1',port=8050,debug=False)

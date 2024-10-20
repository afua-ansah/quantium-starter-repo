from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#f4f4f9',
    'text': '#2c3e50'
}

df = pd.read_csv('data/processed_data.csv')
df = df.sort_values(by='date')

fig = px.line(df, x="date", y="sales", line_shape='linear',
              labels={'date': 'Date', 'sales': 'Sales Amount'})

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis=dict(
            showline=True,
            showgrid=False
        ),
    yaxis=dict(
            showline=True,
            showgrid=True,
        )
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sales Prices of Pink Morsel',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontSize': '36px', 
            'paddingBottom': '20px'
        }
    ),

    html.Div([
        html.Label('Filter by Region:', style={'fontSize': '20px', 'color': colors['text']}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'marginRight': '15px', 'color': colors['text'], 'fontSize': '18px'}
        )
    ], style={'textAlign': 'center', 'paddingBottom': '30px'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Callback to update the graph based on region selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-filter', 'value')]
)
def update_graph(selected_region):
    # Filter the DataFrame based on selected region
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Create the line chart
    fig = px.line(filtered_df, x='date', y='sales',
                  labels={'date': 'Date', 'sales': 'Sales Amount'},
                  line_shape='linear')

    # Customize the chart layout
    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis=dict(
            showline=True,
            showgrid=False
        ),
    yaxis=dict(
            showline=True,
            showgrid=True,
        )
)
    
    return fig

if __name__ == '__main__':
    # app.run(debug=True)
    app.run_server()


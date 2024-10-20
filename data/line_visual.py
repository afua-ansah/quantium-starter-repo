from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#f4f4f9',
    'text': '#2c3e50'
}

df = pd.read_csv('data/processed_data.csv')
df = df.sort_values(by='date')

fig = px.line(df, x="date", y="sales", title='Sales Over Time',
              labels={'date': 'Date', 'sales': 'Sales Amount (in USD)'})

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sales Prices of Pink Morsel',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)


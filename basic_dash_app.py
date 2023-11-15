import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd


# read in data
data = pd.read_csv(
    "precious_metals_prices_2018_2021.csv"
)

# Crate a plotly figure for use by dcc.Graph()
fig = px.line(
    data,
    x='DateTime',
    y=['Gold'],
    title="Precious Metal Prices 2018-2021",
    color_discrete_map={"Gold": "gold"}
)


app = dash.Dash(__name__)
app.title = "Precious Metal Prices 2018-2021"

app.layout = html.Div(
    id="app-container",
    children=[
        html.Div(
            id="header-area",
            style={"backgroundColor": "black"},
            children=[
                html.H1(
                    id="header-title",
                    children="Precious Metal Prices",
                    style={"color": "white", "fontFamily": "Verdana, sans-serif"}
                ),
                html.P(
                    id="header-description",
                    style={"color": "white",
                           "fontFamily": "Verdana, sans-serif"},
                    children=("The cost of precious metals",
                              html.Br(), "between 2018 and 2021"),
                ),
            ],
        ),
        html.Div(
            id="menu-area",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className="menu-title",
                            children="Metal"
                        ),
                        dcc.Dropdown(
                            id="metal-filter",
                            className="dropdown",
                            options=[{"label": metal, "value": metal}
                                     for metal in data.columns[1:]],
                            clearable=False,
                            value="Gold"
                        ),
                    ]
                ),
            ]
        ),
        html.Div(
            id="graph-container",
            children=dcc.Graph(
                id="price-chart",
                figure=fig,
                config={"displayModeBar": False}
            ),
        ),
    ]
)


@app.callback(
    Output("price-chart", "figure"),
    Input("metal-filter", "value")
)
def update_chart(metal):
    # Crate a plotly figure for use by dcc.Graph()
    fig = px.line(
        data,
        x='DateTime',
        y=[metal],
        title="Precious Metal Prices 2018-2021",
        color_discrete_map={
            "Platinum": "#E5E4E2",
            "Gold": "gold",
            "Silver": "silver",
            "Palladium": "#CED0DD",
            "Rhodium": "#E2E7E1",
            "Iridium": "#3D3C3A",
            "Ruthenium": "#C9CBC8"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title='Date',
        yaxis_title='Price (USD/oz)',
        font=dict(
            family="Verdana, sans-serif",
            size=18,
            color='white'
        )
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)

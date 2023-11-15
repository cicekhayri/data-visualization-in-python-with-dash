import dash
from dash import html
from jinja2 import debug

app = dash.Dash(__name__)

app.layout = html.P("Hello World!")

if __name__ == "__main__":
    app.run_server(debug=True)
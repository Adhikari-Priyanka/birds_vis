import dash
from dash import dcc
from dash import html


app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1('display graph usign html tags!'),
        html.H2('fun fun fun')
    ]
)



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL], use_pages=True, suppress_callback_exceptions=True)
server = app.server

tabs = [
    {"name": "Dashboard", "path": "/"},
    {"name": "Modelos", "path": "/modelos"},
    {"name": "Sobre el proyecto", "path": "/proyecto"},
    {"name": "Indicadores", "path": "/indicadores"}
]

sidebar = html.Div(
    [html.Img(src='assets/logo.png', style={'width': '50%'}),
        dbc.Nav(
            [
                dbc.NavLink(
                    'Dashboard', 
                    href='/', 
                    className="btn btn-secondary", 
                    active="exact",
                    style={'margin-bottom': '10px'}
                ),
                dbc.NavLink(
                    'Análisis exploratorio', 
                    href='/eda', 
                    className="btn btn-secondary", 
                    active="exact",
                    style={'margin-bottom': '10px'}
                ),
                dbc.NavLink(
                    'Modelos', 
                    href='/modelos', 
                    className="btn btn-secondary", 
                    active="exact",
                    style={'margin-bottom': '10px'}
                ),
                dbc.NavLink(
                    'Sobre el proyecto', 
                    href='/proyecto', 
                    className="btn btn-secondary", 
                    active="exact",
                    style={'margin-bottom': '10px'}
                ),
                dbc.NavLink(
                    'Indicadores', 
                    href='/indicadores', 
                    className="btn btn-secondary", 
                    active="exact",
                    style={'margin-bottom': '10px'}
                )
            ],
            vertical=True,
            pills=True,
            className='navbar navbar-expand-lg bg-primary',
            style={'padding': '2%'}
        ),
        html.Div(
            [
                html.P("Valentina Cabrera", className="text-secondary-emphasis text-center"),
                html.P("Valentina Bustamante", className="text-secondary-emphasis text-center")
            ],
            style={
                'text-align': 'center', 'width': '100%'
            }
        )
    ],
    style={
        'position': 'fixed', 'top': 0, 'left': 0, 'bottom': 0,
        'width': '12%', 'padding': '20px', 'background-color': '#f8f9fa',
        'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between',
        'align-items': 'center'
    }
)

content = html.Div(
    [
        html.H4("Predicción de retornos según índice ESG", className="text-center"),
        html.Hr(),
        html.Br(),
        dash.page_container
    ],
    style={'margin-left': '14%', 'padding': '20px'}
)

app.layout = html.Div([sidebar, content])

app.title = 'Proyecto Final'

if __name__ == '__main__':
    app.run_server()

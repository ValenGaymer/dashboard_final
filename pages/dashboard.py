import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('eda_data.csv')

dash.register_page(__name__, path='/', name="dashboard")

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id='variable-selector',
                            className='form-label mt-4',
                            options=[
                            {'label': 'Full Time Employees', 'value': 'Full Time Employees'},
                            {'label': 'Total ESG Risk score', 'value': 'Total ESG Risk score'},
                            {'label': 'Environment Risk Score', 'value': 'Environment Risk Score'},
                            {'label': 'Governance Risk Score', 'value': 'Governance Risk Score'},
                            {'label': 'Social Risk Score', 'value': 'Social Risk Score'},
                            {'label': 'ESG Risk Percentile', 'value': 'ESG Risk Percentile'},
                            {'label': 'Return on Assets (ttm)', 'value': 'Return on Assets (ttm)'},
                            {'label': 'Return on Equity (ttm)', 'value': 'Return on Equity (ttm)'},
                            {'label': 'Return on Investment (ttm)', 'value': 'Return on Investment (ttm)'}
                        ],
                            value='Return on Assets (ttm)',
                            clearable=False,
                            style={'margin-bottom': '20px'}
                        ),

                        dcc.Tabs(
                            id='tabs',
                            value='boxplot',
                            style={'border': 'none'},
                            children=[
                                dcc.Tab(
                                    label='Boxplot',
                                    value='boxplot',
                                    className='m-1',
                                    selected_className='active-tab',
                                    style={
                                        'padding': '10px',
                                        'backgroundColor': '#f8f9fa',
                                        'color': '#333',
                                        'border': 'none'
                                    },
                                    selected_style={
                                        'padding': '10px',
                                        'backgroundColor': '#ec6c64',
                                        'color': 'white',
                                        'border': 'none'
                                    }
                                ),
                                dcc.Tab(
                                    label='Histograma',
                                    value='histogram',
                                    className='m-1',
                                    selected_className='active-tab',
                                    style={
                                        'padding': '10px',
                                        'backgroundColor': '#f8f9fa',
                                        'color': '#333',
                                        'border': 'none'
                                    },
                                    selected_style={
                                        'padding': '10px',
                                        'backgroundColor': '#ec6c64',
                                        'color': 'white',
                                        'border': 'none'
                                    }
                                ),
                            ],
                        ),
                        html.Br(),
                        # Tarjeta de la media
                        dbc.Row(
                            [
                                # Tarjeta de la media
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.Div(
                                                    [
                                                        html.H5("Media", className="card-title text-center"),
                                                        html.P(id='mean-value', className="card-text text-center", style={'font-size': '1rem'})  # Tamaño de fuente más pequeño
                                                    ],
                                                    className='d-flex flex-column align-items-center justify-content-center'  # Centrar contenido
                                                )
                                            ],
                                            style={'padding': '5px'}  # Menor padding en CardBody
                                        ),
                                        className='card text-white bg-dark mb-3',
                                        style={'height': '60px'}  # Altura de la tarjeta
                                    ),
                                    width=6  # Ajustar el ancho de la tarjeta
                                ),

                                # Tarjeta de la desviación estándar
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.Div(
                                                    [
                                                        html.H5("SD", className="card-title text-center"),
                                                        html.P(id='std-value', className="card-text text-center", style={'font-size': '1rem'})  # Tamaño de fuente más pequeño
                                                    ],
                                                    className='d-flex flex-column align-items-center justify-content-center'  # Centrar contenido
                                                )
                                            ],
                                            style={'padding': '5px'}  # Menor padding en CardBody
                                        ),
                                        className='card text-white bg-dark mb-3',
                                        style={'height': '60px'}  # Altura de la tarjeta
                                    ),
                                    width=6  # Ajustar el ancho de la tarjeta
                                )
                            ],
                            justify='between',  # Para espaciar las tarjetas
                            className='mb-3'  # Margen inferior para separación
                        ),

                        dcc.Graph(id='distribution-plot'),
                        dcc.Dropdown(
                            id='x-variable-selector',
                            options=[
                            {'label': 'Full Time Employees', 'value': 'Full Time Employees'},
                            {'label': 'Total ESG Risk score', 'value': 'Total ESG Risk score'},
                            {'label': 'Environment Risk Score', 'value': 'Environment Risk Score'},
                            {'label': 'Governance Risk Score', 'value': 'Governance Risk Score'},
                            {'label': 'Social Risk Score', 'value': 'Social Risk Score'},
                            {'label': 'ESG Risk Percentile', 'value': 'ESG Risk Percentile'},
                            {'label': 'Return on Assets (ttm)', 'value': 'Return on Assets (ttm)'},
                            {'label': 'Return on Equity (ttm)', 'value': 'Return on Equity (ttm)'},
                            {'label': 'Return on Investment (ttm)', 'value': 'Return on Investment (ttm)'}
                        ],
                            value='Return on Assets (ttm)',  # Valor por defecto
                            clearable=False,
                            style={'margin-bottom': '20px'}
                        ),
                        dcc.Graph(id='scatter-plot')
                    ],
                    width=4
                ),
                
                # Segunda columna para el gráfico de barras y selector
                dbc.Col(
                    [
                        html.Br(),
                        dcc.Dropdown(
                            id='categorical-variable-selector',
                            options = [
                            {'label': 'Symbol', 'value': 'Symbol'},
                            {'label': 'Name', 'value': 'Name'},
                            {'label': 'Sector', 'value': 'Sector'},
                            {'label': 'Industry', 'value': 'Industry'},
                            {'label': 'Controversy Level', 'value': 'Controversy Level'},
                            {'label': 'Controversy Score', 'value': 'Controversy Score'},
                            {'label': 'ESG Risk Level', 'value': 'ESG Risk Level'}
                        ],
                            value='Symbol', 
                            clearable=False,
                            style={'margin-bottom': '20px'}
                        ),
                        dcc.Graph(id='bar-chart'),

                        # Tarjeta de valores únicos
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.H5("Valores Únicos", className="card-title text-center"),
                                                html.P(id='unique-values', className="card-text text-center", style={'font-size': '1rem'})  # Tamaño de fuente más pequeño
                                            ],
                                            style={'padding': '5px'}
                                        ),
                                        className='card text-white bg-dark mb-3',
                                        style={'height': '60px'}  # Altura de la tarjeta
                                    ),
                                    width=6
                                ),

                                # Tarjeta para la moda
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.H5("Moda", className="card-title text-center"),
                                                html.P(id='mode-value', className="card-text text-center", style={'font-size': '1rem'})  # Tamaño de fuente más pequeño
                                            ],
                                            style={'padding': '5px'}
                                        ),
                                        className='card text-white bg-dark mb-3',
                                        style={'height': '60px'}
                                    ),
                                    width=6
                                )
                            ],
                            justify='between',
                            className='mb-3'
                        ),
                        dcc.Graph(id='line-chart'),
                        dbc.Row(
                        [
                            # Tarjeta para el valor mínimo
                            dbc.Col(
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H5("Mínimo", className="card-title text-center"),
                                            html.P(id='min-category', className="card-text text-center", style={'font-size': '1rem'}),  # Categoría del valor mínimo
                                            html.P(id='min-value', className="card-text text-center", style={'font-size': '1rem'})  # Valor mínimo
                                        ],
                                        style={'padding': '5px'}
                                    ),
                                    className='card border-primary mb-3',
                                    style={'height': '100px'}  # Altura ajustada
                                ),
                                width=6
                            ),
                            
                            # Tarjeta para el valor máximo
                            dbc.Col(
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H5("Máximo", className="card-title text-center"),
                                            html.P(id='max-category', className="card-text text-center", style={'font-size': '1rem'}),  # Categoría del valor máximo
                                            html.P(id='max-value', className="card-text text-center", style={'font-size': '1rem'})  # Valor máximo
                                        ],
                                        style={'padding': '5px'}
                                    ),
                                    className='card border-primary mb-3',
                                    style={'height': '100px'}  # Altura ajustada
                                ),
                                width=6
                            )
                        ],
                        justify='between',
                        className='mb-3'
                    )
                    ],
                    width=8
                )
            ]
        )
    ]
)



@dash.callback(
    Output('distribution-plot', 'figure'),
    Input('variable-selector', 'value'),
    Input('tabs', 'value')
)
def update_distribution_plot(selected_variable, tab):
    if selected_variable is None:
        selected_variable = 'Return on Assets (ttm)'

    if tab == 'boxplot':
        fig = px.box(df, y=selected_variable, title='',
                     color_discrete_sequence=['#f5a087'])
    else:
        fig = px.histogram(df, x=selected_variable, title='',
                           color_discrete_sequence=['#f5a087'])
    return fig

@dash.callback(
    Output('scatter-plot', 'figure'),
    [Input('variable-selector', 'value'), Input('x-variable-selector', 'value')]
)
def update_scatter_plot(selected_variable, x_variable):
    if selected_variable is None:
        selected_variable = 'Return on Assets (ttm)'

    if x_variable is None:
        x_variable = 'Return on Assets (ttm)'

    fig = px.scatter(df, x=x_variable, y=selected_variable, title=f'{x_variable} vs {selected_variable}',
                     color_discrete_sequence=['#f46f64'])
    return fig

@dash.callback(
    Output('mean-value', 'children'),
    Output('std-value', 'children'),
    Input('variable-selector', 'value')
)
def update_statistics(selected_variable):
    if selected_variable is None:
        selected_variable = 'Return on Assets (ttm)'

    mean_value = df[selected_variable].mean()
    std_value = df[selected_variable].std()
    return f"{mean_value:.2f}", f"{std_value:.2f}"

@dash.callback(
    Output('bar-chart', 'figure'),
    Input('categorical-variable-selector', 'value')
)
def update_bar_chart(selected_category):

    if selected_category is None:
        selected_category = 'Symbol'

    filtered_data = df[selected_category]
    counts = filtered_data.value_counts()

    fig = px.bar(counts, x=counts.index, y=counts.values, labels={'x': 'Categoría', 'y': 'Conteo'}, color_discrete_sequence=['#f5a087'])
    return fig

@dash.callback(
    Output('unique-values', 'children'),
    Output('mode-value', 'children'),
    Input('categorical-variable-selector', 'value')
)
def update_statistics_cat( categorical_variable):
    if categorical_variable is None:
        categorical_variable = 'Symbol'

    unique_count = df[categorical_variable].nunique()
    mode_value = df[categorical_variable].mode()[0]
    
    return unique_count, mode_value


@dash.callback(
    Output('line-chart', 'figure'),
    Input('variable-selector', 'value'),
    Input('categorical-variable-selector', 'value')
)
def update_line_chart(selected_variable, categorical_variable):
    if selected_variable is None:
        selected_variable = 'Return on Assets (ttm)'

    if categorical_variable is None:
        categorical_variable = 'Symbol'


    df_filtered = df.groupby([categorical_variable])[selected_variable].mean().reset_index()

    # Crear el gráfico de líneas
    fig = px.line(df_filtered, x=categorical_variable, y=selected_variable, title=f'{selected_variable} por {categorical_variable}', markers=True, color_discrete_sequence=['#f5a087'])

    # Actualizar el diseño del gráfico
    fig.update_layout(
        xaxis_title=categorical_variable,
        yaxis_title=selected_variable,
        hovermode='x unified',
        template='plotly_white'
    )

    return fig


@dash.callback(
    [Output('min-category', 'children'),
     Output('min-value', 'children'),
     Output('max-category', 'children'),
     Output('max-value', 'children')],
    [Input('categorical-variable-selector', 'value'),
     Input('variable-selector', 'value')]
)
def update_min_max_cards(categorical_variable, selected_variable):

    if categorical_variable is None:
        categorical_variable = 'Symbol'

    if selected_variable is None:
        selected_variable = 'Return on Assets (ttm)'

    # Filtrar los datos para obtener los valores mínimos y máximos
    df_filtered = df.groupby(categorical_variable)[selected_variable].mean().reset_index()

    # Obtener los valores mínimos y máximos
    min_row = df_filtered.loc[df_filtered[selected_variable].idxmin()]
    max_row = df_filtered.loc[df_filtered[selected_variable].idxmax()]

    # Devolver la categoría y el valor mínimo y máximo
    return (min_row[categorical_variable], round(min_row[selected_variable], 2),
            max_row[categorical_variable], round(max_row[selected_variable], 2))
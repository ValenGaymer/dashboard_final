import dash
from dash import dcc, html,dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.subplots as sp
import plotly.graph_objs as go


data = pd.read_csv('eda_data.csv')
print(data)


# GRÁFICAS

sector_counts = data['Sector'].value_counts().reset_index()
sector_counts.columns = ['Sector', 'Frecuencia']
sector = px.bar(sector_counts, x='Sector', y='Frecuencia', title='Frecuencia de Sectores',  color_discrete_sequence=['#f46f64'])

industries_per_sector = data.groupby('Sector')['Industry'].nunique().reset_index()
industries_per_sector.columns = ['Sector', 'Cantidad de Industrias']
industrysector = px.bar(industries_per_sector, x='Sector', y='Cantidad de Industrias', title='Cantidad de Industrias por Sector', color_discrete_sequence=['#f46f64'])

employees = px.box(data, y='Full Time Employees', title='Boxplot de Empleados a Tiempo Completo', color_discrete_sequence=['#f46f64'])

histogram_fig = px.histogram(
    data,
    x='Environment Risk Score',
    barmode='overlay',
    opacity=0.3,
    title='Histograma Superpuesto de Puntuaciones de Riesgo Ambiental, de Gobernanza y Social',
    color_discrete_sequence=['#f46f64']
)
histogram_fig.add_trace(px.histogram(data, x='Governance Risk Score', opacity=0.3, color_discrete_sequence=['#f46f64']).data[0])
histogram_fig.add_trace(px.histogram(data, x='Social Risk Score', opacity=0.3, color_discrete_sequence=['#f46f64']).data[0])
histogram_fig.update_layout(
    xaxis_title='Puntuación de Riesgo',
    yaxis_title='Frecuencia',
    legend_title='Variables',
    barmode='overlay'
)
histogram_fig.for_each_trace(lambda t: t.update(name=t.name.split('=')[-1]))

fig = sp.make_subplots(rows=1, cols=3, subplot_titles=(
    'Correlación: Riesgo Total vs Riesgo Ambiental',
    'Correlación: Riesgo Total vs Riesgo Social',
    'Correlación: Riesgo Total vs Riesgo de Gobernanza'
))


fig.add_trace(
    go.Scatter(
        x=data['Total ESG Risk score'],
        y=data['Environment Risk Score'],
        mode='markers',
        marker=dict(color='#f46f64'),
        name='Puntos',
        
    ),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(
        x=data['Total ESG Risk score'],
        y=data['Social Risk Score'],
        mode='markers',
        marker=dict(color='#f46f64'),
        name='Puntos'
    ),
    row=1, col=2
)
fig.add_trace(
    go.Scatter(
        x=data['Total ESG Risk score'],
        y=data['Governance Risk Score'],
        mode='markers',
        marker=dict(color='#f46f64'),
        name='Puntos'
    ),
    row=1, col=3
)
fig.update_layout(
    title_text='Correlaciones entre Riesgos ESG',
    height=400,  # Altura del gráfico
    width=1500,  # Ancho del gráfico
)

sectorep = data['ESG Risk Level'].value_counts().reset_index()
sectorep.columns = ['Nivel de Riesgo', 'Cantidad de Empresas']

risk_level_fig = px.bar(
    sectorep,
    x='Nivel de Riesgo',
    y='Cantidad de Empresas',
    title='Frecuencia de Cada Nivel de Riesgo',
    color_discrete_sequence=['#f46f64'],
    text='Cantidad de Empresas'
)

plos = px.histogram(
    data,
    x='Total ESG Risk score',
    nbins=30,
    title='Distribución de Puntaje de Riesgo ESG',
    color_discrete_sequence=['#f46f64'],
)

plos.update_layout(
    xaxis_title='Puntuación',
    yaxis_title='Frecuencia',
    height=600,
    template='plotly_white',  # Usar un tema limpio
)


returns = px.box(data_frame=data, 
              y=['Return on Assets (ttm)', 'Return on Equity (ttm)', 'Return on Investment (ttm)'], 
              title='Boxplot de distribución de retornos: ROA, ROE y ROI', color_discrete_sequence=['#f46f64'])


cor_returns = sp.make_subplots(rows=1, cols=3, subplot_titles=(
    'Correlación: ROA vs ROE',
    'Correlación: ROA vs ROI',
    'Correlación: ROE vs ROI'
))

# Añadir trazas para cada subplot
cor_returns.add_trace(
    go.Scatter(
        x=data['Return on Assets (ttm)'],
        y=data['Return on Equity (ttm)'],
        mode='markers',
        marker=dict(color='#f46f64'),
        name='Puntos',
    ),
    row=1, col=1
)

cor_returns.add_trace(
    go.Scatter(
        x=data['Return on Assets (ttm)'],
        y=data['Return on Investment (ttm)'],
        mode='markers',
        marker=dict(color='#f46f64'),
        name='Puntos'
    ),
    row=1, col=2
)

cor_returns.add_trace(
    go.Scatter(
        x=data['Return on Equity (ttm)'],
        y=data['Return on Investment (ttm)'],
        mode='markers',
        marker=dict(color='#f46f64'),
        name='Puntos'
    ),
    row=1, col=3
)

cor_returns.update_layout(
    title_text='Correlaciones entre Retornos',
    height=400,  # Altura del gráfico
    width=1500,  # Ancho del gráfico
)

matriz_correlacion = data[['Return on Assets (ttm)', 'Return on Equity (ttm)', 'Return on Investment (ttm)']].corr()
fig_heatmap = px.imshow(
    matriz_correlacion,
    color_continuous_scale=[
        (0, '#ffffff'),  # blanco
        (0.5, '#f46f64'),  # color medio
        (1, '#bf493f')  # rojo más intenso
    ],
    text_auto=True,
    title='Matriz de Correlación',
)

dash.register_page(__name__)


# CONTENIDOS


esg_content = html.Div([
    html.Br(),
    html.H3('Análisis exploratorio sobre las variables asociadas al índice ESG'),
    html.P(''),

    html.Div(
        dash_table.DataTable(
            id='esg-table',
            columns=[
                {'name': 'Variable', 'id': 'variable'},
                {'name': 'Tipo de dato', 'id': 'data_type'}
            ],
            data=[
                {'variable': 'Symbol', 'data_type': 'categórica'},
                {'variable': 'Name', 'data_type': 'categórica'},
                {'variable': 'Address', 'data_type': 'categórica'},
                {'variable': 'Sector', 'data_type': 'categórica'},
                {'variable': 'Industry', 'data_type': 'categórica'},
                {'variable': 'Full Time Employees', 'data_type': 'categórica'},
                {'variable': 'Description', 'data_type': 'categórica'},
                {'variable': 'Total ESG Risk Score', 'data_type': 'numérica'},
                {'variable': 'Environment Risk Score', 'data_type': 'numérica'},
                {'variable': 'Governance Risk Score', 'data_type': 'numérica'},
                {'variable': 'Social Risk Score', 'data_type': 'numérica'},
                {'variable': 'Controversy Level', 'data_type': 'categórica'},
                {'variable': 'Controversy Score', 'data_type': 'numérica'},
                {'variable': 'ESG Risk Percentile', 'data_type': 'categórica'},
                {'variable': 'ESG Risk Level', 'data_type': 'categórica'},
            ],
            style_table={'overflowX': 'auto',
                         'width': '50%',
                         'margin':'auto'},
            style_cell={
                'textAlign': 'left',
                'padding': '8px',
            },
            style_header={
                'backgroundColor': '#ec6c64',
                'color': 'white',
                'fontWeight': 'bold',
            },
            style_data={
                'backgroundColor': '#f8f9fa',
            },
        ),
        className='table-responsive',
    ), 
    html. Hr(),
    html.H4('Sector'),
    dcc.Graph(
        id='sector-frequency-bar',
        figure=sector
    ),
    html.P('Los sectores predominantes son Industrials (Acciones industriales) y Technology (Tecnología), con frecuencias de 69 y 65 empresas, respectivamente. Por otro lado, se observa que los sectores Energy (Energía), Basic Materials (Materiales básicos), y Communication Services (Servicios de comunicación) tienen frecuencias bastante cercanas entre sí, siendo las más bajas con 20, 21 y 22 empresas, respectivamente. Esto indica que estos sectores son los que presentan menor representación en nuestro conjunto de datos.'),
    html.Br(),
    html.Hr(),
    html.H4('Industrias por sector'),
    dcc.Graph(
        id='industries-per-sector-bar',
        figure=industrysector
    ),
    html.P('Los sectores que presentan mayor diversidad de industrias son Consumer Cyclical (Consumo Cíclico) e Industrials (Acciones Industriales), con un total de 19 y 18 industrias diferentes, respectivamente. Por otro lado, los sectores con menor variabilidad son Communication Services (Servicios de Comunicación) y Energy (Energía), que cuentan únicamente con 5 industrias distintas cada uno. Esto sugiere que, en términos generales, la cantidad de industrias variadas entre los sectores no es considerable, ya que, de un total de 112 industrias, la mayor variabilidad es de solo 19, lo que representa aproximadamente solo un 17% del total.'),
    html.Br(),
    html.Hr(),
    html.H4('Empleados de diempo completo'),
    dcc.Graph(
        id='full-time-employees-boxplot',
        figure=employees
    ),
    html.P('Se observa una gran diferencia entre los valores extremos pues la cantidad mínima de empleados es de 28, mientras que la máxima es de 2100000. Esto sugiere que algunas empresas cuentan con una cantidad de empleados significativamente mayor que las demás, lo que contribuye a la elevada variabilidad de los datos. En cuanto a las medidas de tendencia central, la media es de 61240 con una desviación estándar considerable de 144404, lo que refleja la amplia dispersión en los datos. Esta alta variabilidad podemos decir que se debe a la diferencia entre los valores más altos y bajos. Por ello, la mediana de 22300 empleados, es un indicador más representativo del tamaño típico de las empresas, ya que no se ve tan afectada por los valores extremos. Esto indica que la mayoría de las empresas tienen una cantidad de empleados significativamente menor que la media.'),
    html.Br(),
    html.Hr(),
    html.H4('Puntajes de riesgo'),
    dcc.Graph(
        id='risk-score-hist',
        figure=plos
    ),
    html.P('Las empresas presentan una puntuación de riesgo ESG general en un rango de riesgo medio, con un valor promedio de 21.5 y una desviación estándar de 6.8, lo que indica una variabilidad moderada. Además, el valor mínimo de 7.1 sugiere que al menos una empresa se encuentra dentro de un rango de riesgo insignificante, mientras que el valor máximo de 41.7 indica que existe al menos una compañía con un riesgo severo. Al analizar los cuartiles, se evidencia que, a gran escala, las empresas están relativamente bien posicionadas, ya que el 75% de ellas tiene una puntuación de 26 o inferior. Esto implica que la mayoría de las empresas no sobrepasan el umbral de riesgo medio y se encuentran considerablemente alejadas de los puntajes más elevados, lo que sugiere una gestión efectiva de los riesgos ESG en la mayoría de estas compañías.'),
    dcc.Graph(
        id='risk-scores-histogram',
        figure=histogram_fig
    ),
    html.P('En nuestro conjunto de datos, el promedio del puntaje de riesgo ambiental de las compañías es de 5.7, con una desviación estándar de 5. Esto indica que, en general, el riesgo ambiental se encuentra dentro de la categoría de riesgo insignificante. Es importante destacar que hay al menos una compañía con un puntaje de 0, lo que refleja un manejo ambiental perfecto y la ausencia de impactos negativos. Además, el puntaje máximo registrado en este conjunto de datos es de 25, lo que sugiere que ninguna empresa supera el riesgo medio según la escala de clasificación establecida. Asimismo, podemos afirmar que la mayoría de las compañías presentan un riesgo ambiental insignificante, ya que el 75% de los puntajes es menor o igual a 8.8. '),
    html.P('Para el componente de gobernanza de las empresas, hemos encontrado que el puntaje promedio es de 6.72, con una desviación estándar de 2.21. Esto indica que, en general, las compañías se encuentran dentro del rango de riesgo insignificante. Esto se ve respaldado por los valores del segundo y tercer cuartil, que son de 6.1 y 7.6, respectivamente. Esto sugiere que la mayoría de los puntajes de gobernanza se agrupan en torno a niveles que indican un riesgo insignificante. Sin embargo, es importante señalar que no todas las empresas presentan pertencen a este rango, ya que el puntaje máximo registrado es de 19.4, lo que implica que al menos una compañía tiene un puntaje que la clasifica en el rango de riesgo medio.'),
    html.P('En promedio, el puntaje de riesgo social de las compañías incluidas en este estudio es de 9, con una desviación estándar de 3.6. Esto sugiere una variabilidad moderada en los puntajes de riesgo social entre las empresas analizadas. El puntaje mínimo registrado es de 0.8, mientras que el puntaje máximo alcanza 22.5. Esto indica que algunas empresas se encuentran en la categoría de riesgo insignificante, mientras que otras presentan un riesgo más significativo, clasificándose en el rango de riesgo medio. Además, observamos que el 75% de las empresas tiene un puntaje igual o inferior a 11.2. Esto implica que también hay al menos una compañía que se sitúa en un nivel de riesgo bajo.'),
    dcc.Graph(
        id='esg-risk-correlations',
        figure=fig
    ),
    html.Br(),
    html.H5('Niveles de riesgo'),
    dcc.Graph(
        id='esg-risk-level',
        figure=risk_level_fig
    ),
    html.P('Podemos observar que la mayoría de las compañías se concentran en los niveles de riesgo Medium (medio o moderado) y Low (bajo), con 180 y 178 empresas respectivamente. Esto sugiere que, en general, las empresas están iniciando o ya han implementado mejoras en sus estrategias relacionadas con la sostenibilidad y la gestión de riesgos ESG. En contraste, los demás niveles de riesgo, como High (alto), Negligible (insignificante) y Severe (severo), presentan frecuencias considerablemente más bajas en comparación con los dos predominantes, lo que refuerza la tendencia hacia una gestión más responsable y consciente de los riesgos ambientales y sociales.'),

])

financial_content = html.Div([
    html.Br(),
    html.H3('Análisis exploratorio sobre las variables asociadas a retornos'),
    html.P(''),
    html.P('El dataset utilizado contiene una amplia gama de indicadores financieros clave de empresas que forman parte del índice S&P500. Incluye información fundamental, como la capitalización de mercado, ingresos, y utilidades, junto con ratios financieros esenciales como el P/E (precio a ganancias), P/B (precio a valor en libros), y P/S (precio a ventas). Además, el dataset abarca datos de rendimiento a corto y largo plazo, indicadores de rentabilidad como ROA (retorno sobre activos) y ROE (retorno sobre capital), y variables relacionadas con la actividad en el mercado, como el interés corto y la volatilidad. Este conjunto de datos es ideal para analizar tanto el desempeño financiero como el comportamiento en el mercado de las principales empresas del S&P500, ofreciendo una visión integral de su situación económica, liquidez, y perspectivas de crecimiento. Debido al objetivo de este proyecto, se hará enfoque especial en indicadores como ROE, ROA y ROI.'),
    dcc.Graph(
        figure=returns
    ),
    html.P('En promedio, las empresas generan un retorno del 7.35% sobre sus activos, un 17.68% sobre su capital y un 15.16% sobre sus inversiones. Sin embargo, la desviación estándar revela una gran variabilidad, especialmente en el ROE, que tiene una desviación estándar del 82.47%, sugiriendo que hay diferencias significativas en la capacidad de las empresas para generar ganancias en relación con su capital. En cuanto a los percentiles, el 25% de las empresas tiene un ROA menor a 2.60%, mientras que el 75% tiene un ROA mayor a 11.60%, lo que indica que aunque hay empresas con bajos retornos, también hay aquellas que están muy bien gestionadas. Por otro lado, los valores máximos son impresionantes: un ROA máximo de 37.40%, un ROE de 924.90% y un ROI de 326.40% sugieren que hay empresas que han logrado un desempeño excepcional. Acá se puede notar la presencia de datos atípicos, siendo más extremos en ROE, esto esperado dado lo observado en el resumen estadístico. Estos datos extremos, corresponden a un retorno sobre el capital del -850% para Seagate Technology Holdings plc (STX), empresa estadounidense de almacenamiento de dato, lo que indica que la empresa no solo no está siendo rentable, sino que está perdiendo una cantidad significativa de dinero en comparación con el capital que tienen invertido los accionistas; y a un 924.90% de ROE para APA Corporation (APA), el holding de Apache Corporation, una empresa estadounidense dedicada a la exploración de hidrocarburos, lo que sugiere que la empresa está generando ingresos netos extremadamente altos en relación con el capital aportado por los accionistas (patrimonio neto)'),
    dcc.Graph(
        figure=cor_returns
    ),
    html.P('No parece haber una relación lineal entre ROA y ROE ni entre ROI y ROE, sin embargo, sí que parece haber una especie de correlación positiva entre ROA y ROI.'),
    dcc.Graph(
        figure=fig_heatmap
    ),
    html.P('Esto se confirma con la matriz de correlación, donde ROA y ROI cuentan con un coeficiente de correlación de 0.65.')
])




# DASH

layout = html.Div([
    dcc.Tabs(
        id='tabs',
        value='esg',  # Valor inicial
        style={'border': 'none'},
        children=[
            dcc.Tab(
                label='ESG',
                value='esg',
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
                label='Financial',
                value='financial',
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
    html.Div(id='tabs-content'),
])

@dash.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)

def render_content(tab):
    if tab == 'esg':
        return esg_content
    elif tab == 'financial':
        return financial_content
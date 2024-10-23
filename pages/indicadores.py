import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


dash.register_page(__name__)

variables_num = [
    {'label': 'Full Time Employees', 'value': 'Número total de empleados a tiempo completo.'},
    {'label': 'Total ESG Risk score', 'value': 'Puntuación total de riesgo ESG (Environmental, Social, Governance).'},
    {'label': 'Environment Risk Score', 'value': 'Puntuación de riesgo ambiental.'},
    {'label': 'Governance Risk Score', 'value': 'Puntuación de riesgo de gobernanza.'},
    {'label': 'Social Risk Score', 'value': 'Puntuación de riesgo social.'},
    {'label': 'ESG Risk Percentile', 'value': 'Percentil de riesgo ESG comparado con otras empresas.'},
    {'label': 'Return on Assets (ttm)', 'value': 'Retorno sobre activos, indica la rentabilidad de una empresa en relación con su activo total'},
    {'label': 'Return on Equity (ttm)', 'value': 'Retorno sobre patrimonio neto, mide la capacidad que tiene una empresa de dar una remuneración a un inversor.'},
    {'label': 'Return on Investment (ttm)', 'value': 'Retorno sobre inversión, mide rendimiento económico de una inversión en relación con su coste'},
]

variables_cat = [
    {'label': 'Symbol', 'value': 'Símbolo de la acción en el mercado.'},
    {'label': 'Name', 'value': 'Nombre de la empresa.'},
    {'label': 'Sector', 'value': 'Sector al que pertenece la empresa.'},
    {'label': 'Industry', 'value': 'Industria específica de la empresa.'},
    {'label': 'Controversy Level', 'value': 'Nivel de controversia asociado a la empresa.'},
    {'label': 'Controversy Score', 'value': 'Puntuación de controversia de la empresa.'},
    {'label': 'ESG Risk Level', 'value': 'Nivel de riesgo ESG de la empresa.'}
]

def create_card_num(variable):
    return html.Div(
        className='card border-primary mb-3',
        children=[
            html.H5(variable['label'], className='card-header'),
            html.P(variable['value'], className='card-text')
        ],
        style={
            'border': '1px solid #ccc', 
            'border-radius': '5px', 
            'padding': '10px', 
            'margin': '10px', 
            'width': '18%', 
            'display': 'inline-block', 
            'vertical-align': 'top'
        }
    )

def create_card_cat(variable):
    return html.Div(
        className='card border-danger mb-3',
        children=[
            html.H5(variable['label'], className='card-header'),
            html.P(variable['value'], className='card-text')
        ],
        style={
            'border': '1px solid #ccc', 
            'border-radius': '5px', 
            'padding': '10px', 
            'margin': '10px', 
            'width': '18%', 
            'display': 'inline-block', 
            'vertical-align': 'top'
        }
    )

layout = html.Div([
    html.H3('Conoce un poco de las variables involucradas en los modelos', style={'text-align': 'center'}),
    html.H3('Numéricas', className= 'btn btn-dark disabled'),
    html.Div(
        children=[create_card_num(variable) for variable in variables_num], 
        style={'text-align': 'center'}
    ),
    html.H3('Categóricas', className= 'btn btn-dark disabled'),
     html.Div(
        children=[create_card_cat(variable) for variable in variables_cat], 
        style={'text-align': 'center'}
    ),
])


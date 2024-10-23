import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


dash.register_page(__name__)

layout = html.Div([
    html.H1('Sobre el proyecto', className='text-center'),  # Centrar el título
    html.P([
        'El análisis de los índices ESG ',
        html.Span('(Environmental, Social, and Governance)', className='badge rounded-pill bg-primary'),
        ' podría ofrecer una perspectiva valiosa sobre la relación entre las prácticas sostenibles y la presencia de las empresas en el mercado, así como en indicadores financieros clave. Al observar el desempeño en áreas como el impacto ambiental, la responsabilidad social y la gobernanza, se espera identificar posibles patrones que sugieran si las empresas con puntajes más altos en ESG tienden a tener una ventaja competitiva. Esto podría reflejarse en su capacidad para atraer inversores, mantener su crecimiento, o mejorar su rentabilidad a través de métricas como el ROI o los márgenes de utilidad.'
    ], className='text-justify', style={'max-width': '800px', 'margin': '0 auto'}),
    
    html.Br(), html.Br(),
    
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5('¿Indicadores financieros?', className="card-title text-center"),
                    html.P('Los indicadores financieros como la capitalización de mercado, los retornos y los márgenes son esenciales para entender el desempeño y la posición competitiva de una empresa en el mercado.', className="card-text text-center"),
                    html.P('Estos indicadores proporcionan una visión integral del estado financiero de una empresa, ayudando a los inversores a evaluar su rentabilidad, eficiencia y estabilidad en el mercado.', className="card-text text-center")
                ], style={'padding': '10px'}), className='card border-primary mb-3'
            ), width=4
        ),

        dbc.Col([
            html.P([
                'El objetivo de este proyecto es ', 
                html.Span('analizar el índice ESG (Environmental, Social, and Governance) para determinar si existe una relación directa entre las prácticas sostenibles de las empresas y su presencia en el mercado', className='text-primary'), 
                '. Se busca evaluar si un mejor desempeño en áreas como el impacto ambiental, la responsabilidad social y la gobernanza corporativa influye en factores clave como la atracción de inversiones, la reducción de riesgos operativos y la mejora de la reputación empresarial.'
            ], className='text-justify', style={'max-width': '600px', 'margin': '0 auto'})
        ], width=8)
    ], justify='between', className='mb-3')
], style={'max-width': '1200px', 'margin': '0 auto'}) 

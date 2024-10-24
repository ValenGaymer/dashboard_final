import dash
from dash import dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

roa = {
    "Modelo": ["KNN", "Regresión lineal", "Ridge", "Lasso"],
    "Mean Squared Error (MSE)": [6.052576e-03, 2.901403e+24, 5.714636e-03, 6.704687e-03],
    "Root Mean Squared Error (RMSE)": [7.779830e-02, 1.703350e+12, 7.559521e-02, 8.188215e-02],
    "Mean Absolute Error (MAE)": [5.599819e-02, 4.934784e+11, 5.386722e-02, 5.931734e-02],
    "R2 score": [7.629148e-02, -4.427950e+26, 1.278659e-01, -2.322988e-02],
    "Ljung-Box (p-value)": [0.206972, 0.997864, 0.311085, 0.746134],
    "Jarque-Bera (p-value)": [3.569842e-04, 0.000000e+00, 5.347736e-08, 1.386132e-09]
}
roa = pd.DataFrame(roa)


roe = {
    "Modelo": ["KNN", "Regresión lineal", "Ridge", "Lasso"],
    "Mean Squared Error (MSE)": [1.141760e+00, 9.294386e+26, 1.183243e+00, 1.148228e+00],
    "Root Mean Squared Error (RMSE)": [1.068532e+00, 3.048670e+13, 1.087770e+00, 1.071554e+00],
    "Mean Absolute Error (MAE)": [3.827261e-01, 9.470263e+12, 4.484291e-01, 3.590545e-01],
    "R2 score": [-5.708837e-03, -8.186874e+26, -4.224847e-02, -1.140641e-02],
    "Ljung-Box (p-value)": [0.963556, 0.851248, 0.961167, 0.910609],
    "Jarque-Bera (p-value)": [0.000000e+00, 4.300458e-148, 0.000000e+00, 0.000000e+00]
}
roe = pd.DataFrame(roe)

roi = {
    "Modelo": ["KNN", "Regresión lineal", "Ridge", "Lasso"],
    "Mean Squared Error (MSE)": [9.118282e-02, 1.347561e+25, 8.986472e-02, 1.068428e-01],
    "Root Mean Squared Error (RMSE)": [3.019649e-01, 3.670914e+12, 2.997745e-01, 3.268682e-01],
    "Mean Absolute Error (MAE)": [1.134780e-01, 1.115009e+12, 1.188022e-01, 1.299803e-01],
    "R2 score": [1.376146e-01, -1.274491e+26, 1.500809e-01, -6.212029e-03],
    "Ljung-Box (p-value)": [0.993825, 0.519615, 0.987171, 0.947695],
    "Jarque-Bera (p-value)": [0.000000e+00, 9.660907e-182, 0.000000e+00, 0.000000e+00]
}
roi = pd.DataFrame(roi)


dash.register_page(__name__)

layout = html.Div([
    html.H2('Modelos'),
    dcc.Dropdown(
        id='model-dropdown',
        options=[
            {'label': 'ROA', 'value': 'ROA'},
            {'label': 'ROE', 'value': 'ROE'},
            {'label': 'ROI', 'value': 'ROI'}
        ],
        value='ROA',  # Default value
        clearable=False
    ),
    html.Div(id='model-content')
])

@dash.callback(
    Output('model-content', 'children'),
    [Input('model-dropdown', 'value')]
)
def update_model_content(selected_model):
    if selected_model == 'ROA':
        return html.Div([
            html.Br(),
            html.H3('ROA'),
            html.Br(),
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in roa.columns],
                data=roa.to_dict('records'),
                style_cell={'width': '80px', 'textAlign': 'center'},
                style_table={'overflowX': 'auto'},
            ),
            html.Br(),
            html.P('En resumen, KNN, Ridge y Lasso muestran buen rendimiento con bajos errores (MSE, RMSE y MAE), aunque los residuos no siguen una distribución normal según la prueba de Jarque-Bera. La Regresión Lineal tiene un rendimiento muy deficiente, con errores extremadamente altos, lo que indica que no es adecuada para este problema. No hay autocorrelación significativa en los residuos de ninguno de los modelos, lo que es positivo.'),
            html.Img(src='assets/roa.png', style={'width': '100%', 'height': 'auto', 'display': 'block', 'margin': 'auto'}),
        ])
    elif selected_model == 'ROE':
        return html.Div([
            html.Br(),
            html.H3('ROE'),
            html.Br(),
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in roe.columns],
                data=roe.to_dict('records'),
                style_cell={'width': '80px', 'textAlign': 'center'},
                style_table={'overflowX': 'auto'},
            ),
            html.Br(),
            html.P('En esta tabla, se observa que  los valores de MSE, RMSE y MAE sugieren que los modelos están teniendo dificultades para ajustarse adecuadamente a los datos. El modelo de Regresión Lineal tiene un MSE y MAE demasiado altos, indicando predicciones muy erróneas, mientras que los modelos KNN, Ridge y Lasso tienen errores más moderados, pero aún muestran un desempeño deficiente, especialmente en términos de R²,  donde todos están alejados de 1 y además hay algunos negativos. En resumen, todos los modelos parecen estar ajustándose muy mal a los datos, lo que sugiere que podría haber problemas en los datos, o bien, estos modelos no son los más adecuados para el problema en cuestión.'),
            html.Img(src='assets/roe.png', style={'width': '100%', 'height': 'auto', 'display': 'block', 'margin': 'auto'}),
        ])
    elif selected_model == 'ROI':
        return html.Div([
            html.Br(),
            html.H3('ROI'),
            html.Br(),
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in roi.columns],
                data=roi.to_dict('records'),
                style_cell={'width': '80px', 'textAlign': 'center'},
                style_table={'overflowX': 'auto'},
            ),
            html.Br(),
            html.P('En esta tabla, se observa que  los valores de MSE, RMSE y MAE sugieren que los modelos y los datos no se ajustan tan bien entre sí. El modelo de Regresión Lineal tiene un MSE y MAE extremadamente altos, indicando predicciones desastrosamente erróneas, mientras que los modelos KNN, Ridge y Lasso tienen errores más moderados, pero aún muestran un desempeño deficiente, especialmente en términos de R². En resumen, todos los modelos parecen estar ajustándose muy mal a los datos, lo que sugiere que podría haber problemas en los datos, o bien, estos modelos no son los más adecuados para el problema en cuestión.'),
            html.Img(src='assets/roi.png', style={'width': '100%', 'height': 'auto', 'display': 'block', 'margin': 'auto'}),
        ])

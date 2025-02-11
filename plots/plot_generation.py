import matplotlib.pyplot as plt

# Esta classe é para consolidar os modelos gráficos que pretendo criar 
class Visualization:
    
    @staticmethod
    def plot_multiple_lines(data_list, x_col, y_col, labels, colors, title='Gráfico de Linha', xlabel='Data', ylabel='Valor'):
        """Gráfico de linha para múltiplos conjuntos."""
        plt.figure(figsize=(12, 6))
        
        for data, label, color in zip(data_list, labels, colors):
            plt.plot(data[x_col], data[y_col], label=label, color=color)
        
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

def plot_forecast(forecast, x_col='ds', y_col='yhat', title='Previsões para o Preço do Petróleo'):
    """
    Função para plotar previsões com intervalo de confiança.

    Parâmetros:
    - forecast: DataFrame com os dados das previsões.
    - x_col: Nome da coluna para o eixo x (datas).
    - y_col: Nome da coluna para o eixo y (valores previstos).
    - title: Título do gráfico.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(forecast[x_col], forecast[y_col], label='Previsões', color='blue')
    
    plt.fill_between(
        forecast[x_col], 
        forecast['yhat_lower'], 
        forecast['yhat_upper'], 
        color='gray', alpha=0.2, label='Intervalo de Confiança'
    )
    
    plt.title(title)
    plt.xlabel('Data')
    plt.ylabel('Valor da Cotação')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def plot_real_vs_forecast(comparison, title='Comparação entre Valores Reais e Previstos'):
    """
    Plota a comparação entre valores reais e previstos.

    Parâmetros:
    - comparison: DataFrame com colunas ['ds', 'Real', 'Previsto'].
    - title: Título do gráfico.
    """
    plt.figure(figsize=(20, 6))
    plt.plot(comparison['ds'], comparison['Real'], label='Valores Reais', color='blue')
    plt.plot(comparison['ds'], comparison['Previsto'], label='Valores Previstos', color='orange')
    
    plt.title(title)
    plt.xlabel('Data')
    plt.ylabel('Valor da Cotação')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()


def plot_forecast_with_history(train_data, forecast, x_col='ds', y_col='yhat', title='Previsões e Dados Históricos'):
    """
    Plota dados históricos e previsões com intervalo de confiança.

    Parâmetros:
    - train_data: DataFrame com os dados históricos ['ds', 'y'].
    - forecast: DataFrame com os dados de previsão ['ds', 'yhat', 'yhat_lower', 'yhat_upper'].
    - x_col: Coluna com datas (default 'ds').
    - y_col: Coluna com valores previstos (default 'yhat').
    - title: Título do gráfico.
    """
    plt.figure(figsize=(20, 6))

    # Dados históricos
    plt.plot(train_data[x_col], train_data['y'], label='Dados Históricos', color='blue')

    # Previsões
    plt.plot(forecast[x_col], forecast[y_col], label='Previsões (2025 em diante)', color='orange')

    # Intervalo de Confiança
    if 'yhat_lower' in forecast and 'yhat_upper' in forecast:
        plt.fill_between(forecast[x_col], forecast['yhat_lower'], forecast['yhat_upper'], 
                         color='gray', alpha=0.2, label='Intervalo de Confiança 80%')

    plt.xlabel('Data')
    plt.ylabel('Valor da Cotação')
    plt.title(title)
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

class ModelEvaluation:
    def __init__(self, test_data, forecast):
        """
        Classe para validar a performance do modelo.
        
        Args:
        - test_data: DataFrame contendo dados reais com colunas 'ds' e 'y'.
        - forecast: DataFrame contendo previsões com colunas 'ds' e 'yhat'.
        """
        # Verificando se as colunas necessárias estão presentes
        required_columns_test = ['ds', 'y']
        required_columns_forecast = ['ds', 'yhat']
        
        if not all(col in test_data.columns for col in required_columns_test):
            raise ValueError(f"Test data must contain columns {required_columns_test}")
        if not all(col in forecast.columns for col in required_columns_forecast):
            raise ValueError(f"Forecast data must contain columns {required_columns_forecast}")
        
        # Remover valores nulos
        self.test_data = test_data[['ds', 'y']].dropna()
        self.forecast = forecast[['ds', 'yhat']].dropna()
        
        # Garantindo que a comparação seja feita com dados limpos
        self.comparison = self._merge_data()

    def _merge_data(self):
        """
        Combina os dados reais e previstos com base na coluna 'ds'.
        """
        return pd.merge(self.test_data, self.forecast, on='ds', how='inner')

    def calculate_mae(self):
        """
        Calcula o Erro Absoluto Médio (MAE).
        """
        mae = mean_absolute_error(self.comparison['y'], self.comparison['yhat'])
        return mae

    def calculate_rmse(self):
        """
        Calcula o Erro Quadrático Médio (RMSE).
        """
        rmse = np.sqrt(mean_squared_error(self.comparison['y'], self.comparison['yhat']))
        return rmse

    def calculate_mape(self):
        """
        Calcula o Erro Absoluto Percentual Médio (MAPE).
        """
        # Evitando divisão por zero
        with np.errstate(divide='ignore', invalid='ignore'):
            mape = np.mean(np.abs((self.comparison['y'] - self.comparison['yhat']) / self.comparison['y'])) * 100
        return mape

    def evaluate(self):
        """
        Realiza a avaliação do modelo e imprime as métricas.
        """
        mae = self.calculate_mae()
        rmse = self.calculate_rmse()
        mape = self.calculate_mape()

        print(f"Erro Absoluto Médio (MAE): {mae}")
        print(f"Erro Quadrático Médio (RMSE): {rmse}")
        print(f"Erro Absoluto Percentual Médio (MAPE): {mape:.2f}%")

        return {
            'MAE': mae,
            'RMSE': rmse,
            'MAPE': mape
        }

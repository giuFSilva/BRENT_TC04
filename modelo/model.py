from prophet import Prophet
import pandas as pd

class ProphetPipeline:
    def __init__(self, yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False):
        self.model = Prophet(
            yearly_seasonality=yearly_seasonality,
            weekly_seasonality=weekly_seasonality,
            daily_seasonality=daily_seasonality,
            changepoint_prior_scale=0.3,
            seasonality_mode='multiplicative',
            interval_width=0.70
        )
        self.holidays_df = pd.DataFrame()

    # Função para dividir os dados
    def split_data(self, data, train_end_date, test_start_date):
        """Divide os dados em treino e teste."""
        self.train_data = data[data['ds'] <= train_end_date].copy()
        self.test_data = data[data['ds'] >= test_start_date].copy()
        return self.train_data, self.test_data

    # Função para adicionar eventos
    def add_event(self, holiday_name, event_dates, lower_window, upper_window):
        """Adiciona eventos históricos à lista de feriados."""
        event_df = pd.DataFrame({
            'holiday': holiday_name,
            'ds': pd.to_datetime(event_dates),
            'lower_window': lower_window,
            'upper_window': upper_window
        })
        self.holidays_df = pd.concat([self.holidays_df, event_df], ignore_index=True)

    def create_holidays_df(self):
        """Remove duplicatas no DataFrame de eventos."""
        self.holidays_df.drop_duplicates(inplace=True)
        return self.holidays_df

    # Adicionando eventos e configurando o modelo
    def configure_model(self):
        """Configura o modelo com feriados e sazonalidades personalizadas."""
        if not self.holidays_df.empty:
            self.model.holidays = self.holidays_df
        self.model.add_seasonality(name='yearly', period=365.25, fourier_order=10)
        self.model.add_seasonality(name='monthly', period=30.5, fourier_order=5)

    # Treinamento do modelo
    def fit_model(self):
        """Treina o modelo Prophet com os dados de treino."""
        if not self.holidays_df.empty:
            self.train_data['holiday'] = self.train_data['ds'].isin(self.holidays_df['ds']).astype(int)
        self.model.fit(self.train_data)

    # Previsões
    def predict(self, periods=None, freq='D'):
        """Realiza a previsão para os próximos períodos com base no teste."""
        if periods is None:
            periods = len(self.test_data)
        future = self.model.make_future_dataframe(periods=periods, freq=freq)  # Use freq aqui
        if not self.holidays_df.empty:
            future['holiday'] = future['ds'].isin(self.holidays_df['ds']).astype(int)
        forecast = self.model.predict(future)
        return forecast

import joblib 
joblib.dump(Prophet, 'Model_Prophet')
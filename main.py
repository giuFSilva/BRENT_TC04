import pandas as pd
import joblib
from datetime import datetime
from utils.utils import DataPipeline
from modelo.model import ProphetPipeline
from utils.helpers import ModelEvaluation
from plots.plot_generation import plot_real_vs_forecast, plot_forecast_with_history, plot_forecast

# ==============================
# 🔹 Função para carregar e processar os dados
# ==============================
def carregar_dados(file_path):
    try:
        data_pipeline = DataPipeline(file_path=file_path)
        df = data_pipeline.load_data()
        return data_pipeline.preprocess()
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

# ==============================
# 🔹 Função para configurar e treinar o modelo Prophet
# ==============================
def treinar_modelo(df, train_end_date, test_start_date):
    try:
        prophet_pipeline = ProphetPipeline()

        # Dividir os dados
        train_data, test_data = prophet_pipeline.split_data(df, train_end_date, test_start_date)

        # Adicionar eventos históricos
        eventos = [
            ("Pandemia COVID-19", ['2020-03-11', '2020-04-01'], -7, 30),
            ("Guerra Rússia-Ucrânia", ['2022-02-24'], 0, 10),
            ("Crise Financeira Global 2008", ['2008-09-15'], -10, 10),
            ("Queda de Preços do Petróleo", ['2014-06-01', '2015-01-01', '2016-01-01'], -30, 30),
            ("Ataque às instalações da Arábia Saudita", ['2019-09-14'], -1, 2),
        ]
        for nome, datas, impacto_neg, impacto_pos in eventos:
            prophet_pipeline.add_event(nome, datas, impacto_neg, impacto_pos)

        # Criar DataFrame de feriados e configurar o modelo
        holidays_df = prophet_pipeline.create_holidays_df()
        prophet_pipeline.configure_model()

        # Adicionar feriados ao conjunto de treino
        train_data = train_data.merge(holidays_df[['ds', 'holiday']], on='ds', how='left').fillna(0)

        # Treinar o modelo
        prophet_pipeline.fit_model()
        joblib.dump(prophet_pipeline.model, 'Model_Prophet.joblib')

        return prophet_pipeline, train_data, test_data, holidays_df
    except Exception as e:
        print(f"Erro ao treinar o modelo: {e}")
        return None, None, None, None

# ==============================
# 🔹 Função para prever e avaliar o modelo
# ==============================
def prever_e_avaliar(prophet_pipeline, test_data, holidays_df):
    try:
        # Gerar previsões
        forecast = prophet_pipeline.predict(periods=len(test_data), freq='D')

        # Comparação entre dados reais e previsão
        comparison = test_data.merge(forecast[['ds', 'yhat']], on='ds', how='inner')
        comparison.rename(columns={'y': 'Real', 'yhat': 'Previsto'}, inplace=True)

        # Avaliar modelo
        evaluation = ModelEvaluation(test_data, forecast)
        results = evaluation.evaluate()

        return forecast, comparison, results
    except Exception as e:
        print(f"Erro na previsão e avaliação: {e}")
        return None, None, None

# ==============================
# 🔹 Função para prever o futuro (até 2027)
# ==============================
def prever_futuro(prophet_pipeline, holidays_df, forecast):
    try:
        end_date = datetime(2027, 12, 31)
        last_date = forecast['ds'].max()
        days_until_2027 = (end_date - last_date).days

        # Criar DataFrame de previsões futuras
        future_dates = prophet_pipeline.model.make_future_dataframe(periods=days_until_2027, freq='D')
        future_dates = future_dates.merge(holidays_df[['ds', 'holiday']], on='ds', how='left').fillna(0)

        # Gerar previsões para 2025-2027
        forecast_2025 = prophet_pipeline.model.predict(future_dates)

        return forecast_2025
    except Exception as e:
        print(f"Erro ao prever o futuro: {e}")
        return None

# ==============================
# 🔹 Execução do Script
# ==============================
if __name__ == "__main__":
    file_path = "C:\\Users\\giuliasilva\\Desktop\\Estudo\\POS\\TC - Modulo 04\\Projeto_Teste\\data\\Base_IPEA.csv"

    # Carregar os dados
    df = carregar_dados(file_path)
    if df is None:
        exit()

    # Treinar modelo
    prophet_pipeline, train_data, test_data, holidays_df = treinar_modelo(df, '2023-12-31', '2024-01-01')
    if prophet_pipeline is None:
        exit()

    # Gerar previsões e avaliar modelo
    forecast, comparison, results = prever_e_avaliar(prophet_pipeline, test_data, holidays_df)
    if forecast is None:
        exit()

    # Gerar previsões futuras (2025-2027)
    forecast_2025 = prever_futuro(prophet_pipeline, holidays_df, forecast)
    if forecast_2025 is None:
        exit()

    # ==============================
    # 🔹 Exibir resultados
    # ==============================
    print(f"Tamanho do treino: {len(train_data)}")
    print(f"Tamanho do teste: {len(test_data)}")
    print(f"Tamanho da previsão: {len(forecast)}")
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

    # ==============================
    # 🔹 Gerar gráficos
    # ==============================
    plot_forecast(forecast, title='Previsões Ibovespa para o Brent')
    plot_real_vs_forecast(comparison)
    plot_forecast_with_history(train_data, forecast_2025, title='Previsões e Dados Históricos (2025 em diante)')

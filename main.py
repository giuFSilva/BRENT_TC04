from utils.utils import DataPipeline
from modelo.model import ProphetPipeline
from utils.helpers import ModelEvaluation
from plots.plot_generation import plot_real_vs_forecast, plot_forecast_with_history, plot_forecast

import pandas as pd
from datetime import datetime

# Carregar e processar os dados
file_path = "C:\\Users\\giuliasilva\\Desktop\\Estudo\\POS\\TC - Modulo 04\\Projeto_Teste\\data\\Base_IPEA.csv"
data_pipeline = DataPipeline(file_path=file_path)
df = data_pipeline.load_data()
df = data_pipeline.preprocess()

# Dividir os dados para treino e teste
train_end_date = '2020-12-31'
test_start_date = '2021-01-01'

# Instanciar o modelo Prophet
prophet_pipeline = ProphetPipeline()

# Dividir os dados
train_data, test_data = prophet_pipeline.split_data(df, train_end_date, test_start_date)

# Adicionar eventos históricos (antes de treinar o modelo)
prophet_pipeline.add_event('Pandemia COVID-19', ['2020-03-11', '2020-04-01'], -7, 30)
prophet_pipeline.add_event('Guerra Rússia-Ucrânia', ['2022-02-24'], 0, 10)
prophet_pipeline.add_event('Crise Financeira Global 2008', ['2008-09-15'], -10, 10)
prophet_pipeline.add_event('Queda de Preços do Petróleo', ['2014-06-01', '2015-01-01', '2016-01-01'], -30, 30)
prophet_pipeline.add_event('Ataque às instalações da Arábia Saudita', ['2019-09-14'], -1, 2)

# Criar o DataFrame de feriados e eventos
holidays_df = prophet_pipeline.create_holidays_df()

# Configuração do modelo
prophet_pipeline.configure_model()

# Adicionar a coluna 'holiday' à base de treino antes de treinar o modelo
train_data['holiday'] = train_data['ds'].apply(
    lambda x: 1 if x in holidays_df['ds'].values else 0
)

# Treinar o modelo
prophet_pipeline.fit_model()

# Garantir que o período do forecast seja do mesmo tamanho da base de teste
forecast = prophet_pipeline.predict(periods=len(test_data), freq='D')

# Exibir os tamanhos para validação
print(f"Tamanho do treino: {len(train_data)}")
print(f"Tamanho do teste: {len(test_data)}")
print(f"Tamanho da previsão: {len(forecast)}")

# Exibir as previsões
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Exemplo de chamada para o plot das previsões
plot_forecast(forecast, title='Previsões Ibovespa para o Brent')

# Criação e avaliação do modelo
evaluation = ModelEvaluation(test_data, forecast)
results = evaluation.evaluate()  # Isso gera as métricas e imprime

# Mesclar previsões com dados reais
comparison = pd.merge(test_data, forecast[['ds', 'yhat']], on='ds', how='inner')

# Renomear as colunas para facilitar a interpretação
comparison.rename(columns={'y': 'Real', 'yhat': 'Previsto'}, inplace=True)

# Chamar função para plotar comparação
plot_real_vs_forecast(comparison)

# Definindo a data final para previsões até 2027
end_date = datetime(2027, 12, 31)

# Calculando o número de dias entre a última data dos dados atuais e o final de 2027
last_date = forecast['ds'].max()
days_until_2027 = (end_date - last_date).days

# Gerando o DataFrame de previsões para o período desejado
future_2025 = prophet_pipeline.model.make_future_dataframe(periods=days_until_2027, freq='D')

# Adicionando os feriados ao DataFrame de previsões
future_2025 = pd.merge(future_2025, holidays_df[['ds', 'holiday']], on='ds', how='left')

# Garantir que a coluna 'holiday' esteja presente nas previsões (0 ou 1)
future_2025['holiday'] = future_2025['ds'].apply(lambda x: 1 if x in holidays_df['ds'].values else 0)

# Gerar as previsões para o período de 2025 até 2027
forecast_2025 = prophet_pipeline.model.predict(future_2025)

# Gráfico com dados históricos e previsões
plot_forecast_with_history(train_data, forecast_2025, title='Previsões e Dados Históricos (2025 em diante)')

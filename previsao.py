import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objs as go
from prophet import Prophet
from utils.helpers import ModelEvaluation  # Importando a classe ou função

def previsao():
    st.markdown("## **Previsão de valores do Petróleo Brent**", unsafe_allow_html=True)
    st.write("Nesta sessão apresentamos os valores previstos sobre a cotação do petróleo a partir do uso de um modelo de Machine Learning.")
    
    # Carregar os dados com separador ';'
    df = pd.read_csv("data/Base_IPEA.csv", sep=";")
    
    # Corrigir o nome da coluna 'valor_da_cotação' se houver espaços extras
    df.columns = df.columns.str.strip()

    # Garantir que a coluna 'data' esteja no formato datetime
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    
    # Verificar se há valores nulos na coluna 'valor_da_cotacao' e remover
    if 'valor_da_cotacao' in df.columns:
        df = df.dropna(subset=['valor_da_cotacao'])
    else:
        st.write("A coluna 'valor_da_cotacao' não foi encontrada!")
        return
    
    # Filtrar os dados até 2023 para treinar o modelo
    df_treino = df[df['data'] <= '2023-12-31']
    
    # Renomear as colunas para 'ds' e 'y'
    df_treino = df_treino.rename(columns={'data': 'ds', 'valor_da_cotacao': 'y'})
    
    # Certificar que não haja valores nulos após a renomeação
    df_treino = df_treino.dropna(subset=['ds', 'y'])

    # Verificar se a coluna 'ds' foi criada corretamente
    if 'ds' not in df_treino.columns:
        st.write("Erro: A coluna 'ds' não foi criada corretamente.")
        return
    
    # Criar uma nova instância do Prophet e treinar com os dados de treino
    modelo = Prophet()
    modelo.fit(df_treino)
    
    # Prever os valores para 2024
    futuro_2024 = pd.date_range(start="2024-01-01", end="2024-12-31", freq='D')
    futuro_df = pd.DataFrame(futuro_2024, columns=['ds'])
    
    # Fazer as previsões para 2024
    previsao_2024 = modelo.predict(futuro_df)
    
    # Comparar com os valores reais de 2024
    df_2024 = df[(df['data'] >= '2024-01-01') & (df['data'] <= '2024-12-31')]
    
    # Renomear as colunas para 'ds' e 'y' também em df_2024
    df_2024 = df_2024.rename(columns={'data': 'ds', 'valor_da_cotacao': 'y'})
    
    # Certificar que as colunas 'ds' e 'y' existem
    if 'ds' not in df_2024.columns or 'y' not in df_2024.columns:
        st.write("Erro: As colunas 'ds' e 'y' não estão presentes nos dados de 2024.")
        return
    
    # Criação do objeto de avaliação com os dados reais e as previsões
    avaliacao = ModelEvaluation(df_2024, previsao_2024)

    # Chama o método 'evaluate' para obter as métricas
    resultados = avaliacao.evaluate()

    # Exibir as métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("📊 MAE", f"{resultados['MAE']:.2f}")
    col2.metric("📈 MAPE", f"{resultados['MAPE']:.2f}%")
    col3.metric("📉 RMSE", f"{resultados['RMSE']:.2f}")

    # Exibir as previsões para 2024 vs valores reais
    trace1 = go.Scatter(
        x=df_2024['ds'],
        y=df_2024['y'],
        mode='lines+markers',
        name='Real',
        line=dict(color='#1E90FF'),
    )
    
    trace2 = go.Scatter(
        x=previsao_2024['ds'],
        y=previsao_2024['yhat'],
        mode='lines+markers',
        name='Previsão',
        line=dict(color='#FF6347'),
    )
    
    layout = go.Layout(
        title='Previsão x Real de Preço do Petróleo Brent (2024)',
        xaxis=dict(title='Data'),
        yaxis=dict(title='Preço (US$)'),
        hovermode='closest'
    )
    
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    st.plotly_chart(fig)

    # Adicionar o SelectBox para escolha do ano
    ano_selecionado = st.selectbox(
        'Selecione o ano para previsão:',
        options=[2025, 2026, 2027, 2028]
    )
    
    # Gerar previsão para o ano selecionado
    futuro_ano = pd.date_range(start=f"{ano_selecionado}-01-01", end=f"{ano_selecionado}-12-31", freq='D')
    futuro_df_ano = pd.DataFrame(futuro_ano, columns=['ds'])
    
    previsao_ano = modelo.predict(futuro_df_ano)
    
    # Exibir gráfico da previsão do ano selecionado
    trace_ano = go.Scatter(
        x=previsao_ano['ds'],
        y=previsao_ano['yhat'],
        mode='lines',
        name=f'Previsão {ano_selecionado}',
        line=dict(color='#32CD32'),
    )

    layout_ano = go.Layout(
        title=f'Previsão do Preço do Petróleo Brent ({ano_selecionado})',
        xaxis=dict(title='Data'),
        yaxis=dict(title='Preço (US$)'),
        hovermode='closest'
    )
    
    fig_ano = go.Figure(data=[trace_ano], layout=layout_ano)
    st.plotly_chart(fig_ano)

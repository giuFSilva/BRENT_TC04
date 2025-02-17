import streamlit as st
import pandas as pd
import plotly.express as px

# Função para exibir a página de Histórico
def historico():
    st.markdown("## **O que é o Petróleo Brent**", unsafe_allow_html=True)

    # Descrição breve sobre o Petróleo Brent
    st.write(
        "O petróleo Brent foi batizado assim porque era extraído de uma base da Shell chamada Brent. "
        "Atualmente, a palavra Brent designa todo o petróleo extraído no Mar do Norte e comercializado na Bolsa de Londres. "
        "A cotação do Brent desempenha um papel fundamental na economia global, pois influencia diretamente "
        "diversos setores, como os de combustíveis, incluindo o diesel e a gasolina, que são derivados do petróleo. "
        "Alterações nos preços de comercialização do Brent impactam diretamente o custo desses produtos, refletindo no "
        "orçamento do consumidor final, que pode enfrentar um aumento significativo nos gastos."
    )

    # Caminho do arquivo CSV
    file_path = "data/Base_IPEA.csv"

    try:
        # Carregar os dados
        df = pd.read_csv(file_path, sep=";", encoding="utf-8", engine="python")

        # Normalizar os nomes das colunas
        df.columns = df.columns.str.lower().str.strip()

        # Converter a coluna data para datetime
        df["data"] = pd.to_datetime(df["data"], errors="coerce")

        # Criar uma coluna com o ano
        df["ano"] = df["data"].dt.year

        # Criar lista de anos únicos disponíveis
        anos_disponiveis = sorted(df["ano"].dropna().unique(), reverse=True)

        # Criar um selectbox para o usuário escolher um ano
        st.markdown("### **Variação do preço:**")
        st.write("Selecione o ano desejado para conferir as variações de preço do petróleo Brent")
        ano_selecionado = st.selectbox("", ["Todos os anos"] + list(anos_disponiveis))

        # Filtrar os dados pelo ano selecionado
        if ano_selecionado == "Todos os anos":
            df_filtrado = df
        else:
            df_filtrado = df[df["ano"] == ano_selecionado]

        # Calcular estatísticas básicas
        valor_medio = df_filtrado["valor_da_cotacao"].mean()
        valor_maximo = df_filtrado["valor_da_cotacao"].max()
        valor_minimo = df_filtrado["valor_da_cotacao"].min()

        # Exibir estatísticas em três colunas
        col1, col2, col3 = st.columns(3)
        col1.metric("📊 Valor Médio da Cotação", f"${valor_medio:,.2f}")
        col2.metric("📈 Valor Máximo da Cotação", f"${valor_maximo:,.2f}")
        col3.metric("📉 Valor Mínimo da Cotação", f"${valor_minimo:,.2f}")

        # Criar o gráfico de linha interativo com Plotly
        if "data" in df.columns and "valor_da_cotacao" in df.columns:
            fig = px.line(
                df_filtrado,
                x="data",
                y="valor_da_cotacao",
                title="Histórico de Cotação do Petróleo Brent",
                labels={"valor_da_cotacao": "Valor da Cotação (US$)", "data": "Data"},
                line_shape="linear"
            )

            # Aumentar o tamanho do título
            fig.update_layout(
                title=dict(
                    text="Histórico de Cotação do Petróleo Brent",
                    font=dict(
                        size=24,  # Tamanho da fonte
                        family="Arial",  # Fonte do título
                    )
                )
            )

            # Adicionar interatividade (zoom, hover, etc.)
            fig.update_layout(
                xaxis=dict(
                    rangeselector=dict(
                        buttons=[
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(count=6, label="6m", step="month", stepmode="backward"),
                            dict(count=1, label="1y", step="year", stepmode="backward"),
                            dict(step="all")
                        ]
                    ),
                    rangeslider=dict(visible=True),
                    type="date"
                )
            )

            # Exibir o gráfico interativo
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.error("⚠️ Erro: A base de dados não contém as colunas esperadas ('data' e 'valor_da_cotacao').")

    except FileNotFoundError:
        st.error(f"⚠️ Erro: O arquivo `{file_path}` não foi encontrado. Verifique o caminho e tente novamente.")
   
 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Função para carregar e filtrar os dados
def carregar_dados(ano):
    df = pd.read_csv("data/Base_IPEA.csv", parse_dates=["data"], sep=";")
    # Criar uma coluna com o ano
    df["ano"] = df["data"].dt.year
    # Filtrar apenas os dados do ano especificado
    df = df[df["ano"] == ano]
    return df


# Função para Insights
def insights():
    st.markdown("## **Principais Insights**", unsafe_allow_html=True)
    st.write("Esta seção apresenta alguns dos principais insights que impactaram ao longo dos anos o valor do petróleo Brent.")
  
    # Seleção de abas como "pastinhas"
    option = st.selectbox("Escolha um Tópico", ["Impacto das Sanções EUA-Irã", "Impacto da COVID-19", "Tendências de Mercado PÓS COVID", "Guerra da Ucrânia e Rússia"])
    
    # Exibir conteúdo baseado na seleção
    if option == "Impacto das Sanções EUA-Irã":
        st.markdown("### **Impacto das Sanções EUA-Irã**")
        st.write("Em 2018, os preços do petróleo Brent apresentaram grande volatilidade, impulsionados principalmente pela reimposição de sanções dos Estados Unidos ao Irã, um dos maiores produtores de petróleo. A saída dos EUA do Plano de Ação Conjunto Global (JCPOA) em maio daquele ano afetou drasticamente a produção e exportação de petróleo iraniano, retirando milhões de barris do mercado.\n"
                "Antes da reimposição das sanções, o preço do petróleo já estava subindo devido aos cortes de produção da OPEC e ao aumento da demanda global. A decisão de Trump levou a um pico nos preços do petróleo, mas países como China e Índia continuaram comprando petróleo iraniano por meio de isenções temporárias. A produção de petróleo de xisto nos EUA também ajudou a equilibrar o mercado, impedindo uma alta ainda mais acentuada.\n"
                "Em setembro, o preço do barril atingiu o ponto máximo, impulsionado pela incerteza geopolítica e pela alta demanda. No entanto, a volatilidade do mercado também foi influenciada por tensões comerciais entre os EUA e a China, além das incertezas relacionadas à oferta global de petróleo. O aumento dos preços teve impacto nas economias dependentes de importação de energia, gerando preocupações com a inflação e a instabilidade econômica.")
    
        df_2018 = carregar_dados(2018)

        # Criando um gráfico de linha interativo
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df_2018["data"],
            y=df_2018["valor_da_cotacao"],
            mode="lines",
            name="Cotação do Petróleo em 2018",
            line=dict(color="royalblue", width=2)
            ))

        # Adicionando anotações em pontos específicos do gráfico
        annotations = [
            {"x": "2018-05-08", "y": df_2018[df_2018["data"] == "2018-05-08"]["valor_da_cotacao"].values[0], "text": "Saída dos EUA do Acordo Nuclear"},
            ]

        for ann in annotations:
            fig.add_annotation(
            x=ann["x"],
            y=ann["y"],
            text=ann["text"],
            showarrow=True,
            arrowhead=2,
            font=dict(size=12, color="black"),
            bgcolor="yellow"
                )

        # Configurações do layout do gráfico
        fig.update_layout(
            title="Variação da Cotação do Petróleo em 2018",
            xaxis_title="Data",
            yaxis_title="Cotação (USD)",
            hovermode="x"
            )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig)



        
    elif option == "Impacto da COVID-19":
        st.markdown("### **Impacto da COVID-19**")
        st.write("O ano de 2020 foi marcado por grande volatilidade no mercado de petróleo, com o Brent caindo 21,5% em relação ao ano anterior, devido à pandemia de COVID-19. A crise de saúde global afetou diretamente o consumo de petróleo, especialmente nos setores de transporte e comércio. Em 29 de janeiro, a OMS declarou emergência global, o que gerou incertezas no mercado. Em março, a guerra de preços entre Rússia e Arábia Saudita e o fracasso das negociações da OPEP+ desestabilizaram ainda mais a situação, com a Arábia Saudita aumentando a produção. No dia 20 de abril, o preço do petróleo WTI caiu para níveis negativos pela primeira vez na história, enquanto o Brent foi a 20 dolares por barril.\n"
        "Apesar do impacto inicial, cortes históricos de produção da OPEP+ em abril ajudaram a estabilizar os preços no segundo semestre, e o Brent se recuperou para cerca de US$ 50 por barril até o final do ano, à medida que a demanda foi gradualmente se recuperando com a reabertura econômica. Além disso, houve um aumento de 45% no investimento em energias renováveis, acelerando a transição para fontes mais sustentáveis de energia, o que afetou a demanda por petróleo no longo prazo.")
    
        
        
        # Carregar os dados de 2020
        df_2020 = carregar_dados(2020)

        # Verificar se há dados antes de criar o gráfico
        if df_2020 is not None:
            # Criando um gráfico de linha interativo
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=df_2020["data"],
                y=df_2020["valor_da_cotacao"],
                mode="lines",
                name="Cotação do Petróleo em 2020",
                line=dict(color="red", width=2)
            ))

            # Adicionando anotações sobre eventos importantes
            annotations = [
                {"x": "2020-01-30", "y": df_2020[df_2020["data"] == "2020-01-30"]["valor_da_cotacao"].values[0], "text": "OMS declara Emergência Global"},
                {"x": "2020-03-09", "y": df_2020[df_2020["data"] == "2020-03-09"]["valor_da_cotacao"].values[0], "text": "Crise do Petróleo: Colapso da OPEP"},
                {"x": "2020-04-20", "y": df_2020[df_2020["data"] == "2020-04-20"]["valor_da_cotacao"].values[0], "text": "Petróleo atinge preço negativo (-$37)"},
            ]

            for ann in annotations:
                fig.add_annotation(
                    x=ann["x"],
                    y=ann["y"],
                    text=ann["text"],
                    showarrow=True,
                    arrowhead=2,
                    font=dict(size=12, color="black"),
                    bgcolor="yellow"
                )

            # Configurações do layout do gráfico
            fig.update_layout(
                title="Variação da Cotação do Petróleo em 2020 (Impacto da COVID-19)",
                xaxis_title="Data",
                yaxis_title="Cotação (USD)",
                hovermode="x"
            )

            # Exibir o gráfico no Streamlit
            st.plotly_chart(fig)

        
    elif option == "Tendências de Mercado PÓS COVID":
        st.markdown("Em 2021, o mercado de petróleo experimentou uma recuperação expressiva, impulsionada pela retomada econômica global após a pandemia. O início da vacinação no final de 2020 foi um marco, promovendo uma recuperação gradual das economias. Como resultado, o preço do petróleo subiu 47,4%, após a queda acentuada em 2020.\n"
        "Apesar de um início de ano difícil, com preços baixos no primeiro trimestre, a partir do segundo semestre, a vacinação nos Estados Unidos, União Europeia, Rússia e Reino Unido aumentou a confiança no mercado. A demanda por petróleo cresceu à medida que as economias se reabriam. No entanto, em meados de 2021, o preço do petróleo alcançou US$ 73,19, mas sofreu uma leve queda após o anúncio do Federal Reserve sobre o aumento das taxas de juros. Esse movimento gerou incertezas sobre a continuidade da recuperação econômica.\n"
        "Ainda assim, a alta na demanda e o retorno da atividade econômica ajudaram a estabilizar os preços. No final do ano, a variante Ômicron trouxe novas incertezas, mas a recuperação global já estava em andamento, refletindo uma trajetória positiva para o mercado de petróleo.")
        
        
        # Carregar os dados de 2021
        df_2021 = carregar_dados(2021)

        # Verificar se há dados antes de criar o gráfico
        if df_2021 is not None:
            # Criando um gráfico de linha interativo
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=df_2021["data"],
                y=df_2021["valor_da_cotacao"],
                mode="lines",
                name="Cotação do Petróleo em 2021",
                line=dict(color="green", width=2)
            ))

            # Adicionando anotações sobre eventos importantes
            annotations = [
                {"x": "2021-01-04", "y": df_2021[df_2021["data"] == "2021-01-04"]["valor_da_cotacao"].values[0], "text": "Início da vacinação global"},
                {"x": "2021-07-01", "y": df_2021[df_2021["data"] == "2021-07-01"]["valor_da_cotacao"].values[0], "text": "Alta na demanda por petróleo"},
                {"x": "2021-12-01", "y": df_2021[df_2021["data"] == "2021-12-01"]["valor_da_cotacao"].values[0], "text": "Variante Ômicron identificada"},
            ]

            for ann in annotations:
                fig.add_annotation(
                    x=ann["x"],
                    y=ann["y"],
                    text=ann["text"],
                    showarrow=True,
                    arrowhead=2,
                    font=dict(size=12, color="black"),
                    bgcolor="yellow"
                )

            # Configurações do layout do gráfico
            fig.update_layout(
                title="Variação da Cotação do Petróleo em 2021 (Retomada Pós-COVID)",
                xaxis_title="Data",
                yaxis_title="Cotação (USD)",
                hovermode="x"
            )

            # Exibir o gráfico no Streamlit
            st.plotly_chart(fig)


    elif option == "Guerra da Ucrânia e Rússia":
        st.markdown("### **Guerra da Ucrânia e Rússia**")
        st.write("A guerra entre a Ucrânia e a Rússia, iniciada em fevereiro de 2022, causou uma escalada significativa no preço do petróleo. A Rússia, um dos maiores produtores e exportadores de petróleo, viu suas exportações comprometidas por sanções e bloqueios comerciais, o que causou uma escassez de oferta e levou o preço do Brent a atingir US$ 130 por barril.\n"
        "Embora a demanda permanecesse alta, as dificuldades logísticas e geopolíticas pressionaram ainda mais os preços. Para mitigar os impactos econômicos, os Estados Unidos e outros países consumidores anunciaram a liberação de 60 milhões de barris de petróleo de seus estoques de emergência. Simultaneamente, a OPEC+ aumentou gradualmente a produção em 400 mil barris por dia, buscando estabilizar o mercado. Essas ações ajudaram a desacelerar a escalada dos preços, apesar da continuidade do conflito e das sanções contra o petróleo russo."
        )
        
        # Carregar os dados de 2022
        df_2022 = carregar_dados(2022)

        # Verificar se há dados antes de criar o gráfico
        if df_2022 is not None:
            # Criando um gráfico de linha interativo
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=df_2022["data"],
                y=df_2022["valor_da_cotacao"],
                mode="lines",
                name="Cotação do Petróleo em 2022",
                line=dict(color="red", width=2)
            ))

            # Adicionando anotações sobre eventos importantes
            annotations = [
                {"x": "2022-02-24", "y": df_2022[df_2022["data"] == "2022-02-24"]["valor_da_cotacao"].values[0], "text": "Início da Guerra na Ucrânia"},
                {"x": "2022-03-07", "y": df_2022[df_2022["data"] == "2022-03-07"]["valor_da_cotacao"].values[0], "text": "Petróleo atinge US$ 130 (máxima histórica)"},
                {"x": "2022-06-01", "y": df_2022[df_2022["data"] == "2022-06-01"]["valor_da_cotacao"].values[0], "text": "Sanções da UE contra o petróleo russo"},
                {"x": "2022-10-05", "y": df_2022[df_2022["data"] == "2022-10-05"]["valor_da_cotacao"].values[0], "text": "OPEP+ reduz produção para conter queda dos preços"},
            ]

            for ann in annotations:
                fig.add_annotation(
                    x=ann["x"],
                    y=ann["y"],
                    text=ann["text"],
                    showarrow=True,
                    arrowhead=2,
                    font=dict(size=12, color="black"),
                    bgcolor="yellow"
                )

            # Configurações do layout do gráfico
            fig.update_layout(
                title="Variação da Cotação do Petróleo em 2022 (Impactos da Guerra na Ucrânia)",
                xaxis_title="Data",
                yaxis_title="Cotação (USD)",
                hovermode="x"
            )

            # Exibir o gráfico no Streamlit
            st.plotly_chart(fig)
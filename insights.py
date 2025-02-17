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
        st.write("O Irã é o principal Estado patrocinador do terrorismo "
                "Esta foi a frase que o presidente Donald Trump usou para declarar no ano de 2018 a quebra do acordo sobre o alívio de sanções econômicas para o Irã que havia sido estabelecida por Barack Obama em 2016. "
                "O Plano de Ação Conjunto Global (JCPOA), exigia que o Irã limitasse seu programa nuclear, comprometendo-se a não desenvolver armas nucleares, em troca do alívio de sanções econômicas. "
                "Essa iniciativa não apenas estabilizou as relações entre os dois países, mas também trouxe um respiro para o mercado global de petróleo, dado que o Irã é um dos maiores produtores mundiais da commodity "
                "fazendo parte da Opep. Com o fim das sanções, o Irã voltou a exportar grandes volumes de petróleo, aumentando sua produção para cerca de 3,8 milhões de barris por dia. Isso injetou otimismo nos mercados, "
                "reduziu os preços do petróleo e forneceu um equilíbrio necessário à economia global. Países europeus e asiáticos, grandes consumidores de petróleo, puderam acessar um novo fornecedor estável, diversificando "
                "suas cadeias de abastecimento e reduzindo a dependência de outras potências. "
                "Mas em 2018, o equilíbrio foi quebrado. Donald Trump, recém-empossado presidente dos Estados Unidos, decidiu retirar o país do acordo nuclear, acusando o Irã de não ser transparente e de continuar "
                "alimentando ambições nucleares. Essa decisão foi um divisor de águas. "
                "Ao sair do acordo, os EUA reimpuseram sanções devastadoras ao Irã, incluindo restrições ao setor petrolífero. O impacto foi imediato: a produção e exportação de petróleo iraniano despencaram, retirando "
                "milhões de barris diários do mercado. Isso pressionou os preços globais do petróleo para cima, afetando diretamente os custos de energia e combustíveis em diversos países. Para economias dependentes de "
                "importações de petróleo, como as europeias e asiáticas, isso significou maiores gastos e instabilidade econômica.")
    
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
        st.write("O ano de 2020 foi marcado por uma extrema volatilidade no mercado de petróleo, com o Brent registrando uma queda de 21,5% em comparação ao ano anterior, "  
        "devido principalmente à pandemia de COVID-19. A crise global de saúde afetou drasticamente o consumo de petróleo, impactando setores como transporte aéreo, rodoviário, comércio e "  
        "indústria. Em meados de fevereiro, as bolsas de valores registraram quedas acentuadas, com reflexos similares à crise de 2008, marcando o início de uma desaceleração econômica global. " 
        "Paralelamente, uma guerra de preços entre Rússia e Arábia Saudita agravou o cenário. Em março, o fracasso das negociações da OPEP+ levou a Arábia Saudita a reduzir os preços e aumentar "  
        "a produção, desestabilizando o mercado em um momento de baixa demanda. Em abril, o excesso de oferta levou os preços do WTI a ficarem negativos pela primeira vez na história, enquanto "  
        "o Brent caiu para níveis próximos a US 20 por barril."
        "No entanto, cortes históricos de produção acordados pela OPEP+ em abril, com uma redução de 9,7 milhões de barris por dia, "  
        "ajudaram a estabilizar os preços no segundo semestre. No final do ano, o Brent recuperou-se parcialmente, alcançando cerca de US$ 50 por barril, refletindo uma melhora gradual na "  
        "demanda com a reabertura econômica. Além disso, a reabertura gradual das economias do segundo semestre em diante, deram força e perspectiva sobre a volta do consumo. "   
        "Outro ponto significativo foi o aumento do investimento em energias renováveis, com um crescimento de 45% em relação ao ano anterior. Grandes empresas do setor anunciaram planos mais " 
        "agressivos para reduzir emissões de carbono, sinalizando uma mudança estrutural no mercado de energia e pressionando a demanda por petróleo no longo prazo. O ano de 2020 foi um divisor de " 
        "águas para o setor, destacando a fragilidade do mercado frente a crises globais e acelerando a transição para fontes de energia mais sustentáveis "
        )
        
        
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
        st.markdown("### **Tendências de Mercado PÓS COVID**")
        st.write("Em 2021, o mercado de petróleo passou por uma recuperação notável, impulsionada pela retomada econômica global após os desafios causados pela pandemia de COVID-19. " 
        "O marco da liberação das vacinas no final de 2020 teve um impacto direto nesse processo, proporcionando uma recuperação gradual das economias ao longo de 2021. Como resultado, o preço do petróleo experimentou uma alta expressiva de 47,4%, " 
        "após uma queda acentuada no início da pandemia. Desafios Iniciais e Recuperação no 2º Semestre. No início de 2021, o mercado ainda sentia os efeitos da crise sanitária, com o preço do petróleo caindo drasticamente em março e abril, atingindo "
        "níveis muito baixos. No entanto, a partir Do segundo semestre do ano, especialmente com o início da vacinação nos Estados Unidos, União Europeia, Rússia e Reino Unido, o preço do petróleo começou a retomar os níveis pré-pandemia. " 
        "A expectativa de que as economias voltariam a funcionar plenamente impulsionou a demanda por energia, o que refletiu diretamente no aumento dos preços das commodities, incluindo o petróleo. "
        "Impactos das Decisões Econômicas Globais. Em meados de 2021, o preço do petróleo atingiu US$ 73,19 na sexta-feira, 18 de junho. No entanto, essa leve queda foi observada após o anúncio do " 
        "Federal Reserve (FED), o banco central dos Estados Unidos, sobre o aumento da taxa de juros esperado para 2023. O mercado reagiu negativamente a essa notícia, antecipando um impacto na " 
        "recuperação econômica e, consequentemente, na demanda por petróleo. A alta nas taxas de juros sugeria uma desaceleração econômica futura, o que gerou incertezas sobre a continuidade do " 
        "crescimento nos preços das commodities. O Reflexo da Recuperação Econômica. Essa recuperação do preço do Brent em 2021 foi um reflexo da resiliência do mercado de petróleo diante dos desafios impostos pela pandemia e das medidas adotadas para estabilizar a " 
        "economia global. Incentivos fiscais e o retorno da atividade econômica mundial, especialmente nos países mais afetados pela pandemia, como os Estados Unidos e os países da União Europeia, " 
        "ajudaram a acelerar a recuperação da demanda por petróleo. À medida que as economias voltaram a operar a pleno vapor, o preço do petróleo seguiu sua trajetória de alta, com os mercados se " 
        "ajustando à nova")
        
        
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
        st.write("A guerra entre a Ucrânia e a Rússia, iniciada em fevereiro de 2022, teve impactos significativos no mercado global de petróleo, especialmente no preço do Brent. " 
        "A Rússia é um dos maiores produtores e exportadores de petróleo do mundo, e com o início do conflito, o preço do barril de Brent disparou, chegando a custar até $110,00. "
        "sse aumento abrupto ocorreu devido à interrupção da oferta, já que a Rússia, um dos principais fornecedores de petróleo, viu suas exportações prejudicadas por sanções e " 
        "bloqueios comerciais. Embora a demanda por petróleo continuasse alta, as dificuldades logísticas e geopolíticas resultaram em uma escassez de oferta, pressionando os preços para cima. "
        "Diante dos potenciais impactos econômicos globais, os Estados Unidos e outros grandes países consumidores de petróleo optaram por limitar as sanções aplicadas à Rússia, buscando " 
        "minimizar os efeitos negativos para suas economias. Para enfrentar o aumento nos preços do petróleo, os Estados Unidos, juntamente com outras nações, anunciaram a liberação de 60 " 
        "milhões de barris de petróleo de seus estoques de emergência, uma medida para aliviar a pressão sobre os preços no curto prazo. "
        "Além disso, a Organização dos Países Exportadores de Petróleo e aliados (OPEC+) também tomou medidas para tentar equilibrar o mercado. Em abril de 2022, a OPEC+ concordou em aumentar " 
        "a produção de petróleo em 400 mil barris por dia, uma tentativa de estabilizar os preços e fornecer mais oferta ao mercado global. Esse aumento gradual de produção, embora pequeno " 
        "em relação à demanda global, foi suficiente para trazer certa estabilidade aos preços e desacelerar a escalada no valor do Brent. "
        "Visualizar os dados e identificar pontos relevantes ao longo do ano, para melhorar a descrição dos insights. ")


         
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
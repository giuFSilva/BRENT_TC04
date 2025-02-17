import streamlit as st
import pandas as pd
import plotly.express as px

def impactos():
    st.markdown("### **Impactos sobre o Produto Final**")
    
    # Descrição breve sobre o Petróleo Brent
    st.write(
        "O preço do petróleo Brent influencia diretamente o custo dos combustíveis e, consequentemente, afeta uma série de outros produtos e serviços, impactando a economia de forma ampla."
    )
    
    # Descrever o impacto de eventos recentes no preço do petróleo
    st.write(
        "Ao longo dos últimos anos, diversos eventos globais, como a pandemia de COVID-19, a guerra na Ucrânia e as sanções ao Irã, têm causado variações no preço do petróleo, refletindo diretamente no aumento ou redução dos custos dos combustíveis e afetando os consumidores."
    )

    # Seção 1: Aumento nos preços dos combustíveis
    st.markdown("#### **1. Aumento nos Preços dos Combustíveis**")
    st.write(
        "Com o aumento do preço do petróleo Brent, os preços dos combustíveis (como gasolina e diesel) também se elevam. Isso afeta diretamente o custo do transporte de mercadorias e o transporte público, impactando o orçamento das famílias."
    )
    
    # Link para mais informações sobre os impactos no preço dos combustíveis
    st.write("[Leia mais sobre o impacto dos preços dos combustíveis](https://g1.globo.com/economia/noticia/2022/06/27/precos-dos-combustiveis-no-brasil-por-que-subiram-e-o-que-pode-ser-feito-veja-perguntas-e-respostas.ghtml)")

    # Seção 2: Aumento nos preços de alimentos e produtos essenciais
    st.markdown("#### **2. Aumento nos Preços de Alimentos e Produtos Essenciais**")
    st.write(
        "O aumento no preço do petróleo também eleva o custo dos produtos alimentícios, já que o transporte e o armazenamento desses produtos dependem do combustível. Além disso, a produção de fertilizantes e outros insumos agrícolas, que também dependem de derivados do petróleo, tende a ficar mais cara."
    )
        
    # Link para mais informações sobre os impactos no preço dos alimentos
    st.write("[Leia mais sobre o impacto no preço dos alimentos](https://smetal.org.br/imprensa/apesar-de-esforcos-do-governo-federal-preco-dos-alimentos-segue-alto-entenda/#:~:text=Um%20dos%20fatores%20que%20influencia,uma%20s%C3%A9rie%20de%20outros%20produtos.)")

    # Seção 3: Impactos no mercado financeiro e na economia global
    st.markdown("#### **3. Impactos no Mercado Financeiro e na Economia Global**")
    st.write(
        "Quando os preços do petróleo aumentam de forma substancial, pode haver uma pressão sobre os mercados financeiros e uma desaceleração econômica global, o que afeta o emprego e os investimentos."
    )
        
    # Link para mais informações sobre os impactos econômicos
    st.write("[Leia mais sobre os impactos econômicos da alta do petróleo](https://www.infomoney.com.br/mercados/as-8-formas-como-o-petroleo-a-us-100-pode-afetar-drasticamente-a-economia-global/)")

# A função `impactos()` deve ser chamada via navegação no `app.py`, não diretamente.

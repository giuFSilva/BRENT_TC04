import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Função para Página Inicial
def pagina_inicial():
    st.markdown("## **Projeto de pesquisa**", unsafe_allow_html=True)

    st.write("\n\n\n\n\n\n\n\n")
    st.markdown("### **Objetivo**", unsafe_allow_html=True)
    st.write(
        "Este projeto materializa uma jornada de aprendizado, com foco em análise de dados, "
        "insights e representações gráficas, utilizando como base os dados sobre o petróleo Brent."
        " O projeto faz parte do módulo 4 do curso de Data Analytics da FIAP."
    )

    st.markdown("### **Etapas do projeto**", unsafe_allow_html=True)
    st.write(
        "A construção do projeto foi segmentada em fases, a fim de que pequenos entregáveis fossem feitos ao longo do caminho \n"
        "- Estruturação do projeto\n"
        "- Entendimento sobre o que é o petróleo\n"
        "- Análise histórica do petróleo e seus impactos\n"
        "- Levantamento de insights\n"
        "- Criação de um modelo de Machine Learning para predição\n"
        "- Construção de dashboard\n"
    )

    st.markdown("### **Time responsável**", unsafe_allow_html=True)
    st.write("Giulia Felix da Silva - RM357020")

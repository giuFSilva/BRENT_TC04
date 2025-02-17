import streamlit as st

# Função para Página Inicial
def pagina_inicial():
    st.markdown("## **Projeto de Pesquisa**", unsafe_allow_html=True)

    st.divider()  # Linha divisória para melhor organização

    st.markdown("### **🎯 Objetivo**", unsafe_allow_html=True)
    st.write(
        "Este projeto materializa uma jornada de aprendizado, com foco em análise de dados, "
        "insights e representações gráficas, utilizando como base os dados sobre o petróleo Brent. "
        "O projeto faz parte do módulo 4 do curso de **Data Analytics da FIAP**."
    )

    st.divider()

    st.markdown("### **📌 Etapas do Projeto**", unsafe_allow_html=True)
    st.markdown(
        """
        - 🏗️ **Estruturação do projeto**
        - ⛽ **Entendimento sobre o que é o petróleo**
        - 📊 **Análise histórica do petróleo e seus impactos**
        - 🔍 **Levantamento de insights**
        - 🤖 **Criação de um modelo de Machine Learning para predição**
        - 📈 **Construção de dashboard**
        """
    )

    st.divider()

    st.markdown("### **👥 Time Responsável**", unsafe_allow_html=True)
    st.write("📝 **Giulia Felix da Silva** - RM357020")

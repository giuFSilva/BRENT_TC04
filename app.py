import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from historico import historico
from pagina_inicial import pagina_inicial
from insights import insights
from previsao import previsao 
from impactos import impactos

# Inicializa o estado da sessão para navegação (caso não exista)
if "pagina" not in st.session_state:
    st.session_state["pagina"] = "Página Inicial"  # Garante que a Página Inicial será a padrão

# Criando os menus laterais clicáveis (com botões)
with st.sidebar:
    st.markdown("## **Menu**", unsafe_allow_html=True)
    if st.button("Página Inicial", use_container_width=True, key="pagina_inicial_btn"):
        st.session_state["pagina"] = "Página Inicial"
    if st.button("Histórico", use_container_width=True, key="historico_btn"):
        st.session_state["pagina"] = "Histórico"
    if st.button("Insights", use_container_width=True, key="insights_btn"):
        st.session_state["pagina"] = "Insights"
    if st.button("Impactos", use_container_width=True, key="impactos_btn"):
        st.session_state["pagina"] = "Impactos"
    if st.button("Previsão", use_container_width=True, key="previsao_btn"):
        st.session_state["pagina"] = "Previsão"

# Renderizando a página ativa
if st.session_state["pagina"] == "Página Inicial":
    pagina_inicial()
elif st.session_state["pagina"] == "Histórico":
    historico()  
elif st.session_state["pagina"] == "Insights":
    insights()
elif st.session_state["pagina"] == "Impactos":
    impactos()
elif st.session_state["pagina"] == "Previsão":
    previsao()

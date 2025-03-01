import streamlit as st
import pandas as pd



st.title("Clientes cadastrados")
st.divider()

dados = pd.read_csv("clientes.csv")

def mostrar_tabela():
    tabela = st.dataframe(dados)
    return tabela

def editar_tabela():
    tabela = st.data_editor(dados)
    return tabela
    



btn_show = st.button("Mostrar Tabela", on_click=mostrar_tabela)

btn_edit = st.button("Editar Tabela", on_click=editar_tabela)



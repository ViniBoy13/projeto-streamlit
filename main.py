import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, dt_nasc, tipo, senha):
    if nome and senha == verifica_senha:
        with open("clientes.csv", "a", encoding='utf-8') as file:
            file.write(f'{nome},{dt_nasc},{tipo},{senha}\n')
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(

    page_title='Cadastro de Clientes',
    page_icon='📝'
)

st.title('Cadastro de Clientes')
st.divider()


nome = st.text_input("Digite o nome do Cliente: ", key='nome_cliente', max_chars=12)

data_min = date(day=1, month=1, year=1940)
data_max = date.today()
dt_nasc = st.date_input("Data de nascimento", format="DD/MM/YYYY", min_value=data_min, max_value=data_max)

tipo = st.selectbox("Tipo do Cliente", ['Pessoa Física', 'Pessoa Jurídica'])

senha = st.text_input('Digite sua senha: ', key='senha_input', max_chars=40, type='password')
verifica_senha = st.text_input('Confirme sua senha: ', key='verifica_input', max_chars=40, type='password')

if senha and verifica_senha:
    if senha == verifica_senha:
        st.success('As senhas coincidem', icon='✅')
    else:
        st.error('As senhas não coincidem', icon='❌')

btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados, args=[nome, dt_nasc, tipo, senha])

if btn_cadastrar:
    if st.session_state['sucesso']:
        st.success('Cliente cadastrado com sucesso!', icon="✅")
    else:
        st.error('Houve algum problema no cadastro.. ', icon='❌')

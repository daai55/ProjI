import streamlit as st
import requests

# Configuração inicial da página
st.set_page_config(page_title="AgendAçougue", page_icon="🥩")

st.title("AgendAçougue")
st.write("Bem-vindo ao sistema de agendamento do AgendAçougue!")

# Formulário de agendamento
st.header("Agendar um serviço")
nome = st.text_input("Nome")
email = st.text_input("Email")
servico = st.selectbox("Serviço", ["Corte Especial", "Moagem de Carne", "Embalagem a Vácuo"])
data = st.date_input("Data do agendamento")
horario = st.time_input("Horário do agendamento")

if st.button("Agendar"):
    if nome and email:
        dados = {
            "nome": nome,
            "email": email,
            "servico": servico,
            "data": str(data),
            "horario": str(horario)
        }

        # Substitua a URL abaixo pela URL real do backend caso tenha um.
        url_backend = "http://localhost:5000/agendamentos"
        response = requests.post(url_backend, json=dados)

        if response.status_code == 200:
            st.success("Agendamento realizado com sucesso!")
        else:
            st.error("Erro ao realizar agendamento. Tente novamente.")
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios.")
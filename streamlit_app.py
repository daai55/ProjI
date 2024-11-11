import streamlit as st
import requests

# Configuração inicial da página
st.set_page_config(page_title="AgendAçougue", page_icon="🥩", layout="centered")

# Título estilizado
st.markdown("<h1 style='text-align: center; color: #FF6347;'>AgendAçougue 🥩</h1>", unsafe_allow_html=True)
st.write("### Bem-vindo ao sistema de agendamento de serviços do AgendAçougue!")
st.write("Aproveite para agendar seu serviço com comodidade e praticidade.")

# Divisor visual
st.markdown("---")

# Formulário de agendamento com layout melhorado
with st.form(key="form_agendamento"):
    st.subheader("📝 Dados do Agendamento")
    
    # Campos do cliente
    nome = st.text_input("Nome", placeholder="Digite seu nome completo")
    email = st.text_input("Email", placeholder="Digite seu email")
    
    # Opções de serviço
    servico = st.selectbox("Escolha o serviço desejado", ["Corte Especial", "Moagem de Carne", "Embalagem a Vácuo"])
    
    # Escolha da data e horário
    col1, col2 = st.columns(2)
    with col1:
        data = st.date_input("Data do agendamento")
    with col2:
        horario = st.time_input("Horário do agendamento")
    
    # Forma de pagamento
    st.subheader("💳 Forma de Pagamento")
    pagamento = st.radio(
        "Selecione a forma de pagamento:",
        options=["Cartão de Crédito", "Cartão de Débito", "Pix", "Dinheiro"],
        help="Escolha como deseja realizar o pagamento no momento do serviço."
    )

    # Botão de envio com layout centralizado
    submit_button = st.form_submit_button("Agendar")
    if submit_button:
        # Validação de campos obrigatórios
        if nome and email:
            # Dados a serem enviados para o backend
            dados = {
                "nome": nome,
                "email": email,
                "servico": servico,
                "data": str(data),
                "horario": str(horario),
                "pagamento": pagamento
            }

            # Substitua a URL abaixo pela URL real do backend caso tenha um.
            url_backend = "http://localhost:5000/agendamentos"
            response = requests.post(url_backend, json=dados)

            if response.status_code == 200:
                st.success("✅ Agendamento realizado com sucesso!")
            else:
                st.error("❌ Erro ao realizar agendamento. Tente novamente.")
        else:
            st.warning("⚠️ Por favor, preencha todos os campos obrigatórios.")

# Informações adicionais
st.markdown("---")
st.write("#### 📍 Nosso Endereço")
st.write("Rua do Açougue, 123 - Bairro Centro")
st.write("Telefone: (11) 1234-5678")

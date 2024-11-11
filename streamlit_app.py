import streamlit as st
import requests

# Configuração inicial da página com imagem de fundo
page_bg_img = '''
<style>
body {
    background-image: url("https://example.com/sua_imagem_de_fundo.jpg");
    background-size: cover;
    color: #ffffff;
}
.stApp {
    background-color: rgba(0, 0, 0, 0.7);  /* Fundo semi-transparente para melhor leitura */
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Configuração da página
st.set_page_config(page_title="AgendAçougue", page_icon="🥩", layout="centered")

# Título estilizado
st.markdown("<h1 style='text-align: center; color: #FF6347;'>AgendAçougue 🥩</h1>", unsafe_allow_html=True)
st.write("### Bem-vindo ao sistema de agendamento de serviços do AgendAçougue!")
st.write("Aproveite para agendar seu serviço com comodidade e praticidade.")

# Divisor visual
st.markdown("---")

# Dicionário com os serviços e seus respectivos preços
servicos = {
    "Corte Especial": 15.00,
    "Moagem de Carne": 10.00,
    "Embalagem a Vácuo": 12.50,
    "Desossa": 20.00,
    "Tempero Especial": 8.00,
    "Preparação de Hambúrguer": 18.00
}

# Formulário de agendamento com layout melhorado
with st.form(key="form_agendamento"):
    st.subheader("📝 Dados do Agendamento")
    
    # Campos do cliente
    nome = st.text_input("Nome", placeholder="Digite seu nome completo")
    email = st.text_input("Email", placeholder="Digite seu email")
    
    # Seleção de múltiplos serviços com preços
    servicos_selecionados = st.multiselect(
        "Escolha o(s) serviço(s) desejado(s)",
        options=[f"{servico} - R${preco:.2f}" for servico, preco in servicos.items()]
    )
    
    # Processa a lista de serviços selecionados para extrair nomes e calcular o total
    servico_nomes = [servico.split(" - ")[0] for servico in servicos_selecionados]
    preco_total = sum(servicos[servico] for servico in servico_nomes)

    # Exibição do valor total
    st.write(f"**Valor total dos serviços selecionados:** R$ {preco_total:.2f}")

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
        if nome and email and servico_nomes:
            # Dados a serem enviados para o backend
            dados = {
                "nome": nome,
                "email": email,
                "servicos": servico_nomes,
                "preco_total": preco_total,
                "data": str(data),
                "horario": str(horario),
                "pagamento": pagamento
            }

            # Substitua a URL abaixo pela URL real do backend caso tenha um.
            url_backend = "https://fpghdtrd5gtaxkph8kowdm.streamlit.app/"
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

# Redes sociais
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>Siga-nos nas redes sociais</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![Facebook](https://image.similarpng.com/very-thumbnail/2020/06/Facebook-logo-transparent-PNG.png)](https://www.facebook.com)")
with col2:
    st.markdown("[![Instagram](https://image.similarpng.com/very-thumbnail/2020/06/Instagram-logo-transparent-PNG.png)](https://www.instagram.com)")
with col3:
    st.markdown("[![Twitter](https://image.similarpng.com/very-thumbnail/2020/06/Twitter-logo-transparent-PNG.png)](https://www.twitter.com)")


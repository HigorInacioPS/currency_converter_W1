# Importa as bibliotecas necessárias
import streamlit as st
import requests

# Função que busca a taxa de câmbio na API com cache para evitar requisições repetidas
@st.cache_data
def obter_taxa_de_cambio(origem, destino):
    if origem == destino:
        return 1.0  # Retorna 1.0 se as moedas forem iguais (evita requisição desnecessária)

    url = f"https://api.frankfurter.app/latest?from={origem}&to={destino}"
    resposta = requests.get(url)
    if resposta.status_code != 200:
        raise Exception("Erro ao acessar a API.")
    dados = resposta.json()
    return dados['rates'][destino]

# Configurações da página (título e ícone)
st.set_page_config(page_title="Conversor de Moedas", page_icon="💱")
st.title("Conversor de Moedas 💱")

# Lista de moedas disponíveis para conversão
moedas = ["USD", "EUR", "BRL", "JPY", "GBP"]

# Elementos interativos da interface: seleção de moedas e valor
origem = st.selectbox("Moeda de origem", moedas)
destino = st.selectbox("Moeda de destino", moedas)
valor = st.number_input("Valor a ser convertido", min_value=0.0, format="%.2f")

# Botão que dispara a conversão
if st.button("Converter"):
    try:
        # Chama a função para obter a taxa e realiza a conversão
        taxa = obter_taxa_de_cambio(origem, destino)
        convertido = valor * taxa

        # Exibe o resultado da conversão
        st.success(f"{valor:.2f} {origem} = {convertido:.2f} {destino}")
    except Exception as e:
        # Exibe mensagem de erro caso haja problemas com a API ou entrada inválida
        st.error(f"Erro: {e}")

# Importa a biblioteca requests para fazer requisições HTTP à API

import requests

# Função para obter a taxa de câmbio entre duas moedas

def obter_taxa_de_cambio(origem, destino):
    url = f"https://api.frankfurter.app/latest?amount=1&from={origem}&to={destino}"   # Define a URL da API com os parâmetros de origem e destino
    resposta = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code != 200:                
        raise Exception("Erro ao acessar a API.")

    dados = resposta.json()

    # Verifica se a moeda de destino está presente nos dados retornados
    if destino not in dados["rates"]:                 
        raise Exception("Moeda de destino inválida.")

    # Retorna a taxa de câmbio
    return dados["rates"][destino]


# Função para validar se o valor digitado é um número positivo
def validar_valor(valor):
    try:
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")
        return valor
    except ValueError:
        raise ValueError("Entrada inválida. Digite um número válido.")

# Função principal do conversor de moedas no terminal
def conversor_moedas():
    print("=== Conversor de Moedas ===")
    origem = input("Moeda de origem (ex: USD): ").upper()
    destino = input("Moeda de destino (ex: BRL): ").upper()
    valor_str = input("Valor a ser convertido: ")

    try:
        # Valida o valor digitado pelo usuário
        valor = validar_valor(valor_str)
        
        # Obtém a taxa de câmbio e realiza a conversão
        taxa = obter_taxa_de_cambio(origem, destino)
        convertido = valor * taxa
        
        # Exibe o resultado formatado
        print(f"\n{valor:.2f} {origem} = {convertido:.2f} {destino}")
    except Exception as e:
        # Exibe mensagem de erro em caso de exceções
        print(f"\nErro: {e}")

# Ponto de entrada do programa
if __name__ == "__main__":
    conversor_moedas()

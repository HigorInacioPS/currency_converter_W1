# 💱 Conversor de Moedas

Este projeto é um **Conversor de Moedas** simples e eficiente, que consome dados em tempo real a partir da [API pública Frankfurter](https://www.frankfurter.app). O projeto foi desenvolvido em duas versões distintas:

- **Interface de Linha de Comando (CLI)** – para execução via terminal.
- **Aplicativo Web com Streamlit** – com interface gráfica amigável no navegador.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12.3
- [Requests](https://pypi.org/project/requests/) – para requisições HTTP
- [Streamlit](https://streamlit.io) – para criação da interface web

---

## 📦 Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

Se você não tiver um `requirements.txt`, instale manualmente:

```bash
pip install requests streamlit
```

---

## 🧪 Como Executar

### ▶️ Versão CLI (Terminal)

A versão de linha de comando permite conversão direta via terminal:

```bash
python conversor_terminal.py
```

**Funcionamento:**

1. O usuário informa a moeda de origem (ex: `USD`), a moeda de destino (ex: `BRL`) e o valor a ser convertido.
2. O script acessa a API e retorna o valor convertido.
3. Há validações para garantir que o valor seja numérico e positivo.
4. Mensagens de erro são exibidas em caso de falhas na API ou entradas inválidas.

---

### 🌐 Versão Web com Streamlit

Para rodar a interface gráfica com Streamlit:

```bash
streamlit run conversor_streamlit.py
```

**Funcionamento:**

1. O usuário interage com dropdowns e campos numéricos para selecionar as moedas e valor.
2. Ao clicar em "Converter", o app exibe o resultado da conversão.
3. O uso de `@st.cache_data` evita chamadas desnecessárias à API para a mesma conversão.
4. O layout é simples, intuitivo e funciona diretamente no navegador.

---

## ✅ Moedas Suportadas

- USD – Dólar Americano  
- EUR – Euro  
- BRL – Real Brasileiro  
- JPY – Iene Japonês  
- GBP – Libra Esterlina

---

## 📌 Observação

Este projeto faz parte de um **plano de estudos prático** em Python, voltado para desenvolvimento de aplicações reais com foco em **Dados**, **Backend** e **Inteligência Artificial**.  

Trata-se do **Projeto da Semana 1**, cujo principal objetivo foi:

- Praticar integração com **APIs públicas**
- Aplicar **validação de dados**
- Diferenciar o desenvolvimento de **interfaces em terminal e web**
- Familiarizar-se com **boas práticas de estruturação e comentários no código**

Outros projetos serão desenvolvidos nas semanas seguintes, com escopos progressivamente mais desafiadores.
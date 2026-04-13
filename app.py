import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import json

# 1. Configuração de acesso (Lendo do Cofre Secreto da Nuvem)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Pega o texto do segredo e transforma no formato que o Google entende
credenciais_dict = json.loads(st.secrets["google_credentials"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(credenciais_dict, scope)
client = gspread.authorize(creds)

planilha_id = "1XOBHOT0EDg0T09TBsD3Ie7vxkTqo4-f9gMfdhSVdqP0"
aba_familias = client.open_by_key(planilha_id).worksheet("Famílias")

# 2. UI/UX DESIGN
st.set_page_config(page_title="ATIPICONNECT", page_icon="🧩", layout="centered")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background: linear-gradient(-45deg, #FFF0F5, #E0FFFF, #F0F8FF, #FFF8DC) !important; background-size: 400% 400% !important; animation: gradientBG 15s ease infinite !important; }
    @keyframes gradientBG { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    [data-testid="stForm"] { background-color: rgba(255, 255, 255, 0.95) !important; border-radius: 25px !important; padding: 30px !important; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1) !important; border: 2px solid #FFFFFF !important; }
    .stMarkdown p, .stMarkdown span { color: #333333 !important; font-weight: 700 !important; }
    label, label p, label span, [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] { color: #333333 !important; font-weight: 800 !important; font-size: 1.05rem !important; }
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea { background-color: #FFFFFF !important; border: 2px solid #87CEFA !important; border-radius: 12px !important; }
    div[data-baseweb="input"] input, div[data-baseweb="select"] div, textarea { color: #1A1A1A !important; font-weight: 600 !important; }
    div[data-baseweb="input"] > div:focus-within, textarea:focus { border-color: #FF8C00 !important; }
    [data-testid="stFormSubmitButton"] > button { background: linear-gradient(45deg, #FF8C00, #FFA500) !important; color: #FFFFFF !important; border-radius: 50px !important; border: none !important; font-weight: 900 !important; font-size: 1.2rem !important; padding: 10px 20px !important; width: 100% !important; margin-top: 20px !important; box-shadow: 0 8px 15px rgba(255, 140, 0, 0.3) !important; text-transform: uppercase !important; letter-spacing: 1px !important; }
    [data-testid="stFormSubmitButton"] > button:hover { transform: translateY(-3px) !important; background: linear-gradient(45deg, #FFA500, #FF8C00) !important; color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Títulos Blindados
st.markdown("<h1 style='color: #FF8C00; text-align: center; font-weight: 900; font-size: 3.5rem; margin-bottom: 0;'>🧩 ATIPICONNECT</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #4682B4; text-align: center; font-weight: 700; margin-top: 0;'>🌈 Acolhimento, Inclusão e Desenvolvimento</h3>", unsafe_allow_html=True)
st.write("")

st.info("✨ **Como funciona?** 1️⃣ Cadastre a criança. 2️⃣ Nossa IA entende a necessidade. 3️⃣ Conectamos aos melhores especialistas!")
st.write("")

with st.form("cadastro_familia", clear_on_submit=True):
    st.markdown("<h4 style='color: #333333;'>🦸‍♀️ Quem está cuidando hoje?</h4>", unsafe_allow_html=True)
    nome_resp = st.text_input("Seu Nome Completo", placeholder="Como gosta de ser chamado?")
    
    col1, col2 = st.columns(2)
    with col1:
        email_resp = st.text_input("💌 Seu melhor E-mail")
    with col2:
        telefone = st.text_input("📱 WhatsApp")
    
    cidade = st.text_input("📍 Onde vocês moram? (Cidade / Estado)")
    
    st.write("---")
    st.markdown("<h4 style='color: #333333;'>🌟 O grande astro (Perfil da Criança)</h4>", unsafe_allow_html=True)
    nome_crianca = st.text_input("Nome da Criança", placeholder="Qual o nome da fera?")
    diagnostico = st.text_area("🧠 Conta um pouquinho sobre o diagnóstico")
    
    necessidade = st.selectbox(
        "🎯 Do que vocês mais precisam no momento?", 
        ["Fonoaudiologia 🗣️", "Fisioterapia 🏃‍♂️", "Pediatria 🩺", "Neurologia 🧠", "Terapia Ocupacional 👐", "Psicologia 🛋️"]
    )
    
    st.write("")
    submit_button = st.form_submit_button("🚀 CRIAR PERFIL AGORA")

if submit_button:
    if nome_resp and nome_crianca:
        progress_bar = st.progress(0)
        st.success("Preparando a magia...")
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
            
        nova_linha = [nome_resp, email_resp, telefone, cidade, nome_crianca, diagnostico, "", necessidade, ""]
        aba_familias.append_row(nova_linha)
        
        st.balloons()
        st.success("🎉 Deu tudo certo! O perfil já está na nossa rede de apoio.")
    else:
        st.error("🙈 Ops! Parece que você esqueceu de colocar o seu nome e o da criança.")

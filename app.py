import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import json

# 1. Configuração de acesso
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

try:
    if "google_credentials" in st.secrets:
        cred_info = json.loads(st.secrets["google_credentials"])
    else:
        with open("credenciais.json") as f:
            cred_info = json.load(f)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(cred_info, scope)
    client = gspread.authorize(creds)
    planilha_id = "1XOBHOT0EDg0T09TBsD3Ie7vxkTqo4-f9gMfdhSVdqP0"
    aba_familias = client.open_by_key(planilha_id).worksheet("Famílias")
except Exception as e:
    st.error(f"Erro na conexão com a planilha: {e}")

# 2. UI/UX DESIGN (Totalmente unificado para não quebrar no Streamlit)
st.set_page_config(page_title="ATIPICONNECT", page_icon="🧩", layout="centered")

st.markdown("""
    <style>
    /* Fundo Animado */
    [data-testid="stAppViewContainer"] { background: linear-gradient(-45deg, #F0F8FF, #E0FFFF, #FFF0F5, #FFF8DC) !important; background-size: 400% 400% !important; animation: gradientBG 15s ease infinite !important; }
    @keyframes gradientBG { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    
    /* Reset de textos nativos */
    .stMarkdown p, .stMarkdown label, .stMarkdown span { color: #333333 !important; font-weight: 700 !important; }
    [data-testid="stWidgetLabel"] p { color: #333333 !important; font-weight: 800 !important; font-size: 1.05rem !important; }
    
    /* Inputs */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea { background-color: #FFFFFF !important; border: 2px solid #87CEFA !important; border-radius: 12px !important; }
    div[data-baseweb="input"] input, div[data-baseweb="select"] div, textarea { color: #1A1A1A !important; font-weight: 600 !important; }
    div[data-baseweb="input"] > div:focus-within, textarea:focus { border-color: #FF8C00 !important; }
    
    /* Card de Formulário */
    [data-testid="stForm"] { background-color: rgba(255, 255, 255, 0.95) !important; border-radius: 25px !important; padding: 30px !important; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05) !important; border: 2px solid #FFFFFF !important; }
    
    /* Botões Form */
    [data-testid="stFormSubmitButton"] > button { background: linear-gradient(45deg, #FF8C00, #FFA500) !important; color: #FFFFFF !important; border-radius: 50px !important; border: none !important; font-weight: 900 !important; font-size: 1.2rem !important; padding: 10px 20px !important; width: 100% !important; margin-top: 20px !important; box-shadow: 0 8px 15px rgba(255, 140, 0, 0.3) !important; text-transform: uppercase !important; letter-spacing: 1px !important; }
    [data-testid="stFormSubmitButton"] > button:hover { transform: translateY(-3px) !important; background: linear-gradient(45deg, #FFA500, #FF8C00) !important; }
    
    /* Modificações das Abas (Tabs) para visual mais limpo */
    [data-testid="stTabs"] button { font-weight: 700 !important; color: #666 !important; }
    [data-testid="stTabs"] button[aria-selected="true"] { color: #FF8C00 !important; border-bottom-color: #FF8C00 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho Central
st.markdown("<h1 style='color: #FF8C00; text-align: center; font-weight: 900; font-size: 3.2rem; margin-bottom: 0;'>🧩 ATIPICONNECT</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #4682B4; text-align: center; font-weight: 700; margin-top: 0;'>🌈 Acolhimento, Inclusão e Desenvolvimento</h3>", unsafe_allow_html=True)
st.write("")

# 4. Sistema de Navegação (Abas)
tab1, tab2, tab3 = st.tabs(["🏠 Início", "📋 Cadastro", "🔍 Buscar Profissionais"])

with tab1:
    # Card da Ana Paula 100% HTML integrado (Foto + Texto juntos)
    st.markdown("""
        <div style="background-color: rgba(255, 255, 255, 0.95); border-radius: 20px; padding: 25px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 20px; margin-bottom: 20px; border-left: 6px solid #FF8C00;">
            <img src="https://i.pravatar.cc/150?img=47" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 3px solid #FF8C00; flex-shrink: 0;">
            <div>
                <h4 style="color: #333333; font-weight: 800; margin: 0 0 5px 0; font-size: 1.2rem;">Olá, sou a Ana Paula! 👩🏻</h4>
                <p style="color: #666666; font-weight: 600; margin: 0; font-size: 0.95rem; line-height: 1.4;">Seja bem-vinda à nossa rede de apoio. Aqui você encontra especialistas e outras famílias para compartilhar experiências e fortalecer o desenvolvimento do seu pequeno.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("✨ **Como funciona?** 1️⃣ Cadastre a criança no menu ao lado. 2️⃣ Nossa IA entende a necessidade. 3️⃣ Conectamos aos melhores especialistas!")

with tab2:
    with st.form("cadastro_familia", clear_on_submit=True):
        st.markdown("<h4 style='color: #333333; font-weight: 800; margin-bottom: 15px;'>🦸‍♀️ Quem está cuidando hoje?</h4>", unsafe_allow_html=True)
        nome_resp = st.text_input("Seu Nome Completo", placeholder="Ex: Maria Silva")
        col1, col2 = st.columns(2)
        with col1:
            email_resp = st.text_input("💌 Seu melhor E-mail")
        with col2:
            telefone = st.text_input("📱 WhatsApp")
        cidade = st.text_input("📍 Onde vocês moram? (Cidade / Estado)")
        
        st.write("---")
        st.markdown("<h4 style='color: #333333; font-weight: 800; margin-bottom: 15px;'>🌟 O grande astro (Perfil da Criança)</h4>", unsafe_allow_html=True)
        nome_crianca = st.text_input("Nome da Criança", placeholder="Qual o nome da fera?")
        diagnostico = st.text_area("🧠 Conta um pouquinho sobre o diagnóstico")
        necessidade = st.selectbox("🎯 Do que vocês mais precisam no momento?", ["Fonoaudiologia 🗣️", "Fisioterapia 🏃‍♂️", "Pediatria 🩺", "Neurologia 🧠", "Terapia Ocupacional 👐", "Psicologia 🛋️"])
        
        submit_button = st.form_submit_button("🚀 CRIAR PERFIL AGORA")

with tab3:
    st.markdown("<h4 style='color: #333333; font-weight: 800; margin-bottom: 15px;'>Especialistas em Destaque</h4>", unsafe_allow_html=True)
    
    # Lista de profissionais com layout de Cartão HTML perfeito (sem usar st.columns)
    profissionais = [
        {"nome": "Dra. Marina Lopes", "esp": "Fonoaudióloga", "estrela": "4.9", "img": "https://i.pravatar.cc/150?img=32"},
        {"nome": "Dr. Daniel Ferreira", "esp": "Fisioterapeuta", "estrela": "5.0", "img": "https://i.pravatar.cc/150?img=11"},
        {"nome": "Dra. Thais Cardoso", "esp": "Psicóloga Infantil", "estrela": "4.8", "img": "https://i.pravatar.cc/150?img=5"}
    ]
    
    for p in profissionais:
        st.markdown(f"""
            <div style="background-color: rgba(255, 255, 255, 0.95); border-radius: 15px; padding: 15px 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px; border-left: 5px solid #00BFFF;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <img src="{p['img']}" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 2px solid #E0E0E0; flex-shrink: 0;">
                    <div>
                        <div style="color: #333333; font-weight: 800; font-size: 1.1rem;">{p['nome']}</div>
                        <div style="color: #666666; font-weight: 600; font-size: 0.9rem;">{p['esp']}</div>
                    </div>
                </div>
                <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
                    <div style="background: #FFF5E6; color: #FF8C00; padding: 4px 10px; border-radius: 10px; font-weight: 800; font-size: 0.85rem; display: inline-block;">⭐ {p['estrela']}</div>
                    <div style="background: #00BFFF; color: white; padding: 6px 12px; border-radius: 8px; font-weight: 700; font-size: 0.8rem; display: inline-block; cursor: pointer;">Ver Perfil</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Lógica de salvar (fora das abas para funcionar corretamente)
if 'submit_button' in locals() and submit_button:
    if nome_resp and nome_crianca:
        with st.spinner("Preparando a magia..."):
            time.sleep(1.5) # Simula o tempo
            nova_linha = [nome_resp, email_resp, telefone, cidade, nome_crianca, diagnostico, "", necessidade, ""]
            aba_familias.append_row(nova_linha)
        st.balloons()
        st.success("🎉 Deu tudo certo! O perfil já está na nossa rede de apoio.")
    else:
        st.error("🙈 Ops! Parece que você esqueceu de colocar o seu nome e o da criança.")

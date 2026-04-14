import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import json
import base64

# 1. Configuração de acesso (Mantenha o JSON na nuvem ou no arquivo conforme configurado)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

try:
    # Tenta ler do Secrets (Nuvem) ou arquivo local (PC) para facilitar seu teste
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
    # Mostra erro na tela se não conseguir conectar
    st.error(f"Erro na conexão com a planilha: {e}")

# 2. UI/UX DESIGN Blindado (Sem linhas em branco e cores forçadas)
st.set_page_config(page_title="ATIPICONNECT", page_icon="🧩", layout="centered")

# CSS Compactado e Blindado
st.markdown("""
    <style>
    /* Fundo Animado Forçado */
    [data-testid="stAppViewContainer"] { background: linear-gradient(-45deg, #FFF0F5, #E0FFFF, #F0F8FF, #FFF8DC) !important; background-size: 400% 400% !important; animation: gradientBG 15s ease infinite !important; }
    @keyframes gradientBG { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    
    /* Card Central (Fundo Branco Forçado) */
    [data-testid="stForm"] { background-color: rgba(255, 255, 255, 0.95) !important; border-radius: 25px !important; padding: 30px !important; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1) !important; border: 2px solid #FFFFFF !important; }
    
    /* Títulos Blindados com HTML */
    .stMarkdown h1, .stMarkdown h3, .stMarkdown h4 { text-align: center; }
    
    /* Força os textos comuns a ficarem escuros */
    .stMarkdown p, .stMarkdown label, .stMarkdown span { color: #333333 !important; font-weight: 700 !important; }
    
    /* CORREÇÃO DOS LABELS: Força as perguntas a ficarem escuras e legíveis */
    [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] { color: #333333 !important; font-weight: 800 !important; font-size: 1.05rem !important; }
    
    /* Caixas de Texto (Impedindo o fundo preto do dark mode) */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea { background-color: #FFFFFF !important; border: 2px solid #87CEFA !important; border-radius: 12px !important; }
    div[data-baseweb="input"] input, div[data-baseweb="select"] div, textarea { color: #1A1A1A !important; font-weight: 600 !important; }
    div[data-baseweb="input"] > div:focus-within, textarea:focus { border-color: #FF8C00 !important; }
    
    /* Botão Vibrante */
    [data-testid="stFormSubmitButton"] > button { background: linear-gradient(45deg, #FF8C00, #FFA500) !important; color: #FFFFFF !important; border-radius: 50px !important; border: none !important; font-weight: 900 !important; font-size: 1.2rem !important; padding: 10px 20px !important; width: 100% !important; margin-top: 20px !important; box-shadow: 0 8px 15px rgba(255, 140, 0, 0.3) !important; text-transform: uppercase !important; letter-spacing: 1px !important; }
    [data-testid="stFormSubmitButton"] > button:hover { transform: translateY(-3px) !important; background: linear-gradient(45deg, #FFA500, #FF8C00) !important; color: #FFFFFF !important; }
    
    /* Cartões de Profissionais */
    .prof-card { background: white; padding: 20px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); margin-bottom: 15px; border-left: 6px solid #FF8C00; }
    </style>
""", unsafe_allow_html=True)

# 3. Conteúdo da Interface Blindado com HTML
st.markdown("<h1 style='color: #FF8C00; text-align: center; font-weight: 900; font-size: 3.5rem; margin-bottom: 0;'>🧩 ATIPICONNECT</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #4682B4; text-align: center; font-weight: 700; margin-top: 0;'>🌈 Acolhimento, Inclusão e Desenvolvimento</h3>", unsafe_allow_html=True)
st.write("")

# Abas para simular a navegação do design
tab1, tab2, tab3 = st.tabs(["🏠 Início", "📋 Cadastro", "🔍 Buscar Profissionais"])

with tab1:
    # Bem-vinda com imagem livre (Pexels)
    st.image("https://images.pexels.com/photos/1239291/pexels-photo-1239291.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", width=150)
    st.markdown("""
    <div class="prof-card">
        <h4 style="color: #333333; font-weight: 900;">Olá, sou a Ana Paula! 👩🏻</h4>
        <p style="color: #666666; font-weight: 600;">Seja bem-vinda à nossa rede de apoio. Aqui você encontra especialistas e outras famílias para compartilhar experiências.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Caixa de Dica Blindada
    st.info("✨ **Como funciona?** 1️⃣ Cadastre a criança. 2️⃣ Nossa IA entende a necessidade. 3️⃣ Conectamos aos melhores especialistas!")
    st.write("")

with tab2:
    with st.form("cadastro_familia", clear_on_submit=True):
        st.markdown("<h4 style='color: #333333; font-weight: 800; text-align: left; margin-bottom: 15px;'>🦸‍♀️ Quem está cuidando hoje?</h4>", unsafe_allow_html=True)
        nome_resp = st.text_input("Seu Nome Completo", placeholder="Como gosta de ser chamado?")
        
        col1, col2 = st.columns(2)
        with col1:
            email_resp = st.text_input("💌 Seu melhor E-mail")
        with col2:
            telefone = st.text_input("📱 WhatsApp")
        
        cidade = st.text_input("📍 Onde vocês moram? (Cidade / Estado)", placeholder="Ex: Campo Grande, MS")
        
        st.write("---")
        st.markdown("<h4 style='color: #333333; font-weight: 800; text-align: left; margin-bottom: 15px;'>🌟 O grande astro (Perfil da Criança)</h4>", unsafe_allow_html=True)
        nome_crianca = st.text_input("Nome da Criança", placeholder="Qual o nome da fera?")
        diagnostico = st.text_area("🧠 Conta um pouquinho sobre o diagnóstico")
        
        necessidade = st.selectbox(
            "🎯 Do que vocês mais precisam no momento?", 
            ["Fonoaudiologia 🗣️", "Fisioterapia 🏃‍♂️", "Pediatria 🩺", "Neurologia 🧠", "Terapia Ocupacional 👐", "Psicologia 🛋️"]
        )
        
        st.write("")
        submit_button = st.form_submit_button("🚀 CRIAR PERFIL AGORA")

with tab3:
    # Título da listagem forçado escuro
    st.markdown("<h4 style='color: #333333; font-weight: 800; text-align: left; margin-bottom: 15px;'>Especialistas Recomendados (Mock)</h4>", unsafe_allow_html=True)
    
    # Simulação da lista de profissionais do design com imagens livres
    profissionais = [
        {"nome": "Dra. Marina Lopes", "esp": "Fonoaudióloga", "estrela": "⭐ 4.9", "img": "https://images.pexels.com/photos/5212320/pexels-photo-5212320.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},
        {"nome": "Dr. Daniel Ferreira", "esp": "Fisioterapeuta", "estrela": "⭐ 5.0", "img": "https://images.pexels.com/photos/7476839/pexels-photo-7476839.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},
        {"nome": "Dra. Thais Cardoso", "esp": "Psicóloga Infantil", "estrela": "⭐ 4.8", "img": "https://images.pexels.com/photos/5341381/pexels-photo-5341381.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}
    ]
    
    for p in profissionais:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(p['img'], width=60)
        with col2:
            st.markdown(f"""
            <div class="prof-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <b style="color: #333; font-size: 1.1rem;">{p['nome']}</b><br>
                        <span style="color: #666;">{p['esp']}</span>
                    </div>
                    <div style="background: #FFF5E6; color: #FF8C00; padding: 5px 12px; border-radius: 10px; font-weight: bold;">
                        {p['estrela']}
                    </div>
                </div>
                <button style="margin-top: 10px; background: #00BFFF; color: white; border: none; padding: 5px 15px; border-radius: 8px; font-size: 0.8rem; cursor: pointer;">Ver Perfil</button>
            </div>
            """, unsafe_allow_html=True)

# 4. Lógica de Envio para a Planilha (Gatilho fora do loop de layout)
if 'submit_button' in locals() and submit_button:
    if nome_resp and nome_crianca:
        # Mostra o progresso de forma visível
        with st.spinner("Preparando a magia..."):
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
            
            nova_linha = [nome_resp, email_resp, telefone, cidade, nome_crianca, diagnostico, "", necessidade, ""]
            aba_familias.append_row(nova_linha)
        
        st.balloons()
        st.success("🎉 Deu tudo certo! O perfil já está na nossa rede de apoio.")
    else:
        st.error("🙈 Ops! Parece que você esqueceu de colocar o seu nome e o da criança.")

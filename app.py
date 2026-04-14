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

# 2. UI/UX DESIGN (LAYOUT MOBILE APP BLINDADO)
st.set_page_config(page_title="ATIPICONNECT", page_icon="🧩", layout="centered")

# CSS para Simulação Mobile e Navegação Inferior
st.markdown("""
    <style>
    /* Carregar fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
    
    * { font-family: 'Poppins', sans-serif !important; }

    /* Fundo Azul Clarinho Global (Fundo do Telefone) */
    [data-testid="stAppViewContainer"] { 
        background-color: #EAF4FB !important; 
        padding-bottom: 80px !important; /* Espaço para a nav-bar fixa */
    }
    
    /* RESET DE TEXTOS: Blindando contra Modo Escuro (Sempre Escuros) */
    h1 { color: #FF8C00 !important; font-weight: 800 !important; font-size: 2.2rem !important; margin-bottom: 0px !important;}
    h3 { color: #4682B4 !important; font-weight: 600 !important; font-size: 1rem !important; margin-top: 0px !important;}
    label p, label span, .stMarkdown p, .stMarkdown li, [data-testid="stWidgetLabel"] p {
        color: #2D3748 !important; /* Texto Escuro/Visível */
        font-weight: 700 !important; 
        font-size: 0.95rem !important; 
    }
    
    /* Inputs Minimalistas */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea { 
        background-color: #FFFFFF !important;
        border: 1px solid #D0E3F0 !important;
        border-radius: 12px !important; 
        box-shadow: none !important;
        transition: 0.3s;
    }
    div[data-baseweb="input"] input, div[data-baseweb="select"] div, textarea { 
        color: #1A1A1A !important; 
        font-weight: 600 !important; 
    }
    div[data-baseweb="input"] > div:focus-within, textarea:focus { border-color: #FF8C00 !important; }
    
    /* Card de Formulário Branco */
    [data-testid="stForm"] { 
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        padding: 25px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03) !important;
        border: none !important;
        margin-top: 10px !important;
    }
    
    /* Botão Principal Mobile */
    [data-testid="stFormSubmitButton"] > button { 
        background: linear-gradient(135deg, #FF8C00, #FF6B00) !important;
        color: #FFFFFF !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: 800 !important;
        font-size: 1rem !important;
        padding: 10px 20px !important;
        width: 100% !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 12px rgba(255, 140, 0, 0.2) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    [data-testid="stFormSubmitButton"] > button:hover { transform: translateY(-2px); }

    /* Barra de Navegação Inferior FIXA (Simulação Mobile) */
    .mobile-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 70px;
        background: white;
        display: flex;
        justify-content: space-around;
        align-items: center;
        box-shadow: 0 -4px 15px rgba(0,0,0,0.05);
        z-index: 1000;
        border-radius: 20px 20px 0 0;
    }
    .nav-item {
        text-align: center;
        color: #718096;
        cursor: pointer;
    }
    .nav-item.active {
        color: #FF8C00;
        font-weight: 800;
    }
    .nav-icon {
        font-size: 1.5rem;
    }
    .nav-label {
        font-size: 0.75rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho Central
st.markdown("<h1 style='text-align: center;'>🧩 ATIPICONNECT</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Acolhimento & Desenvolvimento</h3>", unsafe_allow_html=True)
st.write("")

# 4. Conteúdo Principal (Simulando uma única tela mobile: Cadastro)
st.markdown("#### 📋 Cadastro da Família", unsafe_allow_html=True)

with st.form("cadastro_familia", clear_on_submit=True):
    st.markdown("#### 👤 Responsável", unsafe_allow_html=True)
    nome_resp = st.text_input("Nome Completo", placeholder="Ex: Maria Silva")
    
    col1, col2 = st.columns(2)
    with col1:
        email_resp = st.text_input("💌 Seu melhor E-mail")
    with col2:
        telefone = st.text_input("📱 WhatsApp")
    
    cidade = st.text_input("📍 Onde vocês moram? (Cidade / Estado)", placeholder="Ex: Campo Grande, MS")
    
    st.write("---")
    st.markdown("#### 🧸 Perfil da Criança", unsafe_allow_html=True)
    nome_crianca = st.text_input("Nome da Criança", placeholder="Qual o nome da fera?")
    diagnostico = st.text_area("🧠 Conta um pouquinho sobre o diagnóstico", help="Pode ser breve! Estamos aqui para entender e ajudar.")
    
    necessidade = st.selectbox("Qual acompanhamento você busca hoje?", ["Neuropediatria", "Psiquiatria Infantil", "Fonoaudiologia", "Fisioterapia", "Terapia Ocupacional", "Psicologia"])
    
    st.write("")
    submit_button = st.form_submit_button("🚀 CRIAR PERFIL AGORA")

# 5. Lógica de salvar
if 'submit_button' in locals() and submit_button:
    if nome_resp and nome_crianca:
        with st.spinner("Salvando no sistema..."):
            nova_linha = [nome_resp, email_resp, telefone, cidade, nome_crianca, diagnostico, "", necessidade, ""]
            aba_familias.append_row(nova_linha)
        st.balloons()
        st.success("✅ Perfil criado com sucesso na rede de apoio!")
    else:
        st.error("🙈 Ops! Parece que você esqueceu de colocar o seu nome e o da criança.")

# 6. Barra de Navegação Inferior FIXA (Totalmente em HTML/CSS)
st.markdown("""
    <div class="mobile-nav">
        <div class="nav-item">
            <div class="nav-icon">🏠</div>
            <div class="nav-label">Início</div>
        </div>
        <div class="nav-item active">
            <div class="nav-icon">📋</div>
            <div class="nav-label">Cadastro</div>
        </div>
        <div class="nav-item">
            <div class="nav-icon">🔍</div>
            <div class="nav-label">Buscar</div>
        </div>
        <div class="nav-item">
            <div class="nav-icon">❤️</div>
            <div class="nav-label">Doações</div>
        </div>
        <div class="nav-item">
            <div class="nav-icon">💬</div>
            <div class="nav-label">Chat</div>
        </div>
    </div>
""", unsafe_allow_html=True)

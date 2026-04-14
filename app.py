import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# 1. Configuração de Acesso (Google Sheets via Secrets)
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
    st.error(f"Erro na conexão: {e}")

# 2. UI/UX DESIGN (Inspirado no Design Vibrante)
st.set_page_config(page_title="AtipiConnect", page_icon="🧩", layout="centered")

st.markdown("""
    <style>
    /* Importação de fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
    
    * { font-family: 'Poppins', sans-serif !important; }

    /* Fundo com gradiente suave */
    .stApp {
        background: linear-gradient(135deg, #F0F4F8 0%, #E1EFFF 100%);
    }

    /* Estilo dos Títulos e Textos */
    h1 { color: #FF8C00 !important; font-weight: 800 !important; font-size: 2.5rem !important; margin-bottom: 0px !important; }
    h3 { color: #00BFFF !important; font-weight: 600 !important; font-size: 1.2rem !important; }
    label { color: #333333 !important; font-weight: 600 !important; }

    /* Cartões de Profissionais e Formulário */
    .prof-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-left: 6px solid #FF8C00;
    }

    /* Input Fields Customizados */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea {
        background-color: white !important;
        border: 2px solid #E0E0E0 !important;
        border-radius: 12px !important;
        transition: 0.3s;
    }
    div[data-baseweb="input"] > div:focus-within {
        border-color: #00BFFF !important;
    }

    /* Botão Principal Vibrante */
    .stButton>button {
        background: linear-gradient(90deg, #FF8C00 0%, #FFA500 100%);
        color: white !important;
        border: none;
        border-radius: 15px;
        padding: 15px 30px;
        font-weight: 700;
        font-size: 1.1rem;
        width: 100%;
        box-shadow: 0 5px 15px rgba(255, 140, 0, 0.3);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(255, 140, 0, 0.4);
    }

    /* Barra de Navegação Inferior (Simulação Visual) */
    .nav-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: white;
        padding: 15px;
        display: flex;
        justify-content: space-around;
        box-shadow: 0 -5px 20px rgba(0,0,0,0.05);
        z-index: 100;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho Dinâmico
st.markdown("<h1>AtipiConnect</h1>", unsafe_allow_html=True)
st.markdown("<h3>Cuidando de quem cuida 🧩</h3>", unsafe_allow_html=True)

# Tabs para simular a navegação do design
tab1, tab2, tab3 = st.tabs(["🏠 Início", "📋 Cadastro", "🔍 Buscar Profissionais"])

with tab1:
    st.markdown("""
    <div class="prof-card">
        <h4>Olá, sou a Ana Paula! 👩‍🦰</h4>
        <p>Seja bem-vinda à nossa rede de apoio. Aqui você encontra especialistas e outras famílias para compartilhar experiências.</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("💡 **Dica:** Complete o perfil da criança no menu 'Cadastro' para receber recomendações personalizadas.")

with tab2:
    with st.form("form_cadastro"):
        st.markdown("#### Perfil da Família")
        nome = st.text_input("Seu Nome")
        whats = st.text_input("WhatsApp")
        
        st.write("---")
        st.markdown("#### Perfil da Criança")
        nome_c = st.text_input("Nome da Criança")
        diag = st.text_area("Diagnóstico ou Necessidades")
        
        servico = st.selectbox("O que você procura?", ["Fonoaudiologia", "Fisioterapia", "Psicologia", "Neurologia"])
        
        enviar = st.form_submit_button("CRIAR PERFIL AGORA")
        
        if enviar:
            if nome and nome_c:
                aba_familias.append_row([nome, "", whats, "", nome_c, diag, "", servico, ""])
                st.balloons()
                st.success("Cadastro realizado! Vá para 'Buscar Profissionais' para ver o match.")

with tab3:
    st.markdown("#### Especialistas Recomendados em Campo Grande, MS")
    
    # Simulação da lista de profissionais do design
    profissionais = [
        {"nome": "Dra. Marina Lopes", "esp": "Fonoaudióloga", "estrela": "⭐ 4.9"},
        {"nome": "Dr. Daniel Ferreira", "esp": "Fisioterapeuta", "estrela": "⭐ 5.0"},
        {"nome": "Dra. Thais Cardoso", "esp": "Psicóloga Infantil", "estrela": "⭐ 4.8"}
    ]
    
    for p in profissionais:
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

# Espaçamento para a barra de navegação não cobrir o conteúdo
st.write("<br><br><br>", unsafe_allow_html=True)

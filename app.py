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

# 2. UI/UX DESIGN (Estilo Mobile App)
st.set_page_config(page_title="ATIPICONNECT", page_icon="🧩", layout="centered")

st.markdown("""
    <style>
    /* Fundo Azul Clarinho (Estilo App) */
    [data-testid="stAppViewContainer"] { background-color: #EAF4FB !important; }
    
    /* Reset de textos nativos */
    .stMarkdown p, .stMarkdown label, .stMarkdown span { color: #333333 !important; font-weight: 600 !important; }
    [data-testid="stWidgetLabel"] p { color: #333333 !important; font-weight: 700 !important; font-size: 1rem !important; }
    
    /* Inputs Estilo Mobile */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea { background-color: #FFFFFF !important; border: 1px solid #D0E3F0 !important; border-radius: 16px !important; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02) !important; padding: 4px !important; }
    div[data-baseweb="input"] input, div[data-baseweb="select"] div, textarea { color: #1A1A1A !important; font-weight: 600 !important; }
    div[data-baseweb="input"] > div:focus-within, textarea:focus { border-color: #4682B4 !important; }
    
    /* Card de Formulário Branco */
    [data-testid="stForm"] { background-color: #FFFFFF !important; border-radius: 24px !important; padding: 25px !important; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04) !important; border: none !important; margin-top: 10px !important;}
    
    /* Botão Principal Estilo Mobile App */
    [data-testid="stFormSubmitButton"] > button { background: linear-gradient(135deg, #FF8C00, #FF6B00) !important; color: #FFFFFF !important; border-radius: 30px !important; border: none !important; font-weight: 800 !important; font-size: 1.1rem !important; padding: 12px 20px !important; width: 100% !important; margin-top: 15px !important; box-shadow: 0 6px 16px rgba(255, 140, 0, 0.25) !important; text-transform: uppercase !important; letter-spacing: 0.5px !important; transition: all 0.2s ease !important; }
    [data-testid="stFormSubmitButton"] > button:active { transform: scale(0.98) !important; }
    
    /* Estilo das Abas (Simulando Menu Superior de App) */
    [data-testid="stTabs"] button { font-weight: 700 !important; color: #88A5BC !important; font-size: 0.95rem !important; padding-bottom: 10px !important;}
    [data-testid="stTabs"] button[aria-selected="true"] { color: #4682B4 !important; border-bottom: 3px solid #FF8C00 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho Central
st.markdown("<h1 style='color: #FF8C00; text-align: center; font-weight: 900; font-size: 2.8rem; margin-bottom: 0;'>🧩 ATIPICONNECT</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #4682B4; text-align: center; font-weight: 700; margin-top: 0; font-size: 1.1rem;'>Acolhimento & Desenvolvimento</h3>", unsafe_allow_html=True)
st.write("")

# 4. Navegação Principal
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Início", "📋 Cadastro", "👨‍⚕️ Médicos", "🧸 Histórias"])

with tab1:
    # Boas-vindas
    st.markdown("""
        <div style="background-color: #FFFFFF; border-radius: 20px; padding: 20px; box-shadow: 0 6px 16px rgba(0,0,0,0.04); display: flex; align-items: center; gap: 15px; margin-bottom: 15px; border-left: 5px solid #FF8C00;">
            <img src="https://i.pravatar.cc/150?img=47" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 2px solid #FF8C00; flex-shrink: 0;">
            <div>
                <h4 style="color: #333333; font-weight: 800; margin: 0 0 4px 0; font-size: 1.1rem;">Olá, sou a Ana Paula!</h4>
                <p style="color: #666666; font-weight: 500; margin: 0; font-size: 0.9rem; line-height: 1.4;">Seja bem-vinda ao nosso app. Aqui você não está sozinha na jornada do seu pequeno.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Dica Rápida:** Vá na aba **Cadastro** para preencher o perfil da criança e começarmos o acompanhamento.")

with tab2:
    with st.form("cadastro_familia", clear_on_submit=True):
        st.markdown("<h4 style='color: #4682B4; font-weight: 800; margin-bottom: 10px; font-size: 1.1rem;'>Responsável</h4>", unsafe_allow_html=True)
        nome_resp = st.text_input("Nome Completo", placeholder="Ex: Maria Silva")
        col1, col2 = st.columns(2)
        with col1:
            email_resp = st.text_input("E-mail")
        with col2:
            telefone = st.text_input("WhatsApp")
        cidade = st.text_input("Cidade / Estado")
        
        st.markdown("<h4 style='color: #4682B4; font-weight: 800; margin-top: 15px; margin-bottom: 10px; font-size: 1.1rem;'>Perfil da Criança</h4>", unsafe_allow_html=True)
        nome_crianca = st.text_input("Nome da Criança")
        diagnostico = st.text_area("Breve relato sobre o diagnóstico")
        necessidade = st.selectbox("Especialidade principal procurada", ["Neuropediatria", "Psiquiatria Infantil", "Fonoaudiologia", "Fisioterapia", "Terapia Ocupacional", "Psicologia"])
        
        submit_button = st.form_submit_button("CRIAR PERFIL AGORA")

with tab3:
    st.markdown("<h4 style='color: #333333; font-weight: 800; margin-bottom: 15px;'>Corpo Clínico</h4>", unsafe_allow_html=True)
    
    medicos = [
        {"nome": "Dr. Carlos Mendes", "esp": "Neuropediatra", "crm": "CRM 45892", "img": "https://i.pravatar.cc/150?img=11"},
        {"nome": "Dra. Juliana Castro", "esp": "Psiquiatra Infantil", "crm": "CRM 67123", "img": "https://i.pravatar.cc/150?img=32"},
        {"nome": "Dra. Renata Alves", "esp": "Fonoaudióloga", "crm": "CRFa 1245", "img": "https://i.pravatar.cc/150?img=5"}
    ]
    
    for m in medicos:
        st.markdown(f"""
            <div style="background-color: #FFFFFF; border-radius: 18px; padding: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.04); display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="{m['img']}" style="width: 55px; height: 55px; border-radius: 50%; object-fit: cover; border: 2px solid #E0E0E0; flex-shrink: 0;">
                    <div>
                        <div style="color: #333333; font-weight: 800; font-size: 1.05rem;">{m['nome']}</div>
                        <div style="color: #4682B4; font-weight: 700; font-size: 0.85rem;">{m['esp']}</div>
                        <div style="color: #999999; font-weight: 600; font-size: 0.75rem;">{m['crm']}</div>
                    </div>
                </div>
                <div style="background: #EAF4FB; color: #4682B4; padding: 8px; border-radius: 50%; cursor: pointer;">
                    📅
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("<h4 style='color: #333333; font-weight: 800; margin-bottom: 15px;'>Inpirações Reais</h4>", unsafe_allow_html=True)
    
    historias = [
        {
            "nome": "Leo, 5 anos", 
            "diag": "Autismo (TEA)", 
            "texto": "Após 6 meses de acompanhamento com a equipe multidisciplinar, o Leo começou a pronunciar as primeiras palavras e interagir com os coleguinhas na escola. Uma vitória de toda a família!", 
            "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=Leo&backgroundColor=b6e3f4"
        },
        {
            "nome": "Sofia, 7 anos", 
            "diag": "TDAH", 
            "texto": "A rotina estruturada recomendada pela neuropediatra transformou a vida da Sofia. Hoje ela consegue focar nas atividades e está muito mais feliz e confiante nas aulas.", 
            "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=Sofia&backgroundColor=ffdfbf"
        }
    ]
    
    for h in historias:
        st.markdown(f"""
            <div style="background-color: #FFFFFF; border-radius: 20px; padding: 20px; box-shadow: 0 6px 16px rgba(0,0,0,0.04); margin-bottom: 15px;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                    <img src="{h['img']}" style="width: 50px; height: 50px; border-radius: 50%; background-color: #F5F5F5;">
                    <div>
                        <div style="color: #FF8C00; font-weight: 800; font-size: 1.1rem;">{h['nome']}</div>
                        <div style="background: #F0F0F0; color: #666; font-size: 0.75rem; padding: 2px 8px; border-radius: 10px; display: inline-block; font-weight: 600;">{h['diag']}</div>
                    </div>
                </div>
                <p style="color: #555555; font-size: 0.9rem; line-height: 1.5; margin: 0; font-style: italic;">"{h['texto']}"</p>
            </div>
        """, unsafe_allow_html=True)

# Lógica de salvar
if 'submit_button' in locals() and submit_button:
    if nome_resp and nome_crianca:
        with st.spinner("Salvando no sistema..."):
            time.sleep(1)
            nova_linha = [nome_resp, email_resp, telefone, cidade, nome_crianca, diagnostico, "", necessidade, ""]
            aba_familias.append_row(nova_linha)
        st.balloons()
        st.success("✅ Perfil criado com sucesso!")
    else:
        st.error("⚠️ Preencha pelo menos o seu nome e o da criança.")

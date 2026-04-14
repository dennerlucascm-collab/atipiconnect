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

# 2. UI/UX DESIGN: MOBILE APP (BARRA INFERIOR SEGURA E ALTO CONTRASTE)
st.set_page_config(page_title="ATIPICONNECT", page_icon="🧩", layout="centered")

st.markdown("""
    <style>
    /* 1. Fundo Azul Claro Fixo */
    [data-testid="stAppViewContainer"] { background-color: #EAF4FB !important; }
    
    /* Protege o conteúdo de ser engolido pela barra inferior */
    .block-container { padding-bottom: 120px !important; }
    
    /* 2. FORÇA BRUTA NAS CORES (Contra Modo Escuro e Textos Fantasmas) */
    p, span, label, div, [data-testid="stWidgetLabel"] p, .stMarkdown p { 
        color: #1A1A1A !important; 
    }
    h3, h4, h5, h6 { color: #1E3A8A !important; font-weight: 800 !important; }
    h1 { color: #FF8C00 !important; font-weight: 900 !important; text-align: center; font-size: 2.2rem !important; margin-bottom: 0px !important;}
    
    /* 3. Inputs (Caixas de texto super legíveis) */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea { 
        background-color: #FFFFFF !important;
        border: 2px solid #A0AEC0 !important; 
        border-radius: 12px !important; 
    }
    div[data-baseweb="input"] input, div[data-baseweb="select"] div, textarea { 
        color: #1A1A1A !important; font-weight: 700 !important; 
    }
    div[data-baseweb="input"] > div:focus-within, textarea:focus { border-color: #FF8C00 !important; }
    
    /* Card Branco do Formulário */
    [data-testid="stForm"] { 
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        padding: 20px !important;
        border: 2px solid #CBD5E1 !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Botão Principal */
    [data-testid="stFormSubmitButton"] > button { 
        background: linear-gradient(135deg, #FF8C00, #FF6B00) !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 12px 20px !important;
        width: 100% !important;
        box-shadow: 0 4px 12px rgba(255, 140, 0, 0.3) !important;
    }
    [data-testid="stFormSubmitButton"] > button p { 
        color: #FFFFFF !important; 
        font-weight: 800 !important; 
        font-size: 1.1rem !important; 
        text-transform: uppercase !important; 
    }

    /* ========================================================
       MÁGICA SEGURA: BARRA INFERIOR (Mobile Navigation)
       ======================================================== */
    /* Foca estritamente na lista de botões das abas */
    div[role="tablist"] {
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        background-color: #FFFFFF !important;
        z-index: 999999 !important;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.15) !important;
        padding: 10px 0px 25px 0px !important; /* Espaço extra para a base do celular */
        display: flex !important;
        justify-content: space-evenly !important;
        border-radius: 25px 25px 0 0 !important;
        flex-wrap: nowrap !important;
    }
    
    /* Remove as linhas e fundos chatos nativos do Streamlit */
    div[data-baseweb="tab-border"] { display: none !important; }
    div[data-baseweb="tab-highlight"] { display: none !important; }
    
    /* Estilo dos Botões Nativos na Barra Inferior */
    button[role="tab"] {
        flex: 1 !important;
        justify-content: center !important;
        background: transparent !important;
        border: none !important;
        min-width: auto !important;
    }
    
    /* Texto Inativo (Cinza) */
    button[role="tab"] p {
        color: #64748B !important; 
        font-weight: 700 !important; 
        font-size: 0.8rem !important; /* Tamanho mobile */
        margin: 0 !important;
        text-align: center !important;
    }
    
    /* Texto Ativo (Laranja e Destacado) */
    button[role="tab"][aria-selected="true"] p {
        color: #FF8C00 !important; 
        font-weight: 900 !important;
        font-size: 0.85rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho 
st.markdown("<h1>🧩 ATIPICONNECT</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-top: 0;'>Acolhimento & Desenvolvimento</h3>", unsafe_allow_html=True)

# 4. As Abas Nativas (Agora no rodapé pelo CSS, 100% clicáveis)
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Início", "📋 Cadastro", "👨‍⚕️ Médicos", "🧸 Histórias"])

with tab1:
    st.markdown("""
        <div style="background-color: #FFFFFF; border-radius: 20px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 15px; border-left: 5px solid #FF8C00; margin-top: 10px;">
            <img src="https://img.freepik.com/premium-photo/confident-middle-aged-business-woman-attorney-45-years-old-lady-entrepreneur-mature-female-professional-executive-manager-leader-standing-modern-company-office-looking-camera-portrait_1254992-255711.jpg" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 2px solid #1E3A8A; flex-shrink: 0;">
            <div>
                <h4 style="margin: 0 0 5px 0;">Olá, sou a Ana Paula! 👩🏻‍💼</h4>
                <p style="margin: 0; font-size: 0.95rem; line-height: 1.4;">Seja bem-vinda ao nosso app. Selecione "Cadastro" na barra inferior para preencher o perfil.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    with st.form("cadastro_familia", clear_on_submit=True):
        st.markdown("<p style='font-size: 1.15rem; font-weight: 800; color: #1E3A8A !important;'>👤 Dados do Responsável</p>", unsafe_allow_html=True)
        nome_resp = st.text_input("Nome Completo", placeholder="Ex: Maria Silva")
        email_resp = st.text_input("E-mail")
        telefone = st.text_input("WhatsApp")
        cidade = st.text_input("Cidade / Estado", placeholder="Ex: Campo Grande, MS")
        
        st.write("---")
        st.markdown("<p style='font-size: 1.15rem; font-weight: 800; color: #1E3A8A !important;'>🧸 Perfil da Criança</p>", unsafe_allow_html=True)
        nome_crianca = st.text_input("Nome da Criança")
        diagnostico = st.text_area("Breve relato sobre o diagnóstico")
        necessidade = st.selectbox("Especialidade principal procurada", ["Neuropediatria", "Psiquiatria Infantil", "Fonoaudiologia", "Fisioterapia", "Terapia Ocupacional", "Psicologia"])
        
        submit_button = st.form_submit_button("CRIAR PERFIL AGORA")

with tab3:
    st.markdown("#### Corpo Clínico", unsafe_allow_html=True)
    medicos = [
        {"nome": "Dr. Carlos Mendes", "esp": "Neuropediatra", "crm": "CRM 45892", "img": "https://images.pexels.com/photos/5327656/pexels-photo-5327656.jpeg?auto=compress&cs=tinysrgb&w=200"},
        {"nome": "Dra. Juliana Castro", "esp": "Psiquiatra Infantil", "crm": "CRM 67123", "img": "https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg?auto=compress&cs=tinysrgb&w=200"},
        {"nome": "Dra. Renata Alves", "esp": "Fonoaudióloga", "crm": "CRFa 1245", "img": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=200"}
    ]
    for m in medicos:
        st.markdown(f"""
            <div style="background-color: #FFFFFF; border-radius: 15px; padding: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 15px; margin-bottom: 12px; border: 1px solid #A0AEC0;">
                <img src="{m['img']}" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; flex-shrink: 0;">
                <div>
                    <div style="font-weight: 800; font-size: 1.05rem; color: #1A1A1A !important;">{m['nome']}</div>
                    <div style="color: #FF8C00 !important; font-weight: 700; font-size: 0.9rem;">{m['esp']}</div>
                    <div style="color: #64748B !important; font-weight: 600; font-size: 0.8rem;">{m['crm']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("#### Histórias de Superação", unsafe_allow_html=True)
    historias = [
        {
            "nome": "Leo, 5 anos", "diag": "Autismo (TEA)", 
            "texto": "Após 6 meses de acompanhamento com a equipe multidisciplinar, o Leo começou a pronunciar as primeiras palavras e interagir com os coleguinhas na escola. Uma vitória de toda a família!", 
            "img": "https://arttherapyresources.com.au/wp-content/uploads/autism-children-art-therapy-1.jpg"
        },
        {
            "nome": "Sofia, 7 anos", "diag": "TDAH", 
            "texto": "A rotina estruturada recomendada pela neuropediatra transformou a vida da Sofia. Hoje ela consegue focar nas atividades e está muito mais feliz e confiante nas aulas.", 
            "img": "https://media.istockphoto.com/id/2160439676/photo/happy-multiethnic-group-of-children-hugging-together-at-park.jpg?s=612x612&w=0&k=20&c=1lqhI9FvBhrHWTeycmeKB_Z36-OQJRcucLodsnKajR4="
        }
    ]
    for h in historias:
        st.markdown(f"""
            <div style="background-color: #FFFFFF; border-radius: 15px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 15px; border: 1px solid #A0AEC0;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <img src="{h['img']}" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
                    <div>
                        <div style="font-weight: 800; font-size: 1.15rem; color: #1E3A8A !important;">{h['nome']} 🧸</div>
                        <div style="background: #EAF4FB; color: #1E3A8A !important; font-size: 0.8rem; padding: 4px 10px; border-radius: 8px; display: inline-block; font-weight: 700; margin-top: 5px;">{h['diag']}</div>
                    </div>
                </div>
                <p style="font-size: 0.95rem; line-height: 1.5; margin: 0; font-style: italic; color: #1A1A1A !important;">"{h['texto']}"</p>
            </div>
        """, unsafe_allow_html=True)

# Lógica de salvar
if 'submit_button' in locals() and submit_button:
    if nome_resp and nome_crianca:
        with st.spinner("Salvando no sistema..."):
            nova_linha = [nome_resp, email_resp, telefone, cidade, nome_crianca, diagnostico, "", necessidade, ""]
            aba_familias.append_row(nova_linha)
        st.balloons()
        st.success("✅ Tudo pronto! O perfil foi criado com sucesso.")
    else:
        st.error("⚠️ Por favor, preencha pelo menos o seu nome e o da criança.")

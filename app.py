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

# 2. UI/UX DESIGN (ESTRUTURA MANTIDA + CORREÇÕES DE MENU E EXPANSÃO)
st.set_page_config(page_title="ATIPICONNECT", page_icon="🧩", layout="centered")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #EAF4FB !important; }
    .block-container { padding-bottom: 120px !important; }
    
    p, span, label, div, [data-testid="stWidgetLabel"] p, .stMarkdown p { color: #1A1A1A !important; }
    h3, h4, h5, h6 { color: #1E3A8A !important; font-weight: 800 !important; }
    h1 { color: #FF8C00 !important; font-weight: 900 !important; text-align: center; font-size: 2.2rem !important; margin-bottom: 0px !important;}
    
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea { 
        background-color: #FFFFFF !important;
        border: 2px solid #A0AEC0 !important; 
        border-radius: 12px !important; 
    }
    div[data-baseweb="input"] input, div[data-baseweb="select"] div, textarea { 
        color: #1A1A1A !important; font-weight: 700 !important; 
    }
    div[data-baseweb="input"] > div:focus-within, textarea:focus { border-color: #FF8C00 !important; }
    
    /* ========================================================
       CORREÇÃO DO MENU DROP-DOWN (A CAIXINHA DE SELEÇÃO)
       ======================================================== */
    div[data-baseweb="popover"] > div { background-color: #FFFFFF !important; }
    ul[role="listbox"] { background-color: #FFFFFF !important; }
    ul[role="listbox"] li { color: #1A1A1A !important; font-weight: 700 !important; }
    ul[role="listbox"] li:hover { background-color: #EAF4FB !important; color: #FF8C00 !important; }
    
    /* ========================================================
       ESTILOS PARA A CAIXA EXPANSÍVEL (DETAILS/SUMMARY HTML)
       ======================================================== */
    summary { list-style: none; outline: none; cursor: pointer; }
    summary::-webkit-details-marker { display: none; }
    
    [data-testid="stForm"] { 
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        padding: 20px !important;
        border: 2px solid #CBD5E1 !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
    }
    
    [data-testid="stFormSubmitButton"] > button { 
        background: linear-gradient(135deg, #FF8C00, #FF6B00) !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 12px 20px !important;
        width: 100% !important;
        box-shadow: 0 4px 12px rgba(255, 140, 0, 0.3) !important;
    }
    [data-testid="stFormSubmitButton"] > button p { 
        color: #FFFFFF !important; font-weight: 800 !important; font-size: 1.1rem !important; text-transform: uppercase !important; 
    }

    div[role="tablist"] {
        position: fixed !important; bottom: 0 !important; left: 0 !important; right: 0 !important; width: 100% !important;
        background-color: #FFFFFF !important; z-index: 999999 !important; box-shadow: 0 -4px 20px rgba(0,0,0,0.15) !important;
        padding: 10px 0px 25px 0px !important; display: flex !important; justify-content: space-evenly !important;
        border-radius: 25px 25px 0 0 !important; flex-wrap: nowrap !important;
    }
    div[data-baseweb="tab-border"], div[data-baseweb="tab-highlight"] { display: none !important; }
    button[role="tab"] { flex: 1 !important; justify-content: center !important; background: transparent !important; border: none !important; min-width: auto !important; }
    button[role="tab"] p { color: #64748B !important; font-weight: 700 !important; font-size: 0.8rem !important; margin: 0 !important; text-align: center !important; }
    button[role="tab"][aria-selected="true"] p { color: #FF8C00 !important; font-weight: 900 !important; font-size: 0.85rem !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho 
st.markdown("<h1>🧩 ATIPICONNECT</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-top: 0;'>Acolhimento & Desenvolvimento</h3>", unsafe_allow_html=True)

# 4. As Abas Nativas no Rodapé
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
    st.markdown("#### Corpo Clínico (Clique para expandir)", unsafe_allow_html=True)
    medicos = [
        {"nome": "Dr. Carlos Mendes", "esp": "Neuropediatra", "crm": "CRM 45892", "img": "https://images.pexels.com/photos/5327656/pexels-photo-5327656.jpeg?auto=compress&cs=tinysrgb&w=200", "bio": "Especialista no diagnóstico e acompanhamento de TEA e TDAH. Atendimento focado no desenvolvimento neuropsicomotor com abordagem humanizada."},
        {"nome": "Dra. Juliana Castro", "esp": "Psiquiatra Infantil", "crm": "CRM 67123", "img": "https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg?auto=compress&cs=tinysrgb&w=200", "bio": "Ampla experiência em transtornos do neurodesenvolvimento. Trabalha em parceria com a família para encontrar o equilíbrio emocional da criança."},
        {"nome": "Dra. Renata Alves", "esp": "Fonoaudióloga", "crm": "CRFa 1245", "img": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=200", "bio": "Foco em comunicação alternativa e atraso de fala. Sessões lúdicas que transformam o aprendizado da comunicação em uma brincadeira."},
        {"nome": "Dr. Marcos Silva", "esp": "Psicólogo Infantil", "crm": "CRP 89231", "img": "https://images.pexels.com/photos/4173251/pexels-photo-4173251.jpeg?auto=compress&cs=tinysrgb&w=200", "bio": "Especialista em Análise do Comportamento Aplicada (ABA). Ajuda a desenvolver habilidades sociais e de independência no dia a dia."},
        {"nome": "Dra. Camila Rocha", "esp": "Terapeuta Ocupacional", "crm": "CREFITO 1290", "img": "https://images.pexels.com/photos/7477023/pexels-photo-7477023.jpeg?auto=compress&cs=tinysrgb&w=200", "bio": "Atua na integração sensorial, auxiliando crianças com sensibilidades auditivas e táteis a se sentirem mais confortáveis em seus ambientes."}
    ]
    for m in medicos:
        st.markdown(f"""
            <details style="background-color: #FFFFFF; border-radius: 15px; padding: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 12px; border: 1px solid #A0AEC0;">
                <summary style="display: flex; align-items: center; justify-content: space-between;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <img src="{m['img']}" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; flex-shrink: 0;">
                        <div>
                            <div style="font-weight: 800; font-size: 1.05rem; color: #1A1A1A !important;">{m['nome']}</div>
                            <div style="color: #FF8C00 !important; font-weight: 700; font-size: 0.9rem;">{m['esp']}</div>
                            <div style="color: #64748B !important; font-weight: 600; font-size: 0.75rem;">{m['crm']}</div>
                        </div>
                    </div>
                    <div style="color: #FF8C00; font-size: 1.2rem; font-weight: 800;">+</div>
                </summary>
                <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #E2E8F0; color: #333333; font-size: 0.9rem; line-height: 1.5;">
                    <b>Sobre o profissional:</b> {m['bio']}
                    <br><br>
                    <button style="background: #EAF4FB; color: #1E3A8A; border: none; padding: 8px 15px; border-radius: 8px; font-weight: 700; width: 100%;">Solicitar Contato</button>
                </div>
            </details>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("#### Histórias de Superação (Clique)", unsafe_allow_html=True)
    historias = [
        {
            "nome": "Leo, 5 anos", "diag": "Autismo (TEA)", "resumo": "As primeiras palavras do Leo mudaram tudo...",
            "texto": "Após 6 meses de acompanhamento com a equipe multidisciplinar de fonoaudiologia e terapia ocupacional, o Leo começou a pronunciar as primeiras palavras e interagir com os coleguinhas na escola. Hoje ele já consegue pedir seus brinquedos favoritos. Uma vitória de toda a família e da nossa rede de apoio!", 
            "img": "https://arttherapyresources.com.au/wp-content/uploads/autism-children-art-therapy-1.jpg"
        },
        {
            "nome": "Sofia, 7 anos", "diag": "TDAH", "resumo": "Uma nova rotina trouxe calma para a Sofia...",
            "texto": "A rotina estruturada recomendada pela neuropediatra transformou a vida da Sofia e de seus pais. Antes, o momento da lição de casa era de muito choro. Hoje, com estratégias visuais e pausas ativas, ela consegue focar nas atividades e está muito mais feliz e confiante nas aulas.", 
            "img": "https://media.istockphoto.com/id/2160439676/photo/happy-multiethnic-group-of-children-hugging-together-at-park.jpg?s=612x612&w=0&k=20&c=1lqhI9FvBhrHWTeycmeKB_Z36-OQJRcucLodsnKajR4="
        }
    ]
    for h in historias:
        st.markdown(f"""
            <details style="background-color: #FFFFFF; border-radius: 15px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 15px; border: 1px solid #A0AEC0;">
                <summary style="display: flex; align-items: center; justify-content: space-between;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <img src="{h['img']}" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
                        <div>
                            <div style="font-weight: 800; font-size: 1.15rem; color: #1E3A8A !important;">{h['nome']} 🧸</div>
                            <div style="color: #64748B !important; font-size: 0.85rem; font-weight: 600; margin-top: 3px;">{h['resumo']}</div>
                        </div>
                    </div>
                    <div style="color: #1E3A8A; font-size: 1.2rem; font-weight: 800;">+</div>
                </summary>
                <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #E2E8F0;">
                    <div style="background: #EAF4FB; color: #1E3A8A !important; font-size: 0.8rem; padding: 4px 10px; border-radius: 8px; display: inline-block; font-weight: 700; margin-bottom: 10px;">Diagnóstico: {h['diag']}</div>
                    <p style="font-size: 0.95rem; line-height: 1.5; margin: 0; font-style: italic; color: #1A1A1A !important;">"{h['texto']}"</p>
                </div>
            </details>
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

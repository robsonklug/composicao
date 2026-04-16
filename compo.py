import streamlit as st

# Configuração da página inspirada no modelo visual do TOTVS
st.set_page_config(page_title="TOTVS | Planej.Contr.Produção", layout="wide")

# Estilização CSS para o cabeçalho e elementos visuais
st.markdown("""
    <style>
    .main-header { background-color: #005483; color: white; padding: 10px; font-size: 20px; font-family: sans-serif; }
    .stButton>button { background-color: #005483; color: white; width: 100%; }
    .etiqueta-container { border: 1px solid #ccc; padding: 20px; background-color: white; color: black; font-family: 'Courier New', Courier, monospace; width: fit-content; min-width: 300px; }
    </style>
    <div class="main-header">TOTVS | Planej.Contr.Produção</div>
    """, unsafe_allow_html=True)

# Layout: Menu Lateral
with st.sidebar:
    st.button("🎥 Modo apresentação")
    st.text_input("🔍 Pesquisar")
    st.markdown("---")
    st.write("📁 Cadastros")
    st.write("⚙️ Configurações")
    st.write("🚚 Logística")
    st.write("📊 Relatórios")
    st.markdown("---")
    st.button("Fechar menu")

# Área Principal: Formulário de Cadastro
st.subheader("Cadastro Complementar de Produto Têxtil")

# 5 - Código do produto
codigo_produto = st.text_input("Código do Produto:", placeholder="Exemplo: 86316")

col1, col2 = st.columns(2)

with col1:
    # 1 - Largura
    st.write("### 📏 Largura")
    l_val = st.number_input("Valor da Largura:", min_value=0.0, format="%.2f")
    l_uni = st.text_input("Unidade (ex: m):", value="m")
    l_tol = st.text_input("Tolerância (ex: ± 2 cm):")

    # 2 - Estrutura
    st.write("### 🧵 Estrutura")
    estrutura = st.text_input("Descrição da Estrutura:", placeholder="Exemplo: sarja 3×1")

with col2:
    # 3 - Peso
    st.write("### ⚖️ Peso")
    p_val = st.number_input("Valor do Peso:", min_value=0.0)
    p_uni = st.text_input("Unidade (ex: g/m²):", value="g/m²")
    p_mar = st.text_input("Margem (ex: ± 5%):")

# 4 - Composição
st.write("### 🧪 Composição")
opcoes_fibras = [
    "Algodão", "Linho", "Seda", "Lã", "Poliéster", 
    "Poliamida", "Elastano", "Viscose", "Liocel"
]

selecionadas = st.multiselect("Selecione as fibras componentes:", opcoes_fibras)
composicao_lista = []

if selecionadas:
    cols = st.columns(len(selecionadas))
    for i, fibra in enumerate(selecionadas):
        perc = cols[i].number_input(f"% {fibra}", min_value=0, max_value=100, key=f"perc_{fibra}")
        if perc > 0:
            composicao_lista.append(f"{perc}% {fibra.upper()}")

st.markdown("---")

# Botão para processar e exibir etiqueta
if st.button("GERAR ETIQUETA E SALVAR"):
    if not codigo_produto or not composicao_lista:
        st.warning("Por favor, preencha o código do produto e a composição.")
    else:
        st.success("Cadastro simulado com sucesso!")
        
        # Simulação visual da etiqueta baseada na imagem de referência
        st.write("### Prévia da Etiqueta")
        
        etiqueta_html = f"""
        <div class="etiqueta-container">
            <div style="font-size: 24px; letter-spacing: 5px; margin-bottom: 10px;">🧺 ⚠️ 🧼 🚫 ⊗</div>
            <div style="font-size: 14px; line-height: 1.4;">
                {'<br>'.join(composicao_lista)}
            </div>
            <div style="margin-top: 15px; border-top: 1px solid black; padding-top: 5px; font-weight: bold;">
                INDÚSTRIA BRASILEIRA
            </div>
            <div style="font-size: 12px; margin-top: 5px; color: #555;">
                Ref: {codigo_produto}<br>
                {l_val}{l_uni} ({l_tol}) | {estrutura}
            </div>
        </div>
        """
        st.markdown(etiqueta_html, unsafe_allow_html=True)

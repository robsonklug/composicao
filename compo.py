import streamlit as st

# Configuração da página inspirada no modelo visual 
st.set_page_config(page_title="TOTVS | Planej.Contr.Produção", layout="wide")

# Estilização para simular o cabeçalho azul e barra lateral 
st.markdown("""
    <style>
    .main-header { background-color: #005483; color: white; padding: 10px; font-size: 20px; }
    .stButton>button { background-color: #005483; color: white; }
    </style>
    <div class="main-header">TOTVS | Planej.Contr.Produção</div>
    """, unsafe_allow_html=True)

# Menu Lateral 
with st.sidebar:
    st.button("🎥 Modo apresentação")
    st.text_input("🔍 Pesquisar")
    st.markdown("---")
    st.write("📁 Cadastros")
    st.write("⚙️ Configurações")
    st.write("🚚 Logística")
    st.markdown("---")
    st.button("Fechar menu")

# Título do Formulário 
st.subheader("Cadastro Complementar de Produto Têxtil")

# 5 - Código do produto [cite: 17]
codigo_produto = st.text_input("Código do Produto:", placeholder="Exemplo: 86316")

col1, col2 = st.columns(2)

with col1:
    # 1 - Largura [cite: 3]
    st.write("### Detalhes de Largura")
    largura_valor = st.number_input("Largura (valor):", min_value=0.0, step=0.01)
    largura_unidade = st.selectbox("Unidade:", ["m", "cm", "mm"])
    largura_tolerancia = st.text_input("Tolerância (Ex: ± 2 cm):")

    # 2 - Estrutura 
    st.write("### Estrutura")
    estrutura = st.text_input("Descrição da Estrutura:", placeholder="Exemplo: sarja 3×1")

with col2:
    # 3 - Peso [cite: 5]
    st.write("### Detalhes de Peso")
    peso_valor = st.number_input("Peso (valor):", min_value=0.0)
    peso_unidade = st.selectbox("Unidade de Medida:", ["g/m²", "oz/yd²"])
    peso_margem = st.text_input("Margem (Ex: ± 5%):")

# 4 - Composição [cite: 6, 7]
st.write("### Composição")
opcoes_fibras = [
    "Algodão", "Linho", "Seda", "Lã", "Poliéster", 
    "Poliamida", "Elastano", "Viscose", "Liocel"
] [cite: 8, 9, 10, 11, 12, 13, 14, 15, 16]

selecionadas = st.multiselect("Selecione as fibras:", opcoes_fibras)
composicao_final = []

if selecionadas:
    cols = st.columns(len(selecionadas))
    for i, fibra in enumerate(selecionadas):
        percentual = cols[i].number_input(f"% de {fibra}", min_value=0, max_value=100, key=fibra)
        if percentual > 0:
            composicao_final.append(f"{percentual}% {fibra.upper()}")

# Geração do Simulado de Etiqueta (Imagem/Visualização) 
st.markdown("---")
if st.button("Gerar Visualização da Etiqueta"):
    if not codigo_produto or not composicao_final:
        st.error("Por favor, preencha o Código e a Composição.")
    else:
        st.write("#### Prévia da Etiqueta (Simulação de Impressão)")
        # Simulação visual da etiqueta baseada na imagem fornecida 
        with st.container():
            st.markdown(f"""
            <div style="border: 1px solid black; padding: 20px; width: 300px; text-align: center; background-color: white; color: black; font-family: Arial;">
                <div style="font-size: 25px; margin-bottom: 10px;">♨️ ⚠️ 🧺 🚫 ⊗</div>
                <div style="text-align: left; font-weight: bold;">
                    {'<br>'.join(composicao_final)}
                </div>
                <div style="margin-top: 10px; font-weight: bold; border-top: 1px solid black;">
                    INDÚSTRIA BRASILEIRA
                </div>
                <div style="font-size: 10px; margin-top: 5px;">Ref: {codigo_produto}</div>
            </div>
            """, unsafe_allow_html=True)
            
        # Resumo dos dados técnicos para o sistema
        st.info(f"**Resumo Técnico:** {largura_valor}{largura_unidade} ({largura_tolerancia}) | "
                f"Estrutura: {estrutura} | "
                f"Peso: {peso_valor}{peso_unidade} ({peso_margem})")

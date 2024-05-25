import streamlit as st
import time
from PIL import Image

st.set_page_config(page_title="NFE Vision - Leitor de Notas Fiscais Eletrônicas", page_icon=":material/monitoring:", layout="wide", initial_sidebar_state="expanded")
st.title("📷 Capturar NFe")
st.sidebar.header("Captura de imagem")

col1, col2 = st.columns([4, 6])
with col1:
    container = st.container(border=True)           
    with container:            
            # Configuração da câmera
            imagem = st.camera_input("Tire uma foto da Nota Fiscal")

            # Processamento da imagem capturada
            if imagem:
                # Converte a imagem do formato Web para PIL Imagem
                imagem = Image.open(imagem)

                # Exibe a imagem capturada
                st.image(imagem, caption="Imagem Capturada", use_column_width=True)

                # Botão para salvar a imagem
                if st.button("Salvar Imagem"):                    
                    now = int(time.time())
                    file_name = f"nfe_{now}.png"
                    imagem.save(file_name)
                    st.success(f"Imagem salva com sucesso como {file_name}")
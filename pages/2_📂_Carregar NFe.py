# Importa Bibliotecas
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Layout da página
st.set_page_config(page_title="NFE Vision - Leitor de Notas Fiscais Eletrônicas", page_icon=":material/monitoring:", layout="wide", initial_sidebar_state="expanded")
st.title("📂 Carregar NFe")
st.sidebar.header("Carregar NFe Digitalizada")

load_dotenv()   # carrega variáveis de ambiente

# Inicia modelos Google Generative AI
my_api_key = os.environ.get("API_KEY")   # Gemini - API_KEY
genai.configure(api_key=my_api_key)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest",
        generation_config=generation_config,
        safety_settings=safety_settings)

# Análise multimodal (instrução e imagem) feita pelo Google Gemini 
def get_info(image):
    prompt = "Esta imagem deve corresponder a uma nota fiscal eletrônica. Levante os dados presentes na mesma e os retorne em formato JSON. Caso a imagem não contenha uma NFe válida, avise sobre o fato descrevendo os elementos que foram encontrados na imagem."
    media = genai.upload_file(path=image, mime_type="image/jpeg")
    ai_analysis = model.generate_content([prompt, media])
    response = ai_analysis.text
    return response    

# Obtem Imagem e envia para análise
container = st.container(border=True)           
with container:            
    uploaded_file = st.file_uploader("Selecione uma Nota Fiscal em formato JPEG", type=["jpg", "jpeg"])
    if uploaded_file is not None:            
        with st.spinner("Aguarde..."):  
            try:
                # Realiza o upload do arquivo para o servidor
                file_path = os.path.join("./", uploaded_file.name)    
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                nfe_data = get_info(file_path)        # realiza a análise da imagem
                os.remove(file_path)                  # Apaga arquivo após conclusão da análise
                st.success("Análise concluída.")
                st.write(nfe_data)

            except Exception as e:
                st.error(f"Não foi possível analisar os dados. Detalhes: {e}")
            
import streamlit as st

st.set_page_config(page_title="NF-e Vision / Leitor de Notas Fiscais Eletrônicas", page_icon=":material/monitoring:")
st.header("NF-e Vision: Leitor de NF-e com IA 🧠")
#st.image(image="./static/logo.jpeg",use_column_width="auto")

text = """
👋 Bem-vindo ao NF-e Vision, um aplicativo inovador que simplifica a leitura e extração de dados de Notas Fiscais Eletrônicas (NF-e) utilizando o poder da Inteligência Artificial!

✨ Funcionalidades que Simplificam sua Vida:

* Escaneamento por meio de foto: Tire uma foto de sua NFe e o app se encarrega de fazer o levantamento dos dados presentes na mesma. 📷
* Upload de Imagens de NF-e: Carregue imagens de NF-e no formato JPEG com facilidade. 🖼️
* Extração de Dados Automática: Nosso modelo de OCR (Optical Character Recognition) baseado em IA extrai informações essenciais da NF-e, como:
    * Chave de Acesso 🔑
    * Número da Nota Fiscal 🔢
    * Data de Emissão 📅
    * Valor Total 💰
    * Nome do Emitente 🏢
    * CNPJ do Emitente 📑
    * E muito mais! 🚀

Visualização Clara e Organizada: Os dados extraídos são apresentados de forma estruturada e fácil de entender em uma interface amigável. 📊

🛠️ Tecnologias que Impulsionam a Solução:

* Python: O coração do projeto, responsável por toda a lógica do aplicativo, manipulação de dados e integração com bibliotecas de IA. 🐍
* Streamlit: Framework web intuitivo que dá vida à interface gráfica interativa do aplicativo. ✨
* Google Generative AI: Biblioteca de Inteligência Artificial da Google (LLM) responsável pela "mágica" da extração dos dados.

🚀 Próximos Passos para um Futuro Brilhante:

* Validação de Dados: Adicionar mecanismos inteligentes para validar os dados extraídos, garantindo sua integridade e confiabilidade. ✅
* Armazenamento de dados: Salvar os dados obtidos em um banco de dados
* Relatórios: Permitir a geração de relatórios detalhados e dashboards interativos com os dados extraídos das NF-es. 📊

💪 Junte-se a Nós nesta Jornada!

Sua contribuição é muito bem-vinda! Você pode nos ajudar de diversas maneiras:
* Reportando bugs e problemas encontrados. 🐞
* Compartilhando suas ideias e sugestões de novas funcionalidades.💡
* Implementando melhorias no código existente. 💻
* Criando testes unitários para garantir a qualidade do código. ✅
* Vamos juntos tornar o NF-e Vision ainda mais incrível! ✨
"""

st.write(text)
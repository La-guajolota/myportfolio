import streamlit as st
from PIL import Image
from pathlib import Path
from utils import social_icons

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", 
                   page_icon=":rocket:", 
                   layout="wide")

# Definir texto 
about_header = "Sobre mí"
subheader = "Ingeniero en sistemas embebidos en proceso"
intro_text = "- 👋🏻 ¡Hola, soy Adrián! Estoy a punto de graduarme, con un fuerte sentido de motivación y dedicación para hacer contribuciones significativas en mi campo."
resume_label = " 📄 Descargar CV"

# Ruta a los archivos
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "CV.pdf"
css_file = current_dir / "styles" / "homepage.css"

# Cargar y aplicar CSS personalizado
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Leer el PDF del CV
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Cargar imagen
img = Image.open("assets/yo.jpeg")

# Diseño y contenido
with st.container():
    left_column, middle_column, right_column = st.columns((1, 0.2, 0.6))
    
    with left_column:
        st.header(about_header, divider='red')
        st.subheader(subheader)
        st.write(intro_text)
        st.download_button(
            label=resume_label,
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream")
        st.markdown(social_icons(32, 32, LinkedIn="https://www.linkedin.com/in/adri%C3%A1n-silva-palafox-a17a6a274/", 
                                         GitHub="https://github.com/La-guajolota"), 
                                         unsafe_allow_html=True)
    
    with middle_column:
        st.empty()
    
    with right_column:
        st.image(img)

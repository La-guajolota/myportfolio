import streamlit as st
from PIL import Image
from pathlib import Path
from utils import social_icons

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", 
                   page_icon=":rocket:", 
                   layout="wide")

# --- Texto principal ---
about_header = "🙋🏻 Sobre mí"
subheader = "Ingeniero en sistemas embebidos en proceso"
intro_text = """
👋🏻 ¡Hola, soy **Adrián**!  
Estoy a punto de graduarme, con un fuerte sentido de motivación y dedicación para hacer contribuciones significativas en mi campo.  

💡 Me especializo en el desarrollo de firmware para microcontroladores, sistemas embebidos Linux y aplicaciones de IoT.  
Me interesa aplicar tecnologías como **FreeRTOS, ROS/microROS y TinyML** en proyectos de automatización, agricultura de precisión y robótica.  
"""
resume_label = "📄 Descargar CV"

# --- Paths ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "AdrianSilvaPalafox_CV.pdf"
css_file = current_dir / "styles" / "homepage.css"

# --- CSS personalizado ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

extra_css = """
<style>
.about-card {
  background: #ffffff;
  padding: 18px 18px 14px;
  border-radius: 14px;
  box-shadow: 0 6px 20px rgba(0,0,0,.18);
  margin-bottom: 18px;
  border: 1px solid rgba(0,0,0,.05);
}
/* Asegura CONTRASTE dentro de la tarjeta, por encima de estilos globales */
.about-card, .about-card * {
  color: #1f2937 !important;         /* gris muy oscuro */
  line-height: 1.45;
}

.profile-pic {
  border-radius: 50%;
  box-shadow: 0 4px 14px rgba(0,0,0,.25);
  max-width: 280px;
  margin: auto;
}
.cv-btn > button {
  background-color: #e63946 !important;
  color: white !important;
  border-radius: 8px !important;
  font-weight: 600 !important;
}
.timeline {
  margin-top: 40px;
  padding-left: 20px;
  border-left: 3px solid #e63946;
}
.timeline-item {
  margin-bottom: 25px;
}
.timeline-date {
  font-weight: bold;
  color: #e63946;
}
.timeline-title {
  font-size: 18px;
  font-weight: 600;
}
.timeline-sub {
  font-size: 14px;
  font-style: italic;
  color: #555;
}
</style>
"""
st.markdown(extra_css, unsafe_allow_html=True)

# --- Cargar archivos ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

img = Image.open("assets/yo.jpeg")

# --- Layout principal ---
with st.container():
    left_column, middle_column, right_column = st.columns((1.2, 0.1, 0.7))
    
    with left_column:
        st.markdown(f"<div class='about-card'><h2>{about_header}</h2></div>", unsafe_allow_html=True)
        st.subheader(subheader)
        st.write(intro_text)
        
        # Botón CV
        st.markdown("<div class='cv-btn'>", unsafe_allow_html=True)
        st.download_button(
            label=resume_label,
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream")
        st.markdown("</div>", unsafe_allow_html=True)

        # Social icons
        st.markdown(
            social_icons(40, 40, 
                         LinkedIn="https://www.linkedin.com/in/adri%C3%A1n-silva-palafox-a17a6a274/", 
                         GitHub="https://github.com/La-guajolota"), 
            unsafe_allow_html=True
        )
    
    with middle_column:
        st.empty()
    
    with right_column:
        st.image(img, width='stretch', output_format="PNG", caption="Adrián Silva Palafox")

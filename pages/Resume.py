from pathlib import Path
from PIL import Image
import streamlit as st
from utils import social_icons

st.set_page_config(layout="centered")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir.parent / "assets" / "AdrianSilvaPalafox_CV.pdf"
profile_pic = current_dir.parent / "assets" / "yo.jpeg"
css_file = current_dir.parent / "styles" / "resume.css"

# --- LOAD PDF, PROFILE PIC & CSS ---

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# --- HERO SECTION ---
with st.container():
    left_column, middle_column, right_column = st.columns((1,0.2,1))
    
    with left_column:
        st.image(profile_pic)

    with middle_column:
        st.empty()

    with right_column:
        st.title("Adrián Silva Palafox")
        st.write("Ingeniero de sistemas embebidos")
        st.download_button(
            label=" 📄 Descarga CV",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", "adriansilpa@gmail.com")
        st.write("📱", "+52 477 264 1384")
        st.markdown(social_icons(32, 32, LinkedIn="https://www.linkedin.com/in/adri%C3%A1n-silva-palafox-a17a6a274/",
                                         GitHub="https://github.com/La-guajolota"),
                                         unsafe_allow_html=True)

# --- LEVEL LEGEND ---
st.write('')
st.subheader("📊 Leyenda de niveles")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""**🟢 Avanzado**
    - Dominio completo de la materia, capaz de diseñar y depurar sistemas de forma autónoma.""")
with col2:
    st.markdown("""**🟡 Intermedio**
    - Con experiencia práctica, resuelve tareas comunes y aprende rápidamente temas nuevos.""")
with col3:
    st.markdown("""**🔵 Básico**
    - Conocimientos fundamentales, en proceso de aprendizaje y práctica.""")

# --- Skills ---
st.write('\n')
st.subheader("💻 Habilidades", divider="red")

st.markdown(
    """
### ⚙️ Sistemas embebidos  
- 🟢 **C/C++**   
- 🟡 **VHDL, Verilog**   
- 🔵 **Ensamblador**   
- 🟡 **FreeRTOS**   
- 🟢 **UART, SPI, I2C**   
- 🟡 **CAN**   

### 🖥️ Lenguajes de apoyo  
- 🟢 **Python**   
- 🟡 **MATLAB/Octave**   
- 🔵 **PHP, HTML, CSS**   

### 🧩 Frameworks  
- 🟡 **ROS / microROS**  
- 🟡 **Edge Impulse**  
- 🟡 **OpenCV**  
- 🔵 **TensorFlow Lite**  

### 🌐 Protocolos y comunicación  
- 🟡 **MQTT, LoRa, Modbus**  

### 🐧 Sistemas GNU/Linux  
- 🟡 **Ubuntu Server**, **Debian Server**  
- 🔵 **Yocto / Buildroot**  

### 📐 CADs y Modelado  
- 🟢 **KiCad**  
- 🔵 **Altium Designer, FreeCAD**  

### 🔬 Instrumentación y Automatización  
- 🟡 **Node-RED**, **LabVIEW**  
- 🔵 **PLC Siemens**, **Electroneumática**  

### 🌍 Idiomas  
- 🇬🇧 Inglés (80%)  
"""
)


# --- EDUCATION ---
st.write('\n')
st.subheader("🎓 Educación", divider="red")

st.markdown(
    """
**Licenciatura en Ingeniería en Electrónica y Telecomunicaciones**  
📍 [Universidad La Salle Bajío](https://www.lasallebajio.edu.mx/)  
📅 2021 – Actualidad  

**Cursos y capacitaciones adicionales:**  
- 🛠️ Taller de Máquinas Herramienta – IECA León GTO (Febrero – Marzo 2022)  
- 🤖 Redes Neuronales – IECA en línea (Septiembre – Diciembre 2021)  
"""
)


# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("💼 Experiencia", divider="red")

st.markdown(
    """
**Ingeniero de aplicación Jr @ [INBIODROID](https://inbiodroid.com/)**  
📅 Enero – Septiembre 2025  

- 🔧 Desarrollo de firmware robusto para control de horno de reflujo.  
- 📈 Implementación de controlador PID + filtro de Kalman.  
- 🌐 Interfaz web embebida para monitoreo y control.  
- 📐 Colaboración en diseño de PCB.  
---
**Equipos representativos @ ULSB**  
📅 Enero 2024 – Actualidad  

- 🤖 Robótica competitiva: seguidores de línea y sumos RF.  
- 🚀 Proyecto Mars Rover: asesor técnico en electrónica, ROS/microROS y GNU Radio.  
---
**Becario de investigación @ [CIO](https://www.cio.mx/)**  
📅 Agosto – Diciembre 2023  

- 🧪 Proyecto “Diseño y fabricación de microbobinas”.  
- 🧼 Procesos de microfabricación en cuarto limpio.  
- 📊 Simulación electromagnética (COMSOL Multiphysics).  
---
**Participante Reto Bushido @ SMC**  
📅 Septiembre 2023  

- ⚙️ Automatización industrial con PLCs y electroneumática.  
---
**Instructor de inglés y matemáticas @ [KUMON](https://www.kumon.com/mx-es/)**  
📅 Enero 2021 – Septiembre 2022  

- 📚 Asesoría académica en inglés y matemáticas (primaria a preparatoria).  
- 💻 Actividades de ofimática y gestión de contenidos educativos.  
"""
)

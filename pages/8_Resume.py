from pathlib import Path
from PIL import Image
import streamlit as st
from utils import social_icons

st.set_page_config(layout="centered")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir.parent / "assets" / "CV.pdf"
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


# --- Skills ---
st.write('\n')
st.subheader("Habilidades", divider="red")
st.write(
    """
- **Lenguajes y programación**
    - HDLs: VHDL, Verilog
    - Microcontroladores: C/C++, ensamblador (básico en RISC-V)
    - Análisis de datos: MATLAB, SQL, Python, C#
    - Tiny Machine Learning: TensorFlow Lite, Edge Impulse
    - Desarrollo web: Streamlit, Node-RED; nociones de PHP, HTML, CSS y JavaScript
- **Diseño y simulación electrónica**
    - ECADs: Altium Designer, KiCad
    - Simuladores: LTspice, Proteus, Multisim
    - Instrumentación: LabVIEW
    - Interfaces embebidas: GFX, LVGL
- **Protocolos y automatización industrial**
    - IoT y comunicación: Nociones de protocolos IoT como MQTT y CoAP
    - Automatización industrial: PLC Siemens, electroneumática
- **Modelado y diseño 3D**
    - Herramientas: OpenSCAD, FreeCAD, SolidWorks (básico)
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Educación", divider="red")

st.write(
    """
### Licenciatura en Ingeniería en Electrónica y Telecomunicaciones [UDLSB](https://www.lasallebajio.edu.mx/) (2021-2025)
- **Cursos relevantes:** Diseño electronico y PCB, Firmware embebido, DSP, Progrmación PLC, Redes, RFID, Telecomunicaciones por RF
"""
)


# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("Experiencia", divider="red")


# --- Experience 2
st.write(
    """
**∎ Becario de investigación @ [CIO](https://www.cio.mx/)**

*Ago - Dic 2023*

- ► Diseño y la fabricación de microbobinas con técnicas de microelectrónica.
- ► Capacitación en labores de cuartos límpios.

""")


# --- Experience 1
st.write(
    """
**∎ Instructor de inglés y matemáticas @ [KUMON](https://www.kumon.com/mx-es/)**

*mar 2020 - Sep 2022*

- ► Llevé acabo actividades de ofimática.
- ► Maestro de repaso para la asignatura de Inglés con grados escolares de primaria, secundaria y preparatoria
- ► Maestro de repaso para la asignatura de Matemáticas con grados escolares de primaria, secundaria y preparatoria
""")

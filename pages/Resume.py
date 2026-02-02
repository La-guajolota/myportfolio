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
        st.write("Embedded Systems Engineer")
        st.download_button(
            label=" 📄 Download CV",
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
st.subheader("📊 Skill Level Legend")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""**🟢 Advanced**
    - Full mastery of the subject, capable of designing and debugging systems autonomously.""")
with col2:
    st.markdown("""**🟡 Intermediate**
    - Practical experience, solves common tasks and quickly learns new topics.""")
with col3:
    st.markdown("""**🔵 Basic**
    - Fundamental knowledge, in the process of learning and practicing.""")

# --- Skills ---
st.write('\n')
st.subheader("💻 Technical Skills", divider="red")

st.markdown(
    """
### ⚙️ Embedded Systems  
- 🟢 **C/C++**   
- 🟡 **VHDL, Verilog**   
- 🔵 **Assembly**   
- 🟡 **FreeRTOS**   
- 🟢 **UART, SPI, I2C**   
- 🟡 **CAN**   

### 🖥️ Supporting Languages  
- 🟢 **Python**   
- 🟡 **MATLAB/Octave**   
- 🔵 **PHP, HTML, CSS**   

### 🧩 Frameworks & Tools  
- 🟡 **ROS / microROS**  
- 🟡 **Edge Impulse**  
- 🟡 **OpenCV**  
- 🔵 **TensorFlow Lite**  

### 🌐 Protocols & Communication  
- 🟡 **MQTT, LoRa, Modbus**  

### 🐧 GNU/Linux Systems  
- 🟡 **Ubuntu Server**, **Debian Server**  
- 🔵 **Yocto / Buildroot**  

### 📐 CAD & Modeling  
- 🟢 **KiCad**  
- 🔵 **Altium Designer, FreeCAD**  

### 🔬 Instrumentation & Automation  
- 🟡 **Node-RED**, **LabVIEW**  
- 🔵 **Siemens PLC**, **Electropneumatics**  

### 🌍 Languages  
- 🇬🇧 English (80%)  
- 🇪🇸 Spanish (Native)  
"""
)


# --- EDUCATION ---
st.write('\n')
st.subheader("🎓 Education", divider="red")

st.markdown(
    """
**Bachelor's Degree in Electronics and Telecommunications Engineering**  
📍 [Universidad La Salle Bajío](https://www.lasallebajio.edu.mx/)  
📅 2021 – Present  
"""
)

# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("📜 Certifications & Training", divider="red")

st.markdown(
    """
- 🛠️ **Machine Tools Workshop** – IECA León GTO (Feb – Mar 2022)  
- 🤖 **Neural Networks Course** – IECA Online (Sep – Dec 2021)  
"""
)


# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("💼 Experience", divider="red")

st.markdown(
    """
**Jr. Application Engineer @ [INBIODROID](https://inbiodroid.com/)**  
📅 January – September 2025  

- 🔧 Developed robust firmware for reflow oven control.  
- 📈 Implemented PID controller + Kalman filter.  
- 🌐 Built embedded web interface for monitoring and control.  
- 📐 Collaborated on PCB design.  
---
**Representative Teams @ ULSB**  
📅 January 2024 – Present  

- 🤖 Competitive robotics: line followers and RF sumo robots.  
- 🚀 Mars Rover Project: technical advisor in electronics, ROS/microROS, and GNU Radio.  
---
**Research Intern @ [CIO](https://www.cio.mx/)**  
📅 August – December 2023  

- 🧪 Project: "Design and fabrication of microcoils".  
- 🧼 Microfabrication processes in cleanroom environment.  
- 📊 Electromagnetic simulation (COMSOL Multiphysics).  
---
**Bushido Challenge Participant @ SMC**  
📅 September 2023  

- ⚙️ Industrial automation with PLCs and electropneumatics.  
---
**English & Math Instructor @ [KUMON](https://www.kumon.com/mx-es/)**  
📅 January 2021 – September 2022  

- 📚 Academic tutoring in English and Mathematics (elementary to high school).  
- 💻 Office administration and educational content management.  
"""
)

import streamlit as st
from PIL import Image
from pathlib import Path
from utils import social_icons

# Page configuration
st.set_page_config(page_title="Adrián Silva Palafox | Embedded Systems Engineer", 
                   page_icon="🔧", 
                   layout="wide")

# --- Main Text ---
about_header = "👨‍💻 About Me"
subheader = "Embedded Systems Engineer | Firmware Developer | IoT Specialist"
intro_text = """
👋 Hi, I'm **Adrián Silva Palafox**!  

I design and build **reliable embedded systems** that bridge hardware and software. With hands-on experience in firmware development, real-time systems, and IoT applications, I transform complex requirements into efficient, production-ready solutions.

---

### 🎯 What I Bring to Your Team

| **Firmware Development** | **Real-Time Systems** | **IoT & Connectivity** |
|:------------------------:|:---------------------:|:----------------------:|
| C/C++, Python, VHDL | FreeRTOS | MQTT, LoRa, Modbus |
| ARM Cortex-M (STM32, ESP32) | PID Control, Kalman Filters | Embedded Linux |
| UART, SPI, I2C, CAN | ROS/microROS | Edge Impulse, TinyML |

---

### 🏆 Key Achievements

- 🔥 **Developed production firmware** for reflow oven with PID + Kalman filter control achieving precise temperature profiles
- 🤖 **Integrated microROS with ROS2** for SCARA robot enabling real-time distributed communication with Modbus TCP
- 📐 **Designed custom PCBs** including FPGA trainer boards (Tang Nano 9K/20K) and power control systems
- 🌱 **Building IoT precision agriculture system** with custom sensor networks and MQTT dashboards
- 🔬 **Research intern at CIO** - Microcoil design and fabrication for biomedical sensors

---

📍 **León, Guanajuato, Mexico** | Open to relocation | Available for remote work
"""
resume_label = "📄 Download CV"

# --- Paths ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "AdrianSilvaPalafox_CV.pdf"
css_file = current_dir / "styles" / "homepage.css"

# --- Custom CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

extra_css = """
<style>
.about-card {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  padding: 20px 24px 16px;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0,0,0,.3);
  margin-bottom: 20px;
  border: 1px solid rgba(230,57,70,0.3);
}
.about-card h2 {
  color: #e63946 !important;
  margin: 0;
}
.profile-pic {
  border-radius: 50%;
  box-shadow: 0 4px 14px rgba(0,0,0,.25);
  max-width: 280px;
  margin: auto;
}
.cv-btn > button {
  background: linear-gradient(135deg, #e63946 0%, #d62839 100%) !important;
  color: white !important;
  border-radius: 10px !important;
  font-weight: 700 !important;
  padding: 12px 24px !important;
  font-size: 1.1rem !important;
  transition: transform 0.2s ease !important;
}
.cv-btn > button:hover {
  transform: translateY(-2px) !important;
}
</style>
"""
st.markdown(extra_css, unsafe_allow_html=True)

# --- Load files ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

img = Image.open("assets/yo.jpeg")

# --- Main Layout ---
with st.container():
    left_column, middle_column, right_column = st.columns((1.3, 0.1, 0.6))
    
    with left_column:
        st.markdown(f"<div class='about-card'><h2>{about_header}</h2></div>", unsafe_allow_html=True)
        st.subheader(subheader)
        st.markdown(intro_text)
        
        # CV Button
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
                         LinkedIn="https://www.linkedin.com/in/adrian-silva-palafox/", 
                         GitHub="https://github.com/La-guajolota"), 
            unsafe_allow_html=True
        )
    
    with middle_column:
        st.empty()
    
    with right_column:
        st.image(img, width='stretch', output_format="PNG", caption="Adrián Silva Palafox")

# --- Call to Action ---
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📧 Get In Touch")
    st.markdown("**adriansilpa@gmail.com**")
    st.markdown("**+52 477 264 1384**")

with col2:
    st.markdown("### 🔗 Explore My Work")
    st.markdown("Check out my **Projects** page to see detailed case studies with code repositories and demo videos.")

with col3:
    st.markdown("### 📄 Quick Facts")
    st.markdown("""
    - 🎓 B.S. Electronics & Telecom (2025)
    - 💼 Jr. Application Engineer @ INBIODROID
    - 🌐 English (B2) / Spanish (Native)
    """)

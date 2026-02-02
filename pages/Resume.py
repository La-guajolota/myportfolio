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
        st.write("**Embedded Systems Engineer**")
        st.caption("Firmware Development • IoT • Real-Time Systems")
        st.download_button(
            label=" 📄 Download CV",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", "adriansilpa@gmail.com")
        st.write("📱", "+52 477 264 1384")
        st.markdown(social_icons(32, 32, LinkedIn="https://www.linkedin.com/in/adrian-silva-palafox/",
                                         GitHub="https://github.com/La-guajolota"),
                                         unsafe_allow_html=True)

# --- PROFESSIONAL SUMMARY ---
st.write('\n')
st.subheader("📋 Professional Summary", divider="red")
st.markdown("""
Results-driven **Embedded Systems Engineer** with hands-on experience developing production-ready firmware for industrial applications. 
Proficient in **C/C++, Python, and real-time operating systems** with a strong foundation in control systems, PCB design, and IoT connectivity. 
Passionate about creating efficient, reliable embedded solutions that solve real-world problems in automation, robotics, and precision agriculture.
""")

# --- LEVEL LEGEND ---
st.write('')
st.subheader("📊 Skill Level Legend")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""**🟢 Advanced**
    - Full mastery, capable of designing and debugging systems autonomously.""")
with col2:
    st.markdown("""**🟡 Intermediate**
    - Practical experience, solves common tasks and quickly learns new topics.""")
with col3:
    st.markdown("""**🔵 Basic**
    - Fundamental knowledge, in the process of learning and practicing.""")

# --- Skills with Visual Progress Bars ---
st.write('\n')
st.subheader("💻 Technical Skills", divider="red")

def skill_bar(skill_name, level, color="#e63946"):
    """Create a visual skill bar. Level: 0-100"""
    st.markdown(f"""
    <div style='margin-bottom: 10px;'>
        <div style='display: flex; justify-content: space-between; margin-bottom: 2px;'>
            <span style='font-weight: 600;'>{skill_name}</span>
            <span style='color: #888;'>{level}%</span>
        </div>
        <div style='background: #2a2a4a; border-radius: 10px; height: 8px; overflow: hidden;'>
            <div style='background: {color}; width: {level}%; height: 100%; border-radius: 10px;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### ⚙️ Embedded Systems & Firmware")
skill_col1, skill_col2 = st.columns(2)

with skill_col1:
    skill_bar("C/C++", 90)
    skill_bar("Python", 85)
    skill_bar("FreeRTOS", 70)

with skill_col2:
    skill_bar("UART/SPI/I2C", 90)
    skill_bar("CAN", 65)
    skill_bar("VHDL/Verilog", 60)

st.markdown("### 🧩 Frameworks & Tools")
skill_col3, skill_col4 = st.columns(2)

with skill_col3:
    skill_bar("ROS / microROS", 70, "#9b5de5")
    skill_bar("KiCad", 85, "#9b5de5")

with skill_col4:
    skill_bar("Edge Impulse / TinyML", 65, "#9b5de5")
    skill_bar("OpenCV", 60, "#9b5de5")

st.markdown("### 🌐 Protocols & IoT")
skill_col5, skill_col6 = st.columns(2)

with skill_col5:
    skill_bar("MQTT", 75, "#2a9d8f")
    skill_bar("Modbus", 70, "#2a9d8f")

with skill_col6:
    skill_bar("LoRa", 65, "#2a9d8f")
    skill_bar("Embedded Linux", 60, "#2a9d8f")

# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("💼 Professional Experience", divider="red")

st.markdown(
    """
### Jr. Application Engineer @ [INBIODROID](https://inbiodroid.com/)
📅 **January – September 2025** | León, GTO, Mexico

**Key Achievements:**
- ✅ Developed **production firmware** for reflow oven control system using STM32F144
- ✅ Implemented **PID controller with Kalman filter** for precise temperature control
- ✅ Built **embedded web interface** (ESP01) for real-time monitoring and profile management
- ✅ Collaborated on **PCB design** for control board

**Technologies:** C, STM32 HAL, PID Control, Kalman Filter, HTML/CSS/JS, ESP8266

---

### Technical Advisor – Representative Teams @ Universidad La Salle Bajío
📅 **January 2024 – Present**

**Key Achievements:**
- ✅ Led electronics development for **Mars Rover** project (ROS/microROS, GNU Radio)
- ✅ Mentored students in **competitive robotics** (line followers, sumo robots)
- ✅ Designed custom circuits for competition robots

**Technologies:** ROS2, microROS, ESP32, STM32, KiCad, FreeRTOS

---

### Research Intern @ [CIO (Centro de Investigación en Óptica)](https://www.cio.mx/)
📅 **August – December 2023** | León, GTO, Mexico

**Key Achievements:**
- ✅ Contributed to **"Design and fabrication of microcoils for biomedical sensors"** project
- ✅ Performed **microfabrication processes** in cleanroom environment
- ✅ Conducted **electromagnetic simulations** using COMSOL Multiphysics
- ✅ Documented technical processes using **LaTeX**

**Technologies:** COMSOL Multiphysics, Cleanroom fabrication, LaTeX, MATLAB

---

### SMC Bushido Challenge Participant
📅 **September 2023**

- ⚙️ Industrial automation with **PLCs and electropneumatics**
- Problem-solving in pneumatics and hardwired logic

---

### English & Math Instructor @ [KUMON](https://www.kumon.com/mx-es/)
📅 **January 2021 – September 2022**

- 📚 Academic tutoring in English and Mathematics (elementary to high school)
- 💻 Office administration and educational content management
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("🎓 Education", divider="red")

st.markdown(
    """
### Bachelor's Degree in Electronics and Telecommunications Engineering
📍 **[Universidad La Salle Bajío](https://www.lasallebajio.edu.mx/)** | León, GTO, Mexico  
📅 **2021 – 2025 (Expected)**

**Relevant Coursework:** Digital Signal Processing, Control Systems, Microcontrollers, Power Electronics, Communication Systems, Embedded Systems Design
"""
)

# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("📜 Certifications & Training", divider="red")

st.markdown(
    """
| Certification | Institution | Date |
|--------------|-------------|------|
| Machine Tools Workshop | IECA León GTO | Feb – Mar 2022 |
| Neural Networks Course | IECA Online | Sep – Dec 2021 |
"""
)

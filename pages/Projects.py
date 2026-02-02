import streamlit as st
from streamlit_extras.mention import mention
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide", page_title="Projects | Adrián Silva Palafox")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Custom CSS for project cards
st.markdown("""
<style>
.project-card {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 20px;
    border-radius: 12px;
    border-left: 4px solid #e63946;
    margin-bottom: 20px;
}
.tech-tag {
    background: #2a2a4a;
    padding: 4px 12px;
    border-radius: 15px;
    margin-right: 8px;
    font-size: 0.85em;
    display: inline-block;
    margin-bottom: 5px;
}
.metric-box {
    background: rgba(230, 57, 70, 0.1);
    padding: 10px 15px;
    border-radius: 8px;
    text-align: center;
    border: 1px solid rgba(230, 57, 70, 0.3);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; font-weight:bold;'>🚀 Featured Projects</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; margin-bottom:30px;'>Production-ready embedded systems with demos and source code</p>", unsafe_allow_html=True)

# --- IMAGE LOADING ---
SCARA = Image.open("assets/SCARA.jpeg")
horno = Image.open("assets/horno.jpg")
estructura = Image.open("assets/estructura.jpeg")
stand = Image.open("assets/standcultivo.jpeg")
hongo = Image.open("assets/hongo.jpeg")
elec = Image.open("assets/eleclechu.png")
PIDfoco = Image.open("assets/PIDfoco.jpeg")
PIDbalancin = Image.open("assets/PIDbalancin.jpeg")
CNCx = Image.open("assets/CNC.jpeg")
tang20 = Image.open("assets/tang20k.jpeg")
tang9 = Image.open("assets/tang9k.jpeg")
controlpotencia = Image.open("assets/controlpotencia.jpeg")

# --- PROJECTS ---

# PROJECT: SCARA ROBOT
st.markdown("---")
with st.container():
    text_column, image_column = st.columns((3, 1))
    with text_column:
        st.markdown("### 🤖 SCARA Robot with microROS")
        
        # Tech tags
        st.markdown("""
        <span class='tech-tag'>ROS2</span>
        <span class='tech-tag'>microROS</span>
        <span class='tech-tag'>ESP32</span>
        <span class='tech-tag'>Raspberry Pi 5</span>
        <span class='tech-tag'>Computer Vision</span>
        <span class='tech-tag'>Modbus TCP</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Project Type:** Personal Project | Robotics & Automation
        
        #### 📋 Overview
        Autonomous SCARA robot for box sorting using computer vision, integrated with **microROS on ESP32** and **ROS2 on Raspberry Pi 5**.
        """)
        
        # Metrics
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown("<div class='metric-box'><b>100Hz</b><br>Control Rate</div>", unsafe_allow_html=True)
        with m2:
            st.markdown("<div class='metric-box'><b>±0.5mm</b><br>Accuracy</div>", unsafe_allow_html=True)
        with m3:
            st.markdown("<div class='metric-box'><b>4 DOF</b><br>Articulation</div>", unsafe_allow_html=True)
        
        st.markdown("""
        #### 🛠️ Technical Contributions
        - Stepper motor control with magnetic encoder feedback
        - Distributed communication architecture (microROS ↔ ROS2)
        - PLC integration via Modbus TCP for industrial compatibility
        - Custom user interface for remote operation
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Demo Video", icon="youtube", url="https://youtu.be/UwlWYntn_pg?si=N4t4PZQV8fb_UifI")
        with col2:
            mention(label="Source Code", icon="github", url="https://github.com/La-guajolota/Robotica/tree/main/proyects/SCARA_robot")
        with col3:
            mention(label="Extra Footage", icon="youtube", url="https://youtube.com/shorts/p9Vn9d3aslc?si=Wqwv5COZT4yjtEO0")

    with image_column:
        st.image(SCARA, caption="SCARA Robot with microROS")

# PROJECT: REFLOW OVEN
st.markdown("---")
with st.container():
    text_column, image_column = st.columns((3, 1))
    with text_column:
        st.markdown("### 🔥 Reflow Oven for PCBs")
        
        st.markdown("""
        <span class='tech-tag'>STM32F144</span>
        <span class='tech-tag'>ESP01</span>
        <span class='tech-tag'>PID Control</span>
        <span class='tech-tag'>Kalman Filter</span>
        <span class='tech-tag'>Web Interface</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Project Type:** Professional Project @ INBIODROID | Temperature Control
        
        #### 📋 Overview
        Production-ready reflow oven system for SMD soldering with precise temperature control and real-time monitoring.
        """)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown("<div class='metric-box'><b>±2°C</b><br>Precision</div>", unsafe_allow_html=True)
        with m2:
            st.markdown("<div class='metric-box'><b>5</b><br>Thermal Profiles</div>", unsafe_allow_html=True)
        with m3:
            st.markdown("<div class='metric-box'><b>Real-time</b><br>Web Monitoring</div>", unsafe_allow_html=True)
        
        st.markdown("""
        #### 🛠️ Technical Contributions
        - Digital PID with Kalman filter to counteract thermocouple thermal inertia
        - Programmable temperature profiles for different PCB types
        - Safety system with overheating protection
        - Embedded web interface for control and monitoring
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            mention(label="Demo Video", icon="youtube", url="https://youtu.be/XSk6v5LdElc?si=cIEzceQJt_Kj0cJl")
        with col2:
            mention(label="Source Code", icon="github", url="https://github.com/La-guajolota/Horno_reflujo")

    with image_column:
        st.image(horno, caption="Reflow oven for PCBs")

# PROJECT: SPOT WELDER
st.markdown("---")
with st.container():
    text_column, image_column = st.columns((3, 1))
    with text_column:
        st.markdown("### ⚡ Spot Welder Automation")
        
        st.markdown("""
        <span class='tech-tag'>PLC</span>
        <span class='tech-tag'>HMI</span>
        <span class='tech-tag'>STM32F103</span>
        <span class='tech-tag'>Pneumatics</span>
        <span class='tech-tag'>Power Control</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Project Type:** Academic Project | Industrial Automation
        
        #### 📋 Overview
        Industrial spot welding automation system with manual/automatic modes, voltage control, and cycle management.
        
        #### 🛠️ My Contributions
        - PLC programming for cycle control
        - Custom interface board (STM32F103C8T6) for voltage regulation
        - Potentiometer-based average voltage control
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Demo", icon="tiktok", url="https://vm.tiktok.com/ZMkf7bJaX/")
        with col2:
            mention(label="Test 1", icon="tiktok", url="https://vm.tiktok.com/ZMkfvYuPP/")
        with col3:
            mention(label="Test 2", icon="tiktok", url="https://vm.tiktok.com/ZMkfv5oLb/")

    with image_column:
        st.image(estructura, caption="Spot welder and control panel")

# PROJECT: CONTROL SYSTEMS
st.markdown("---")
with st.container():
    text_column, image_column = st.columns((3, 1))
    with text_column:
        st.markdown("### 🎛️ Control Systems Portfolio")
        
        st.markdown("""
        <span class='tech-tag'>PID</span>
        <span class='tech-tag'>PSoC 5LP</span>
        <span class='tech-tag'>Arduino</span>
        <span class='tech-tag'>LabVIEW</span>
        <span class='tech-tag'>Python</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Project Type:** Academic Projects | Control Theory Applications
        
        #### 📋 Projects Included
        
        **1. PID Balance Beam Control**
        - Brushless motor with magnetic encoder feedback
        - Real-time P-I-D tuning interface
        - Position and error visualization
        
        **2. PID Temperature Control (Incubator)**
        - Discrete PID on Arduino UNO
        - SSR with zero-crossing control
        - LabVIEW monitoring interface
        
        **3. 2-Axis Pixel Scanner**
        - DC motors with encoder feedback
        - IR LED emitter/receiver pair
        - Python terminal interface
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Balance Beam", icon="tiktok", url="https://vm.tiktok.com/ZMkfK9REL/")
        with col2:
            mention(label="Incubator", icon="youtube", url="https://youtu.be/9GzK51KK4rQ?si=dXn9kD5sQDgz_Gij")
        with col3:
            mention(label="Pixel Scanner", icon="youtube", url="https://youtube.com/shorts/1h-Tq7sl8uE?si=FEmKmIi90RWEy_bA")

    with image_column:
        st.image(PIDbalancin, caption="Balance beam")
        st.image(PIDfoco, caption="Temperature control")
        st.image(CNCx, caption="Pixel scanner")

# PROJECT: FPGA BOARDS
st.markdown("---")
with st.container():
    text_column, image_column = st.columns((3, 1))
    with text_column:
        st.markdown("### 📐 FPGA Trainer Boards & Power Controller")
        
        st.markdown("""
        <span class='tech-tag'>KiCad</span>
        <span class='tech-tag'>FPGA</span>
        <span class='tech-tag'>Tang Nano</span>
        <span class='tech-tag'>RS-485</span>
        <span class='tech-tag'>SCR Control</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Project Type:** Personal Projects | PCB Design & Commercialization
        
        #### 📋 Products Developed
        
        **Tang Nano 9K/20K Breakout Boards**
        - Tri-state multiplexed LED matrix
        - 4-digit 7-segment display
        - Module slots (MPU6050, ESP01, DHT11/22)
        - HDMI/SD card access preserved
        
        **Inductive Load Power Controller**
        - RS-485 + analog voltage communication
        - Anti-parallel SCR configuration
        - Optional snubber network
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="9K Board Demo", icon="youtube", url="https://youtube.com/shorts/1Tsm5lJ4Fyw?si=9BlyFCejvi8cHO8Q")
        with col2:
            mention(label="Example", icon="tiktok", url="https://vm.tiktok.com/ZMkfKRUMX/")
        with col3:
            mention(label="Power Controller", icon="tiktok", url="https://vm.tiktok.com/ZMkfKNdn2/")

    with image_column:
        st.image(tang9, caption="Tang Nano 9K board")
        st.image(tang20, caption="Tang Nano 20K board")
        st.image(controlpotencia, caption="Power controller")

# PROJECT: SMART FARMING
st.markdown("---")
with st.container():
    text_column, image_column = st.columns((3, 1))
    with text_column:
        st.markdown("### 🌱 Smart Urban Farming System")
        
        st.markdown("""
        <span class='tech-tag'>IoT</span>
        <span class='tech-tag'>MQTT</span>
        <span class='tech-tag'>ESP32</span>
        <span class='tech-tag'>Hydroponics</span>
        <span class='tech-tag'>Machine Learning</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Project Type:** Personal Project | Precision Agriculture | **Currently Active**
        
        #### 📋 Overview
        Autonomous control system for urban vertical farming with real-time monitoring, intelligent dosing, and data-driven optimization.
        
        #### 🏆 Achievements
        - LED intensity control board with overcurrent protection
        - MQTT-based mobile/web dashboard
        - Custom IoT sensor network design
        - Digital filters for analog sensors
        - Ion-selective electrode research (ongoing)
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Documentation", icon="youtube", url="https://www.youtube.com/watch?v=h5dIs2VbnKQ&list=PLz4Si3LTpIHn8Sm7qZtzyirCftxZIDVzY&index=3")
        with col2:
            mention(label="Source Code", icon="github", url="https://github.com/La-guajolota/Libre-cultivo")
        with col3:
            mention(label="Mushrooms", icon="tiktok", url="https://vm.tiktok.com/ZMkfKCyKS/")

    with image_column:
        st.image(stand, caption="Urban farming stand")
        st.image(hongo, caption="Mushroom cultivation")
        st.image(elec, caption="Control prototype")
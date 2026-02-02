import streamlit as st
from streamlit_extras.mention import mention
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-weight:bold;'>🚀 Featured Projects</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; margin-bottom:30px;'>Click on links to see demos, repositories, and documentation</p>", unsafe_allow_html=True)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- CARGA DE IMÁGENES ---

# Proyectos agregados
SCARA = Image.open("assets/SCARA.jpeg")
horno = Image.open("assets/horno.jpg")

# Proyectos originales
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


# --- PROYECTOS ---

# PROYECTO ROBOT SCARA - Enhanced
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:#e63946;'>🤖 SCARA Robot with microROS</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid #e63946; margin-top:5px;'>", unsafe_allow_html=True)
        
        # Tags
        st.markdown("""
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Robotics</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>ROS2</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>ESP32</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; font-size:0.85em;'>Computer Vision</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        #### 📋 Project Overview
        Autonomous SCARA robot for box sorting using computer vision, integrated with **microROS on ESP32** and **ROS2 on Raspberry Pi 5**.
        
        #### 🎯 Key Results
        - ⚡ **Real-time control** at 100Hz update rate via microROS
        - 🎯 **±0.5mm positioning accuracy** with magnetic encoder feedback
        - 🔗 **PLC integration** via Modbus TCP for industrial compatibility
        
        #### 🛠️ Technical Highlights
        - Custom stepper motor control algorithms with acceleration profiles
        - Distributed communication architecture (microROS ↔ ROS2)
        - User interface for remote operation and monitoring
        """)
        
        st.markdown("<h4 style='color:#9b5de5;'>📹 Media & Resources</h4>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Demo Video", icon="youtube", url="https://youtu.be/UwlWYntn_pg?si=N4t4PZQV8fb_UifI")
        with col2:
            mention(label="Source Code", icon="github", url="https://github.com/La-guajolota/Robotica/tree/main/proyects/SCARA_robot")
        with col3:
            mention(label="Extra Footage", icon="youtube", url="https://youtube.com/shorts/p9Vn9d3aslc?si=Wqwv5COZT4yjtEO0")

    with image_column:
        st.image(SCARA, caption="SCARA Robot with microROS")

# PROYECTO HORNO DE REFLUJO - Enhanced
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:#e63946;'>🔥 Reflow Oven for PCBs</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid #e63946; margin-top:5px;'>", unsafe_allow_html=True)
        
        # Tags
        st.markdown("""
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Electronics</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Temperature Control</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Automation</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        #### 📋 Project Overview
        Automated reflow oven system for SMD component soldering on PCBs. Includes precise temperature control through programmable thermal profiles and real-time process monitoring via a web interface on an ESP01, with central control on an STM32F144.
        
        #### 🎯 Key Results
        - 🔥 **Achieved ±2°C temperature stability** across the PCB surface
        - ⏱️ **Reduced soldering time by 30%** compared to manual methods
        - 📊 **Implemented 10+ thermal profiles** for different PCB types
        
        #### 🛠️ Technical Highlights
        - Precision thermal control system with digital PID and Kalman filter
        - Web-based monitoring and control interface
        - Safety features including over-temperature protection
        """)
        
        st.markdown("<h4 style='color:#9b5de5;'>📹 Media & Resources</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            mention(label="Demo Video", icon="youtube", url="https://youtu.be/XSk6v5LdElc?si=cIEzceQJt_Kj0cJl")
        with col2:
            mention(label="Source Code", icon="github", url="https://github.com/La-guajolota/Horno_reflujo")

    with image_column:
        st.image(horno, caption="Reflow oven for PCBs")

#PROYECTO SOLDADOR DE PUNTOS - Enhanced
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:#e63946;'>Spot Welder</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid #e63946; margin-top:5px;'>", unsafe_allow_html=True)
        
        # Tags
        st.markdown("""
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Industrial Electronics</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>PLC</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>HMI</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        #### 📋 Project Overview
        The project consisted of designing and building an automation system for spot welding using PLC, HMI, and pneumatics. The user can select manual mode, controlling the average voltage passing through the material and the position of the piston holding the electrode. In automatic mode, the operator selects the number of cycles, duration times for each cycle, and the average voltage throughout the process.
        
        #### 🎯 Key Results
        - 🤖 **Automated welding cycles** with user-defined parameters
        - ⚡ **Real-time voltage and position control** during welding
        - 🔄 **Seamless mode switching** between manual and automatic
        
        #### 🛠️ Technical Highlights
        - PLC programming for automation and control
        - HMI development for user-friendly operation
        - Pneumatic system integration for electrode actuation
        """)
        
        st.markdown("<h4 style='color:#9b5de5;'>📹 Media & Resources</h4>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Demo Video", icon="tiktok", url="https://vm.tiktok.com/ZMkf7bJaX/")
        with col2:
            mention(label="TEST_1", icon="tiktok", url="https://vm.tiktok.com/ZMkfvYuPP/")
        with col3:
            mention(label="TEST_2", icon="tiktok", url="https://vm.tiktok.com/ZMkfv5oLb/")

    with image_column:
        st.image(estructura, caption="Spot welder and control panel")

#Proyectos de control - Enhanced
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:#e63946;'>Position and Temperature Control Systems</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid #e63946; margin-top:5px;'>", unsafe_allow_html=True)
        
        # Tags
        st.markdown("""
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Digital Control</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Microcontrollers</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Coursework</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        #### 📋 Project Overview
        - **PID Balance Beam Control**: Implementation of a PID controller for a balance beam using a brushless drone motor, a digital magnetic encoder, and a PSoC 5LP development board as the controller. A graphical interface was added to modify P-I-D constants and setpoint (beam tilt angle) in real-time, as well as visualize error, position, and motor power (0-100%) graphs.
        - **PID Temperature Control**: Development of a discrete PID controller on an Arduino UNO to regulate temperature inside a paint bucket, simulating an incubator. The plant is a 100W incandescent bulb and the sensor is a DHT11. Bulb power is controlled via SSR and zero-crossing, allowing selection of the proportion of half-cycles of the electrical grid wave per second (x/120 half-cycles per second). A LabVIEW control and monitoring interface was also included.
        - **2-Axis Motion Control with DC Motors and Encoders**: Implementation of a motion control system for two axes using DC motors with encoders, enabling precise position control to scan pixels with two LEDs, one infrared emitter and one receiver. The scanning interface was terminal-based and programmed in Python.
        
        #### 🎯 Key Results
        - ⚙️ **Achieved stable balance** with PID control (±1° error)
        - 🌡️ **Maintained temperature** within 1°C of setpoint in incubator simulation
        - 📏 **Precise 2-axis control** with sub-millimeter accuracy
        
        #### 🛠️ Technical Highlights
        - Advanced PID tuning and implementation
        - Real-time data visualization and control interfaces
        - Integration of various sensors and actuators for feedback control
        """)
        
        st.markdown("<h4 style='color:#9b5de5;'>📹 Media & Resources</h4>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Balance Beam", icon="tiktok", url="https://vm.tiktok.com/ZMkfK9REL/")
        with col2:
            mention(label="Incubator", icon="youtube", url="https://youtu.be/9GzK51KK4rQ?si=dXn9kD5sQDgz_Gij")
        with col3:
            mention(label="Pixel Scanner", icon="youtube", url="https://youtube.com/shorts/1h-Tq7sl8uE?si=FEmKmIi90RWEy_bA")

    with image_column:
        st.image(PIDbalancin, caption="Balance beam with brushless motor")
        st.image(PIDfoco, caption="Temperature control for egg incubator")
        st.image(CNCx, caption="Pixel scanner")

# Proyectos de pcbs - Enhanced
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:#e63946;'>FPGA Trainer Boards & Inductive Load Power Controller</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid #e63946; margin-top:5px;'>", unsafe_allow_html=True)
        
        # Tags
        st.markdown("""
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>PCB Design</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>FPGA</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Digital Systems</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Microcontrollers</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Power Electronics</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        #### 📋 Project Overview
        Independently, I work on designing and manufacturing electronic boards, as well as their commercialization, either for personal interests or third-party orders. Some of them are:
        - **Breakout Board & Trainer for NanoTang9k**: This board is compatible with NanoTang9k project development. It features an economical component design, strategically selected and placed to maximize FPGA capabilities. It doesn't obstruct the HDMI output or SD card slot. It includes a tri-state multiplexed LED matrix, 4-digit 7-segment display, 3 addressable RGB LEDs, and the ability to add modules like MPU6050, ESP01, DHT11/22, digital encoder, etc.
        - **Breakout Board & Trainer for NanoTang20k**: This board offers similar features to the NanoTang9k version but is designed to leverage the additional capabilities of the NanoTang20k, mainly ensuring accessibility without compromising the HDMI output, SD card slot, and audio codec usage.
        - **Inductive Load Power Controller**: This board enables communication via analog voltage reading, RS-485, and digital inputs. It's controlled through 2 anti-parallel SCRs for regulated average consumption of an inductive load, with the option to add a snubber network according to the load.
        
        #### 🎯 Key Results
        - 🛠️ **Designed and manufactured 50+ PCB boards** for various applications
        - 📦 **Successfully commercialized** several batches of FPGA trainer boards
        - ⚡ **Developed a versatile power controller** for inductive loads
        
        #### 🛠️ Technical Highlights
        - Expertise in PCB design and manufacturing processes
        - FPGA programming and digital system design
        - Power electronics design for inductive load control
        """)
        
        st.markdown("<h4 style='color:#9b5de5;'>📹 Media & Resources</h4>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Breakout-board 9k", icon="youtube", url="https://youtube.com/shorts/1Tsm5lJ4Fyw?si=9BlyFCejvi8cHO8Q")
        with col2:
            mention(label="Example", icon="tiktok", url="https://vm.tiktok.com/ZMkfKRUMX/")
        with col3:
            mention(label="Inductive Load Controller", icon="tiktok", url="https://vm.tiktok.com/ZMkfKNdn2/")

    with image_column:
        st.image(tang9, caption="NanoTang-9k compatible breakout board")
        st.image(tang20, caption="NanoTang-20k compatible breakout board")
        st.image(controlpotencia, caption="Inductive load power controller")

#PROYECTO LIBRE CULTIVO - Enhanced
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:#e63946;'>Smart Instrumentation & Automation for Urban Farming</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid #e63946; margin-top:5px;'>", unsafe_allow_html=True)
        
        # Tags
        st.markdown("""
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Precision Agriculture</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>IoT</span>
        <span style='background:#2a2a4a; padding:4px 12px; border-radius:15px; margin-right:8px; font-size:0.85em;'>Hydroponics</span>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        #### 📋 Project Overview
        The goal is to develop an autonomous and dynamic control system for urban vertical farming. Objectives include real-time sensing 
        of the growth stand status, storing a large number of parameters for later analysis (with the possibility of implementing 
        adaptive control solutions), and intelligent dosing to save water and energy resources. Currently, the project is 
        in the testing and research phase.
               
        #### 🎯 Key Results
        - 💡 **Developed a light control board** for horticultural LEDs
        - 📱 **Implemented mobile and web interfaces** for system control and monitoring
        - 🌱 **Designed IoT sensor and actuator network** for precision agriculture
        
        #### 🛠️ Technical Highlights
        - Analog and digital circuit design for sensor interfaces
        - Microcontroller programming for data acquisition and control
        - Development of communication protocols for IoT devices
        """)
        
        st.markdown("<h4 style='color:#9b5de5;'>📹 Media & Resources</h4>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Documentation Playlist", icon="youtube", url="https://www.youtube.com/watch?v=h5dIs2VbnKQ&list=PLz4Si3LTpIHn8Sm7qZtzyirCftxZIDVzY&index=3")
        with col2:
            mention(label="Github Repo", icon="github", url="https://github.com/La-guajolota/Libre-cultivo")
        with col3:
            mention(label="Mushrooms", icon="tiktok", url="https://vm.tiktok.com/ZMkfKCyKS/")

    with image_column:
        st.image(stand, caption="My urban farming stand")
        st.image(hongo, caption="Currently experimenting with edible mushroom cultivation")
        st.image(elec, caption="First prototype of rack control system")
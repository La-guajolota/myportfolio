import streamlit as st
from streamlit_extras.mention import mention
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-weight:bold;'>Featured Projects & Practical Work</h1>", unsafe_allow_html=True)

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

# PROYECTO ROBOT SCARA
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>🤖 SCARA Robot with microROS</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Robotics • ROS2 • Microcontrollers • Personal Project*")
        st.markdown("""
            - ⚙️ **Description**:
            - Programming of a SCARA robot integrated with microROS on ESP32 and ROS on a Raspberry Pi 5 for box collection using computer vision.
            
            🛠️ **Contributions**:
            - Stepper motor control with magnetic encoder feedback.
            - Successful integration of microROS with ROS2 for distributed communication.
            - Development of control algorithms for stepper motors.
            - Creation of user interface for remote robot control.
            - Integration of PLC communication via Modbus TCP.
        """)
        st.markdown("<h2 style='color:purple;'>Audiovisual Evidence</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Demo", icon="youtube", url="https://youtu.be/UwlWYntn_pg?si=N4t4PZQV8fb_UifI")
        with col2:
            mention(label="Repository", icon="github", url="https://github.com/La-guajolota/Robotica/tree/main/proyects/SCARA_robot")
        with col3:
            mention(label="Extra", icon="youtube", url="https://youtube.com/shorts/p9Vn9d3aslc?si=Wqwv5COZT4yjtEO0")

    with image_column:
        st.image(SCARA, caption="SCARA Robot with microROS")

# PROYECTO HORNO DE REFLUJO
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>🔥 Reflow Oven for PCBs</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Electronics • Temperature Control • Automation • Personal Project*")
        st.markdown("""
            - ⚙️ **Description**:
            - Automated reflow oven system for SMD component soldering on PCBs. Includes precise temperature control through programmable thermal profiles and real-time process monitoring via a web interface on an ESP01, with central control on an STM32F144.
            
            🛠️ **Contributions**:
            - Design and implementation of precision thermal control system.
            - Development of programmable temperature profiles for different PCB types.
            - Real-time monitoring and control interface.
            - Safety system with overheating protection.
            - Digital PID with Kalman filter to counteract thermocouple thermal inertia.
        """)
        st.markdown("<h2 style='color:purple;'>Audiovisual Evidence</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            mention(label="Demo", icon="youtube", url="https://youtu.be/XSk6v5LdElc?si=cIEzceQJt_Kj0cJl")
        with col2:
            mention(label="Repository", icon="github", url="https://github.com/La-guajolota/Horno_reflujo")

    with image_column:
        st.image(horno, caption="Reflow oven for PCBs")

#PROYECTO SOLDADOR DE PUNTOS
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>Spot Welder</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Industrial Electronics • Coursework • Team Project*")
        st.markdown("""
            - ⚙️ **Description**:
            - The project consisted of designing and building an automation system for spot welding using PLC, HMI, and pneumatics. The user can select manual mode, controlling the average voltage passing through the material and the position of the piston holding the electrode. In automatic mode, the operator selects the number of cycles, duration times for each cycle, and the average voltage throughout the process.
            
            🛠️ **My Contributions**:
            I collaborated on PLC programming and designed a control board to interface with the control panel.
            This board allows control of the average voltage passing through the material via a potentiometer.
            The board was implemented with an STM32F103C8T6, the same one featured on this page.
        """)
        st.markdown("<h2 style='color:purple;'>Audiovisual Evidence</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Demo", icon="tiktok", url="https://vm.tiktok.com/ZMkf7bJaX/")
        with col2:
            mention(label="TEST_1", icon="tiktok", url="https://vm.tiktok.com/ZMkfvYuPP/")
        with col3:
            mention(label="TEST_2", icon="tiktok", url="https://vm.tiktok.com/ZMkfv5oLb/")

    with image_column:
        st.image(estructura, caption="Spot welder and control panel")

#Proyectos de control
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>Position and Temperature Control Systems</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Digital Control • Microcontrollers • Coursework • Team Projects*")
        st.markdown("""
            - ⚙️ **PID Balance Beam Control**: 
            - Implementation of a PID controller for a balance beam using a brushless drone motor, a digital magnetic encoder, and a PSoC 5LP development board as the controller. A graphical interface was added to modify P-I-D constants and setpoint (beam tilt angle) in real-time, as well as visualize error, position, and motor power (0-100%) graphs.
            - 🌡️ **PID Temperature Control**: 
            - Development of a discrete PID controller on an Arduino UNO to regulate temperature inside a paint bucket, simulating an incubator. The plant is a 100W incandescent bulb and the sensor is a DHT11. Bulb power is controlled via SSR and zero-crossing, allowing selection of the proportion of half-cycles of the electrical grid wave per second (x/120 half-cycles per second). A LabVIEW control and monitoring interface was also included.
            - 🔧 **2-Axis Motion Control with DC Motors and Encoders**: 
            - Implementation of a motion control system for two axes using DC motors with encoders, enabling precise position control to scan pixels with two LEDs, one infrared emitter and one receiver. The scanning interface was terminal-based and programmed in Python.
            
            🛠️ **Contributions**:
            1. In all projects, I was responsible for microcontroller programming, control algorithm implementation, and the control/monitoring interface (except for the temperature control project).
        """)
        st.markdown("<h2 style='color:purple;'>Audiovisual Evidence</h2>", unsafe_allow_html=True)
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

# Proyectos de pcbs 
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>FPGA Trainer Boards & Inductive Load Power Controller</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*PCB Design • FPGA • Digital Systems • Microcontrollers • Power Electronics • Personal Projects*")
        st.markdown("""
            - 🔧 **Overview**: 
            - Independently, I work on designing and manufacturing electronic boards, as well as their commercialization, either for personal interests or third-party orders. Some of them are:
            - 🛠️ **Breakout Board & Trainer for NanoTang9k**:
            - This board is compatible with NanoTang9k project development. It features an economical component design, strategically selected and placed to maximize FPGA capabilities. It doesn't obstruct the HDMI output or SD card slot. It includes a tri-state multiplexed LED matrix, 4-digit 7-segment display, 3 addressable RGB LEDs, and the ability to add modules like MPU6050, ESP01, DHT11/22, digital encoder, etc.
            - 🛠️ **Breakout Board & Trainer for NanoTang20k**:
            - This board offers similar features to the NanoTang9k version but is designed to leverage the additional capabilities of the NanoTang20k, mainly ensuring accessibility without compromising the HDMI output, SD card slot, and audio codec usage.
            - ⚡ **Inductive Load Power Controller**:
            - This board enables communication via analog voltage reading, RS-485, and digital inputs. It's controlled through 2 anti-parallel SCRs for regulated average consumption of an inductive load, with the option to add a snubber network according to the load.
            
            📋 **Activities**:
            1. Design and manufacturing of electronic boards.
            2. Programming, electronic design, and testing of developed systems.
            3. Commercialization and technical support for products.
        """)
        st.markdown("<h2 style='color:purple;'>Audiovisual Evidence</h2>", unsafe_allow_html=True)
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

#PROYECTO LIBRE CULTIVO
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>Smart Instrumentation & Automation for Urban Farming</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Precision Agriculture • Personal Project • Currently Active*")
        st.markdown("""
            - 🥬 **Description**:
            The goal is to develop an autonomous and dynamic control system for urban vertical farming. Objectives include real-time sensing 
            of the growth stand status, storing a large number of parameters for later analysis (with the possibility of implementing 
            adaptive control solutions), and intelligent dosing to save water and energy resources. Currently, the project is 
            in the testing and research phase.
               
            🥬 **Achievements**:
            1. Design of a light intensity control board for horticultural LEDs, including overvoltage and overcurrent protection.
            2. Mobile and web control/monitoring interface via MQTT.
            3. Design of my own IoT sensor and actuator network system. I'm still working on the analog design of ion-selective electrode sensors to measure nutrient concentration and water quality.
            4. Implementation of digital filters for analog sensors, as well as efficient statistical methods for microcontrollers.
            5. Continuous learning of hydroponic and aeroponic cultivation techniques (still in progress).
            6. Continuous learning and currently in the process of machine learning for crop parameter optimization.
        """)
        st.markdown("<h2 style='color:purple;'>Audiovisual Evidence</h2>", unsafe_allow_html=True)
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
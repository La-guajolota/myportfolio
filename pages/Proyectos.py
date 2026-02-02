import streamlit as st
from streamlit_extras.mention import mention
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-weight:bold;'>Proyectos y prácticas destacables</h1>", unsafe_allow_html=True)

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
        st.markdown("<h2 style='color:red;'>🤖 Robot SCARA con microROS</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Robótica • ROS2 • Microcontroladores • Proyecto Personal*")
        st.markdown("""
            - ⚙️ **Descripción**:
            - Programación de un robot SCARA integrado con microROS en ESP32 y ROS en una raspberry 5 para recolección de cajas por medio de visión artificial.
            
            🛠️ **Aportes**:
            - Control de motores paso a paso con retroalimentación de encoders magnéticos.
            - Integración exitosa de microROS con ROS2 para comunicación distribuida.
            - Desarrollo de algoritmos de control para motores paso a paso.
            - Creación de interfaz de usuario para control remoto del robot.
            - Integración de comunicación a un PLC por modbus TCP.
        """)
        st.markdown("<h2 style='color:purple;'>Evidencia Audiovisual</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Demo", icon="youtube", url="https://youtu.be/UwlWYntn_pg?si=N4t4PZQV8fb_UifI")
        with col2:
            mention(label="Repositorio", icon="github", url="https://github.com/La-guajolota/Robotica/tree/main/proyects/SCARA_robot")
        with col3:
            mention(label="Extra", icon="youtube", url="https://youtube.com/shorts/p9Vn9d3aslc?si=Wqwv5COZT4yjtEO0")

    with image_column:
        st.image(SCARA, caption="Robot SCARA con microROS")

# PROYECTO HORNO DE REFLUJO
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>🔥 Horno de Reflujo para PCBs</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Electrónica • Control de Temperatura • Automatización • Proyecto Personal*")
        st.markdown("""
            - ⚙️ **Descripción**:
            - Sistema automatizado de horno de reflujo para soldadura de componentes SMD en PCBs. Incluye control preciso de temperatura mediante perfiles térmicos programables y monitoreo en tiempo real del proceso dentro de una interfaz web en una ESP01, con el control central en un STM32F144.
            
            🛠️ **Aportes**:
            - Diseño e implementación de sistema de control térmico de precisión.
            - Desarrollo de perfiles de temperatura programables para diferentes tipos de PCB.
            - Interfaz de monitoreo y control en tiempo real.
            - Sistema de seguridad con protecciones contra sobrecalentamiento.
            - PID digital con filtro de Kalman para contrarestar la inercia térmica del termopar.
        """)
        st.markdown("<h2 style='color:purple;'>Evidencia Audiovisual</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            mention(label="Demo", icon="youtube", url="https://youtu.be/XSk6v5LdElc?si=cIEzceQJt_Kj0cJl")
        with col2:
            mention(label="Repositorio", icon="github", url="https://github.com/La-guajolota/Horno_reflujo")

    with image_column:
        st.image(horno, caption="Horno de reflujo para PCBs")

#PROYECTO SOLDADOR DE PUNTOS
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>Soldador de puntos</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Electrónica industrial - asignatura - equipo*")
        st.markdown("""
            - ⚙️ **Descripción**:
            - El proyecto consistió en diseñar y construir una automatización para soldadura por puntos utilizando PLC, HMI y neumática. El usuario puede seleccionar un modo manual, en el cual controla el voltaje promedio que pasa por el material y la posición del pistón que sujeta el electrodo. En modo automático, el operador selecciona la cantidad de ciclos, los tiempos de duración de cada ciclo y el voltaje promedio durante todo el proceso.
            
            🛠️ **Mis aportes**:
            Colaboré en la programación del PLC y en el diseño de una tarjeta de control para interfazar con el tablero de control.
            Esta tarjeta permite controlar el voltaje promedio que pasa por el material mediante un potenciómetro.
            La tarjeta fue implementada con un STM32f103c8t6. La misma que se encuentra en esta página.
        """)
        st.markdown("<h2 style='color:purple;'>Evidencia Audiovisual</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Demostración", icon="tiktok", url="https://vm.tiktok.com/ZMkf7bJaX/")
        with col2:
            mention(label="TEST_1", icon="tiktok", url="https://vm.tiktok.com/ZMkfvYuPP/")
        with col3:
            mention(label="TEST_2", icon="tiktok", url="https://vm.tiktok.com/ZMkfv5oLb/")

    with image_column:
        st.image(estructura, caption="Soldadora de puntos y panel de control")

#Proyectos de control
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>Controles de posición y temperatura</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Control digital | microcontroladores | asignatura | Equipo*")
        st.markdown("""
            - ⚙️ **Control PID de Balancín**: 
            - Implementación de un control PID para un balancín utilizando un motor brushless de dron, un encoder magnético digital y una placa de desarrollo PSoc 5LP como controlador. Se añadió una interfaz gráfica para modificar en tiempo real las constantes P-I-D y el setpoint (ángulo de inclinación del balancín), además de visualizar gráficas del error, la posición y la potencia del motor (0-100%).
            - 🌡️ **Control PID de Temperatura**: 
            - Desarrollo de un control PID discreto en un Arduino UNO para regular la temperatura dentro de una cubeta de pintura, simulando una incubadora. La planta es un foco incandescente de 100W y el sensor es un DHT11. Se controla la potencia del foco mediante un SSR y cruce por cero, permitiendo seleccionar la proporción de semiciclos de la onda de la red eléctrica en un segundo (x/120 semiciclos por segundo). También se incluyó una interfaz de control y monitoreo en LabVIEW para visualizar la temperatura actual y controlar los setpoints.
            - 🔧 **Control de Movimiento de 2 Ejes con Motores DC con Encoder**: 
            - Implementación de un sistema de control de movimiento para dos ejes utilizando motores DC con encoders, permitiendo un control preciso de la posición para escanear los píxeles con dos LEDs, uno emisor y otro receptor infrarrojo. La interfaz del escaneo fue en un terminal y programada en Python.
            
            🛠️ **Aportes**:
            1. En todos los proyectos, fui responsable de la programación de los microcontroladores, la implementación de los algoritmos de control y la interfaz de control y monitoreo (a excepción del control de temperatura).
        """)
        st.markdown("<h2 style='color:purple;'>Evidencia Audiovisual</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Balancín", icon="tiktok", url="https://vm.tiktok.com/ZMkfK9REL/")
        with col2:
            mention(label="Incubadora", icon="youtube", url="https://youtu.be/9GzK51KK4rQ?si=dXn9kD5sQDgz_Gij")
        with col3:
            mention(label="Scanner de píxeles", icon="youtube", url="https://youtube.com/shorts/1h-Tq7sl8uE?si=FEmKmIi90RWEy_bA")

    with image_column:
        st.image(PIDbalancin, caption="Balancín con motor brushless")
        st.image(PIDfoco, caption="Control de temperatura para incubadora de huevos")
        st.image(CNCx, caption="Scanner de píxeles")

# Proyectos de pcbs 
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>Tarjetas entrenadoras para FPGA y un control de consumo para cargas inductivas</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*PCB | FPGA | Digital | Microcontrolador | Electrónica de potencia | Proyectos personales*")
        st.markdown("""
            - 🔧 **General**: 
            - De manera independiente, trabajo en el diseño y fabricación de tarjetas electrónicas, así como en su comercialización, ya sea por afinidades propias o encargos de terceros. Algunas de ellas son las siguientes:
            - 🛠️ **Breakout-board y tarjeta entrenadora para la NanoTang9k**:
            - Esta tarjeta es compatible con el desarrollo de proyectos utilizando la NanoTang9k. Tiene un diseño económico de componentes, estratégicamente seleccionados y colocados para maximizar las capacidades de la FPGA. No impide el uso de la salida HDMI ni del slot de SDcard. Cuenta con una matriz de LEDs por multiplexación tri-state, display de 7 segmentos con 4 dígitos, 3 LEDs RGB direccionables, y la posibilidad de colocar módulos como el MPU6050, ESP01, DHT11/22, encoder digital, etc.
            - 🛠️ **Breakout-board y tarjeta entrenadora para la NanoTang20k**:
            - Esta tarjeta ofrece características similares a la NanoTang9k, pero está diseñada para aprovechar las capacidades adicionales de la NanoTang20k, principalmente asegurando la accesibilidad sin comprometer la salida HDMI, el slot de SDcard y el uso de códecs de audio.
            - ⚡ **Controlador de consumo para cargas inductivas**:
            - Esta tarjeta permite la comunicación mediante lectura analógica de voltaje, RS-485 y entradas digitales. Se controla por medio de 2 SCR antiparalelos para el consumo promedio regulado de una carga inductiva, y se le puede agregar una red snubber de acuerdo a la carga.
            
            📋 **Actividades**:
            1. Diseño y fabricación de tarjetas electrónicas.
            2. Programación, diseño electrónico y pruebas de los sistemas desarrollados.
            3. Comercialización y soporte técnico de los productos.
        """)
        st.markdown("<h2 style='color:purple;'>Evidencia Audiovisual</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Breakout-board 9k", icon="youtube", url="https://youtube.com/shorts/1Tsm5lJ4Fyw?si=9BlyFCejvi8cHO8Q")
        with col2:
            mention(label="Ejemplo", icon="tiktok", url="https://vm.tiktok.com/ZMkfKRUMX/")
        with col3:
            mention(label="Controlador de cargas inductivas", icon="tiktok", url="https://vm.tiktok.com/ZMkfKNdn2/")

    with image_column:
        st.image(tang9, caption="Breakout-board NanoTang-9k compatible")
        st.image(tang20, caption="Breakout-board NanoTang-20k compatible")
        st.image(controlpotencia, caption="Controlador de consumo para cargas inductivas")

#PROYECTO LIBRE CULTIVO
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.markdown("<h2 style='color:red;'>Instrumentalización y automatización inteligente de cultivo urbano</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)
        st.write("*Agricultura de precisión - proyecto personal - actualmente activo*")
        st.markdown("""
            - 🥬 **Descripción**:
            El objetivo es desarrollar un sistema de control autónomo y dinámico para un cultivo vertical urbano. Las metas incluyen sensar en tiempo real 
            el estado del stand de crecimiento, almacenar una gran cantidad de parámetros para análisis posteriores (con la posibilidad de implementar 
            soluciones de control adaptativo) y dosificar inteligentemente para economizar recursos hídricos y energéticos. Actualmente, el proyecto se encuentra 
            en fase de pruebas e investigación.
               
            🥬 **Logros**:
            1. Diseño de una tarjeta de control de intensidad lumínica de LEDs de horticultura, incluyendo protección contra sobretensiones y corrientes.
            2. Interfaz de control y monitoreo móvil y web por MQTT.
            3. Diseño de mi propio sistema de red de sensores y actuadores (IoT). Aún estoy trabajando en el diseño analógico de sensores con electrodos selectivos de iones para medir la concentración de nutrientes y la calidad del agua.
            4. Implementación de filtros digitales para sensores analógicos, así como métodos estadísticos eficientes en microcontroladores.
            5. Aprendizaje constante de las técnicas de cultivo hidropónico y aeropónico (aún en progreso). 
            6. Aprendizaje constante y actualmente en proceso de machine learning para la optimización de los parámetros de cultivo.
        """)
        st.markdown("<h2 style='color:purple;'>Evidencia Audiovisual</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            mention(label="Playlist-documentación", icon="youtube", url="https://www.youtube.com/watch?v=h5dIs2VbnKQ&list=PLz4Si3LTpIHn8Sm7qZtzyirCftxZIDVzY&index=3")
        with col2:
            mention(label="Github Repo", icon="github", url="https://github.com/La-guajolota/Libre-cultivo")
        with col3:
            mention(label="Champiñones", icon="tiktok", url="https://vm.tiktok.com/ZMkfKCyKS/")

    with image_column:
        st.image(stand, caption="Este es mi stand de cultivo urbano")
        st.image(hongo, caption="Actualmente experimento con el cultivo de zetas comestibles")
        st.image(elec, caption="El primer prototipado de control del rack")
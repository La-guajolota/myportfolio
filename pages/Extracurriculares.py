import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; font-weight:bold; margin-bottom:0;'>Actividades Extracurriculares</h2>", unsafe_allow_html=True)
st.markdown("<hr style='border:2px solid red; margin-top:5px;'>", unsafe_allow_html=True)

# Images
cio = Image.open('assets/ciologo.png')
cioid = Image.open('assets/ciocredencial.jpeg')
cioid = cioid.crop((0, 200, cioid.width, cioid.height - 200))

baja0 = Image.open('assets/baja0.jpeg')
baja1 = Image.open('assets/torneado.jpeg')
baja2 = Image.open('assets/baja2.jpeg')

robotica0 = Image.open('assets/buckdisenno.jpeg')
robotica1 = Image.open('assets/3d.jpeg')

bushido = Image.open('assets/bushido.png')
bushteam = Image.open('assets/equipobushido.jpeg')

lechuga = Image.open('assets/lechuagerminado.jpeg')
lechuga2 = Image.open('assets/lechugaleds.jpeg')
lechuga3 = Image.open('assets/lechugasiemens.jpeg')

# CIO
with st.container():
    text_column, mid, image_column = st.columns((3, 0.4, 1))
    with text_column:
        st.subheader("Estancia de investigación", divider="blue")
        st.write("*Ago – Dic 2023*")
        st.markdown("""
        - **Descripción**: Participé en una estancia de investigación, colaborando en el proyecto titulado 'Diseño y fabricación de microbobinas en implementación de sensores biomédicos'.
        - ► Aprendí procesos de microelectrónica y fabricación de capacitores, resistores y bobinas en técnicas de deposición de sustratos y semiconductores.
        - ► Tuve instrucción en modelado matemático de microbobinas en diferentes geometrías implementadas en PCBs.
        - ► Fui capacitado para ejercer funciones de técnico de laboratorio en cuarto limpio.
        - ► Adquirí habilidad para documentar con herramientas como LaTeX.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(cio, caption="Centro de Investigación en Óptica")
        st.image(cioid)

# BUSHIDO SMC
with st.container():
    text_column, mid, image_column = st.columns((3, 0.4, 1))
    with text_column:
        st.subheader("Reto BUSHIDO de SMC", divider="blue")
        st.write("*2024*")
        st.markdown("""
        - **General**: Tuve la oportunidad de participar en el reto Bushido, organizado y promocionado por SMC.
        - ► Resolución de problemas de automatización industrial.
        - ► Neumática y lógica cableada.
        - ► Electroneumática.
        - ► Programación de PLC.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(bushido, caption="SMC")
        st.image(bushteam, caption="Soy el de guinda :)")

# Agricultura vertical
with st.container():
    text_column, mid, image_column = st.columns((3, 0.4, 1))
    with text_column:
        st.subheader("Proyecto de investigación para automatización y optimización de procesos agrícolas", divider="blue")
        st.write("*Nov 2024 – Actualidad*")
        st.markdown("""
        - **Descripción**: Por iniciativa propia, recibo asesoría de un investigador de mi universidad y profesores de la escuela de agronomía. Las propuestas se enfocan en el estudio de técnicas de hidroponía vertical, especialmente (aunque hay interés en otros métodos), para su mecanización en todas las etapas de crecimiento del cultivo objetivo (actualmente, la lechuga romana). Se está trabajando en conjunto con los responsables y operadores del contenedor adquirido por la universidad de [Verde Compacto](https://www.youtube.com/watch?v=P3Bq6tVHDG4&t=9s).
        - ► Actualmente me enfoco en el diseño de un sistema de adquisición de datos.
        - ► Participo en diseños electrónicos y sistemas embebidos para el monitoreo de la calidad del agua y su dosificación óptima.
        - ► Aprendo tópicos de agricultura de precisión tanto en la práctica como en investigación.
        - ► Asisto a ferias y foros donde la agricultura de precisión es un área tratada y promovida, como la Agroferia de Irapuato o la Hannover-Messe.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(lechuga, caption="Germinado de lechugas hidropónicas")
        st.image(lechuga2, caption="Luz artificial con longitudes de onda idóneas para las hortalizas")
        st.image(lechuga3, caption="Cultivo hidropónico de lechuga hermético")

# Equipos representativos BAJA y Electratón
with st.container():
    text_column, mid, image_column = st.columns((3, 0.4, 1))
    with text_column:
        st.subheader("Equipo representativo de la UDLSB de Baja y Electratón", divider="blue")
        st.write("*Junio 2024 – Actualidad*")
        st.markdown("""
        - **General**: Actúo como miembro-asesor de apoyo en proyectos que relacionan electrónica y programación de microcontroladores para funciones de telemetría.
        - ► Colaboré en la programación de un tacómetro con un sensor de presencia inductivo.
        - ► Participé en la implementación de un velocímetro mediante un módulo de GPS utilizando el protocolo NMEA.
        - ► Apoyo con la programación de pantallas TFT para interfaces de usuario en automovilismo.
        - ► Adquiero conocimientos básicos de mecánica.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(baja0, caption="Apoyé en el sistema eléctrico")
        st.image(baja1, caption="Aprendí torneado básico")
        st.image(baja2, caption="El suministro de energía en vehículos eléctricos es interesante")

# Equipo de robótica
with st.container():
    text_column, mid, image_column = st.columns((3, 0.4, 1))
    with text_column:
        st.subheader("Equipo de robótica", divider="blue")
        st.write("*Nov 2024 – Actualidad*")
        st.markdown("""
        - **General**: Actúo como miembro y asesor en proyectos para competencia de robótica.
        - ► Trabajo en conjunto para un seguidor de línea velocista.
        - ► Asesoro a integrantes de primeros semestres y nuevos en el club para el diseño electrónico de robots sumo.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(robotica0, caption="Un diseño mío de un buck-converter")
        st.image(robotica1, caption="Una pieza que modelé")
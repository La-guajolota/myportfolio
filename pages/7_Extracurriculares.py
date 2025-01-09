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

bushsido = Image.open('assets/bushido.png')
bushteam = Image.open('assets/equipobushido.jpeg')

lechuga = Image.open('assets/lechuagerminado.jpeg')
lechuga2 = Image.open('assets/lechugaleds.jpeg')
lechuga3 = Image.open('assets/lechugasiemens.jpeg')


with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("Jefe de Relaciones Públicas e Industriales", divider="blue")
        st.write("*Abr 2023 – Presente*")
        st.markdown("""
        - ► Me uní al equipo central del Grupo de Trabajo para la Contabilidad Eficiente de Unidades Organizativas.
        - ► Este proyecto, apoyado por la Sección IEEE de Túnez, mejorará la experiencia de más de 30 ramas estudiantiles y sus subunidades.
        - ► Este proyecto de un año tiene como objetivo reestructurar el flujo de comunicación entre todas las unidades y subunidades con la sección y reducir los correos electrónicos y llamadas telefónicas innecesarios en más del 50%.
                    """)
    with mid:
        st.empty()
    with image_column:
        st.image(cio, caption="Centro de Investigación en óptica")
        st.image(cioid)

with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("Head of Sponsorship of the IEEE R8 SYP Congress", divider="blue")
        st.write("*Feb 2022 – Aug 2022*")
        st.markdown("""
        - ► Won the right to organize IEEE EMEA Region Student and Young Professional Congress in Tunisia.
        - ► Raised approximately 30,000$ from local and international sponsors to fund the congress.
        - ►  Managed the participation of 200+ attendees and guests during the 5-day Congress.
                    """)
    with mid:
        st.empty()
    with image_column:
        st.image(bushsido, caption="SMC")
        st.image(bushteam, caption="Soy el de guinda :)")

with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("General Secretary", divider="blue")
        st.write("*Sep 2021 – May 2022*")
        st.markdown("""
        - ► Scheduled and coordinated executive board meetings, ensuring efficient operation of the chapter.
        - ►  Supported the organization of 3 significant events, contributing to their successful execution.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(lechuga, caption="Germinado de lechugas hidropónicas")
        st.image(lechuga2, caption="Germinado de lechugas hidropónicas")
        st.image(lechuga3, caption="Germinado de lechugas hidropónicas")


with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("Ambassador / Project Manager", divider="blue")
        st.write("*Apr 2021 – Oct 2021*")
        st.markdown("""
        - ► This was the fifteenth edition of the international competetitive programming hackathon IEEEXtreme.
        - ► Managed a committee to organize a highly successful edition of the hackathon, attracting 160 participants.
        - ► Communicated essential information provided by regional ambassadors, facilitating effective coordination.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(baja0, caption="Germinado de lechugas hidropónicas")
        st.image(baja1, caption="Aprendí torneado básico")
        st.image(baja2, caption="Germinado de lechugas hidropónicas")

with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("Ambassador / Project Manager", divider="blue")
        st.write("*Apr 2021 – Oct 2021*")
        st.markdown("""
        - ► This was the fifteenth edition of the international competetitive programming hackathon IEEEXtreme.
        - ► Managed a committee to organize a highly successful edition of the hackathon, attracting 160 participants.
        - ► Communicated essential information provided by regional ambassadors, facilitating effective coordination.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(robotica0, caption="Germinado de lechugas hidropónicas")
        st.image(robotica1, caption="Aprendí torneado básico")
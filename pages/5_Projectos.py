import streamlit as st
from streamlit_extras.mention import mention
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.header("Proyectos y prácticas", divider="red")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Soldadura a puntos
estructura = Image.open("assets/estructura.jpeg")

# librecultivo
stand = Image.open("assets/standcultivo.jpeg")
hongo = Image.open("assets/hongo.jpeg")
elec = Image.open("assets/eleclechu.png")

#CONTROLADORES
PIDfoco = Image.open("assets/PIDfoco.jpeg")
PIDbalancin = Image.open("assets/PIDbalancin.jpeg")
CNCx = Image.open("assets/CNC.jpeg")

#PCB
tang20 = Image.open("assets/tang20k.jpeg")
tang9 = Image.open("assets/tang9k.jpeg")
controlpotencia = Image.open("assets/controlpotencia.jpeg")

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Soldador de puntos", divider="blue")
        st.write("*Electrónica industrial - asignatura - equipo*")
        st.markdown("""
            **Descripción**:
            El proyecto consistió en diseñar y construir una automatización para soldadura por puntos utilizando PLC, HMI y neumática.
            El usuario puede seleccionar un modo manual, en el cual controla el voltaje promedio que pasa por el material y la posición del pistón que sujeta el electrodo.
            En modo automático, el operador selecciona la cantidad de ciclos, los tiempos de duración de cada ciclo y el voltaje promedio durante todo el proceso.
                
            **Mis aportes**:
            Colaboré en la programación del PLC y en el diseño de una tarjeta de control para interfazar con el tablero de control.
            Esta tarjeta permite controlar el voltaje promedio que pasa por el material mediante un potenciómetro.
            La tarjeta fue implementada con un STM32f103c8t6. La misma que se encuentra en esta página.
        """)
        mention(label="Demostración de funcionamiento", icon="tiktok", url="https://vm.tiktok.com/ZMkf7bJaX/")
        mention(label="Pruebas de potencia 1", icon="tiktok", url="https://vm.tiktok.com/ZMkfvYuPP/")
        mention(label="Pruebas de potencia 2", icon="tiktok", url="https://vm.tiktok.com/ZMkfv5oLb/")

    with image_column:
        st.image(estructura, caption="Germinado de lechugas hidropónicas")

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Building a Siamese Neural Network for Face Verification", divider="blue")
        st.write("*Self-initiated project*")
        st.markdown("""
            - ► Built a Siamese network, specifically designed for comparing similarities. With twin subnetworks generating 
            embeddings and a tailored loss function, it excelled in facial recognition.
            - ► By crafting a training dataset, incorporating data augmentation, and utilizing VGGFace for feature 
            extraction, I improved the model’s accuracy. 
            - ► The Siamese architecture, coupled with a custom training loop, yielded remarkable average recall and 
            precision on the test set — 99% and 100% respectively.
            - ► Real-time testing demonstrated the model’s practical utility.
        """)
        mention(label="Playlist-documentación", icon="youtube", url="https://www.youtube.com/watch?v=h5dIs2VbnKQ&list=PLz4Si3LTpIHn8Sm7qZtzyirCftxZIDVzY&index=3")
        mention(label="Github Repo", icon="github", url="https://github.com/La-guajolota/Libre-cultivo")

    with image_column:
        st.image(stand, caption="Germinado de lechugas hidropónicas")
        st.image(hongo, caption="Aprendí torneado básico")
        st.image(elec, caption="Germinado de lechugas hidropónicas")

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Arabic Word-level Sign Language Recognition", divider="blue")
        st.write("*End of Year project*")
        st.markdown("""
            - ► Worked on the largest dataset for word-level Arabic sign language recognition, containing 502 words 
            performed by three signers. I used the 100 words subset of this dataset for experiments.
            - ► Leveraged mediapipe's holistic model to extract the hand and pose landmarks and used them to train a 
            Bidirectional LSTM model. Setting Adam optimizer, categorical_crossentropy loss and categorical_accuracy metric.
            - ► Achieved 99.6% accuracy on the test set and 0.026 loss.
            - ► Examined the generalization ability of our model, testing its performance with unseen persons and under 
            different conditions. This exploration uncovered areas for improvement, which we will focus on in the future.
        """)
        mention(label="Github Repo", icon="github", url="https://github.com/issamjebnouni/Arabic-Word-level-Sign-Language-Recognition")

    with image_column:
        st.image(PIDbalancin, caption="Germinado de lechugas hidropónicas")
        st.image(PIDfoco, caption="Aprendí torneado básico")
        st.image(CNCx, caption="Germinado de lechugas hidropónicas")

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Arabic Word-level Sign Language Recognition", divider="blue")
        st.write("*End of Year project*")
        st.markdown("""
            - ► Worked on the largest dataset for word-level Arabic sign language recognition, containing 502 words 
            performed by three signers. I used the 100 words subset of this dataset for experiments.
            - ► Leveraged mediapipe's holistic model to extract the hand and pose landmarks and used them to train a 
            Bidirectional LSTM model. Setting Adam optimizer, categorical_crossentropy loss and categorical_accuracy metric.
            - ► Achieved 99.6% accuracy on the test set and 0.026 loss.
            - ► Examined the generalization ability of our model, testing its performance with unseen persons and under 
            different conditions. This exploration uncovered areas for improvement, which we will focus on in the future.
        """)
        mention(label="Github Repo", icon="github", url="https://github.com/issamjebnouni/Arabic-Word-level-Sign-Language-Recognition")

    with image_column:
        st.image(tang9, caption="Germinado de lechugas hidropónicas")
        st.image(tang20, caption="Aprendí torneado básico")
        st.image(controlpotencia, caption="Control de carga promedia AC")
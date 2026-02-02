import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

# --- CSS: cargamos tu CSS y luego sobreescribimos con estilos de tarjetas ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

custom_css = """
<style>
/* Tarjeta limpia y legible sobre fondo oscuro */
.card {
  background: #ffffff;
  padding: 18px 18px 14px;
  border-radius: 14px;
  box-shadow: 0 6px 20px rgba(0,0,0,.18);
  margin-bottom: 18px;
  border: 1px solid rgba(0,0,0,.05);
}

/* Asegura CONTRASTE dentro de la tarjeta, por encima de estilos globales */
.card, .card * {
  color: #1f2937 !important;         /* gris muy oscuro */
  line-height: 1.45;
}

/* Título de cada bloque */
.card h4 {
  margin: 0 0 6px 0;
  font-size: 1.15rem;
  font-weight: 800;
}

/* Fecha en cursiva, más tenue (pero legible) */
.card p {
  margin: 0 0 8px 0;
  opacity: .9;
  font-style: italic;
}

/* Lista con separación */
.card ul { margin: 0 0 0 18px; padding: 0; }
.card li { margin: 6px 0; }

/* Imágenes redondeadas y con sombra */
img {
  border-radius: 12px;
  box-shadow: 0 4px 14px rgba(0,0,0,.22);
  margin-bottom: 12px;
}

/* Título principal */
.section-title {
  text-align: center;
  font-weight: 800;
  margin-bottom: 0;
}
.section-rule {
  border: 2px solid #e63946;
  margin-top: 6px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<h2 class='section-title'>🚀 Extracurricular Activities</h2>", unsafe_allow_html=True)
st.markdown("<hr class='section-rule'>", unsafe_allow_html=True)

# --- Imágenes ---
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

# =========================
# CIO
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#007acc;">🔬 Research Internship</h4>
          <p>Aug – Dec 2023</p>
          <ul>
            <li><b>Description:</b> Project "Design and fabrication of microcoils for biomedical sensors".</li>
            <li><b>Microelectronics</b> processes and semiconductor deposition.</li>
            <li>Mathematical modeling of microcoils on PCBs.</li>
            <li>Cleanroom training and certification.</li>
            <li>Technical documentation with <b>LaTeX</b>.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(cio, caption="Center for Optical Research (CIO)", use_container_width=True)
        st.image(cioid, use_container_width=True)

# =========================
# BUSHIDO SMC
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#f77f00;">⚙️ SMC BUSHIDO Challenge</h4>
          <p>2024</p>
          <ul>
            <li><b>Overview:</b> Participated in industrial automation challenge.</li>
            <li>Problem-solving in <b>pneumatics</b> and <b>electropneumatics</b>.</li>
            <li>Hardwired logic and <b>PLC programming</b>.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(bushido, caption="SMC", use_container_width=True)
        st.image(bushteam, caption="I'm the one in burgundy :)", use_container_width=True)

# =========================
# AGRICULTURA VERTICAL
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#2a9d8f;">🌱 Vertical Farming & Research</h4>
          <p>Nov 2024 – Present</p>
          <ul>
            <li><b>Description:</b> Research on vertical hydroponics techniques with university advisory.</li>
            <li>Design of data acquisition systems.</li>
            <li>Electronics and embedded systems for <b>water monitoring</b> and dosing.</li>
            <li>Hands-on experience in <b>precision agriculture</b>.</li>
            <li>Attended industry forums (Agroferia Irapuato, Hannover Messe).</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(lechuga, caption="Lettuce germination", use_container_width=True)
        st.image(lechuga2, caption="Optimal artificial lighting", use_container_width=True)
        st.image(lechuga3, caption="Sealed hydroponic cultivation", use_container_width=True)

# =========================
# BAJA / ELECTRATÓN
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#e63946;">🏎️ Baja SAE & Electrathon Team</h4>
          <p>June 2024 – Present</p>
          <ul>
            <li><b>Role:</b> Member-advisor in electronics and microcontroller programming.</li>
            <li>Tachometer programming with inductive sensor.</li>
            <li>Speedometer implementation using GPS (NMEA protocol).</li>
            <li>TFT displays for automotive user interfaces.</li>
            <li>Basic mechanical knowledge.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(baja0, caption="Assisted with the electrical system", use_container_width=True)
        st.image(baja1, caption="Learned basic lathe operation", use_container_width=True)
        st.image(baja2, caption="Energy systems in electric vehicles", use_container_width=True)

# =========================
# ROBÓTICA
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#9b5de5;">🤖 Robotics Team</h4>
          <p>Nov 2024 – Present</p>
          <ul>
            <li><b>Overview:</b> Advisor and member in competitive robotics projects.</li>
            <li>Development of high-speed line follower robot.</li>
            <li>Mentoring new members in sumo robot electronic design.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(robotica0, caption="Buck converter design", use_container_width=True)
        st.image(robotica1, caption="3D modeled component", use_container_width=True)

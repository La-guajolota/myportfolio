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
st.markdown("<h2 class='section-title'>🚀 Actividades Extracurriculares</h2>", unsafe_allow_html=True)
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
          <h4 style="color:#007acc;">🔬 Estancia de investigación</h4>
          <p>Ago – Dic 2023</p>
          <ul>
            <li><b>Descripción:</b> Proyecto “Diseño y fabricación de microbobinas en sensores biomédicos”.</li>
            <li>Procesos de <b>microelectrónica</b> y deposición de semiconductores.</li>
            <li>Modelado matemático de microbobinas en PCBs.</li>
            <li>Capacitación en cuarto limpio.</li>
            <li>Documentación técnica con <b>LaTeX</b>.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(cio, caption="Centro de Investigación en Óptica", use_container_width=True)
        st.image(cioid, use_container_width=True)

# =========================
# BUSHIDO SMC
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#f77f00;">⚙️ Reto BUSHIDO de SMC</h4>
          <p>2024</p>
          <ul>
            <li><b>General:</b> Participación en reto de automatización industrial.</li>
            <li>Resolución de problemas de <b>neumática</b> y <b>electroneumática</b>.</li>
            <li>Lógica cableada y <b>programación de PLC</b>.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(bushido, caption="SMC", use_container_width=True)
        st.image(bushteam, caption="Soy el de guinda :)", use_container_width=True)

# =========================
# AGRICULTURA VERTICAL
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#2a9d8f;">🌱 Agricultura vertical e investigación</h4>
          <p>Nov 2024 – Actualidad</p>
          <ul>
            <li><b>Descripción:</b> Investigación en técnicas de hidroponía vertical con asesoría universitaria.</li>
            <li>Diseño de sistemas de adquisición de datos.</li>
            <li>Electrónica y sistemas embebidos para <b>monitoreo de agua</b> y dosificación.</li>
            <li>Práctica en <b>agricultura de precisión</b>.</li>
            <li>Asistencia a foros (Agroferia Irapuato, Hannover-Messe).</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(lechuga, caption="Germinado de lechugas", use_container_width=True)
        st.image(lechuga2, caption="Luz artificial óptima", use_container_width=True)
        st.image(lechuga3, caption="Cultivo hidropónico hermético", use_container_width=True)

# =========================
# BAJA / ELECTRATÓN
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#e63946;">🏎️ Equipo representativo Baja y Electratón</h4>
          <p>Junio 2024 – Actualidad</p>
          <ul>
            <li><b>Rol:</b> Miembro-asesor en electrónica y programación de microcontroladores.</li>
            <li>Programación de tacómetro con sensor inductivo.</li>
            <li>Implementación de velocímetro con GPS (NMEA).</li>
            <li>Pantallas TFT para interfaces de usuario en automovilismo.</li>
            <li>Conocimientos básicos de mecánica.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(baja0, caption="Apoyé en el sistema eléctrico", use_container_width=True)
        st.image(baja1, caption="Aprendí torneado básico", use_container_width=True)
        st.image(baja2, caption="Energía en vehículos eléctricos", use_container_width=True)

# =========================
# ROBÓTICA
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card">
          <h4 style="color:#9b5de5;">🤖 Equipo de robótica</h4>
          <p>Nov 2024 – Actualidad</p>
          <ul>
            <li><b>General:</b> Asesor y miembro en proyectos de competencia de robótica.</li>
            <li>Desarrollo de seguidor de línea velocista.</li>
            <li>Asesoría a nuevos integrantes en diseño electrónico de robots sumo.</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(robotica0, caption="Diseño de buck-converter", use_container_width=True)
        st.image(robotica1, caption="Pieza modelada en 3D", use_container_width=True)

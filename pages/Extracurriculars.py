import streamlit as st
from PIL import Image
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import add_footer

st.set_page_config(layout="wide", page_title="Extracurriculars | Adrián Silva Palafox")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

custom_css = """
<style>
.card {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  padding: 20px;
  border-radius: 14px;
  box-shadow: 0 6px 20px rgba(0,0,0,.18);
  margin-bottom: 18px;
  border-left: 4px solid;
}
.card h4 { margin: 0 0 8px 0; font-size: 1.2rem; font-weight: 700; }
.card p { margin: 0 0 10px 0; opacity: .8; font-style: italic; }
.card ul { margin: 0 0 0 18px; padding: 0; }
.card li { margin: 8px 0; }
.skill-gained {
  background: rgba(230, 57, 70, 0.1);
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.8em;
  display: inline-block;
  margin: 2px;
}
img { border-radius: 12px; box-shadow: 0 4px 14px rgba(0,0,0,.22); margin-bottom: 12px; }
.section-title { text-align: center; font-weight: 800; margin-bottom: 0; }
.section-rule { border: 2px solid #e63946; margin-top: 6px; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>🚀 Extracurricular Activities</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>Hands-on experience beyond the classroom</p>", unsafe_allow_html=True)
st.markdown("<hr class='section-rule'>", unsafe_allow_html=True)

# --- Images ---
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
# CIO RESEARCH
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card" style="border-color: #007acc;">
          <h4 style="color:#007acc;">🔬 Research Internship @ CIO</h4>
          <p>📅 August – December 2023 | Centro de Investigación en Óptica</p>
          <ul>
            <li><b>Project:</b> "Design and fabrication of microcoils for biomedical sensors"</li>
            <li>Microelectronics processes and semiconductor deposition</li>
            <li>Mathematical modeling of microcoils on PCBs</li>
            <li>ISO Class 5 cleanroom certification</li>
            <li>Technical documentation with LaTeX</li>
          </ul>
          <p style="margin-top: 12px; font-style: normal;"><b>Skills Gained:</b></p>
          <span class='skill-gained'>COMSOL Multiphysics</span>
          <span class='skill-gained'>Microfabrication</span>
          <span class='skill-gained'>LaTeX</span>
          <span class='skill-gained'>Research Methods</span>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(cio, caption="CIO - Center for Optical Research", use_container_width=True)
        st.image(cioid, use_container_width=True)

# =========================
# BUSHIDO SMC
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card" style="border-color: #f77f00;">
          <h4 style="color:#f77f00;">⚙️ SMC BUSHIDO Challenge</h4>
          <p>📅 September 2023 | Industrial Automation Competition</p>
          <ul>
            <li><b>Overview:</b> National industrial automation challenge</li>
            <li>Problem-solving in pneumatics and electropneumatics</li>
            <li>Hardwired logic design and implementation</li>
            <li>PLC programming under time constraints</li>
          </ul>
          <p style="margin-top: 12px; font-style: normal;"><b>Skills Gained:</b></p>
          <span class='skill-gained'>PLC Programming</span>
          <span class='skill-gained'>Pneumatics</span>
          <span class='skill-gained'>Problem Solving</span>
          <span class='skill-gained'>Teamwork</span>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(bushido, caption="SMC Corporation", use_container_width=True)
        st.image(bushteam, caption="I'm the one in burgundy :)", use_container_width=True)

# =========================
# VERTICAL FARMING
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card" style="border-color: #2a9d8f;">
          <h4 style="color:#2a9d8f;">🌱 Vertical Farming Research</h4>
          <p>📅 November 2024 – Present | Precision Agriculture</p>
          <ul>
            <li><b>Description:</b> Personal research on vertical hydroponics with university advisory</li>
            <li>Design of IoT data acquisition systems</li>
            <li>Embedded systems for water monitoring and dosing</li>
            <li>Attended: Agroferia Irapuato, Hannover Messe</li>
          </ul>
          <p style="margin-top: 12px; font-style: normal;"><b>Skills Gained:</b></p>
          <span class='skill-gained'>IoT</span>
          <span class='skill-gained'>Sensor Networks</span>
          <span class='skill-gained'>MQTT</span>
          <span class='skill-gained'>Data Analysis</span>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(lechuga, caption="Lettuce germination", use_container_width=True)
        st.image(lechuga2, caption="Optimal artificial lighting", use_container_width=True)
        st.image(lechuga3, caption="Sealed hydroponic cultivation", use_container_width=True)

# =========================
# BAJA SAE
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card" style="border-color: #e63946;">
          <h4 style="color:#e63946;">🏎️ Baja SAE & Electrathon Team</h4>
          <p>📅 June 2024 – Present | University Representative Team</p>
          <ul>
            <li><b>Role:</b> Electronics advisor and microcontroller programmer</li>
            <li>Tachometer with inductive sensor implementation</li>
            <li>GPS speedometer using NMEA protocol</li>
            <li>TFT displays for driver interfaces</li>
            <li>Basic mechanical skills (lathe operation)</li>
          </ul>
          <p style="margin-top: 12px; font-style: normal;"><b>Skills Gained:</b></p>
          <span class='skill-gained'>Automotive Electronics</span>
          <span class='skill-gained'>GPS/NMEA</span>
          <span class='skill-gained'>TFT Displays</span>
          <span class='skill-gained'>Mechanical Basics</span>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(baja0, caption="Electrical system work", use_container_width=True)
        st.image(baja1, caption="Lathe operation training", use_container_width=True)
        st.image(baja2, caption="Electric vehicle energy systems", use_container_width=True)

# =========================
# ROBOTICS
# =========================
with st.container():
    text_column, _, image_column = st.columns((3, 0.25, 1))
    with text_column:
        st.markdown("""
        <div class="card" style="border-color: #9b5de5;">
          <h4 style="color:#9b5de5;">🤖 Competitive Robotics Team</h4>
          <p>📅 November 2024 – Present | University Representative Team</p>
          <ul>
            <li><b>Role:</b> Technical advisor and team member</li>
            <li>Development of high-speed line follower robots</li>
            <li>Mentoring new members in sumo robot design</li>
            <li>Power electronics and motor control</li>
          </ul>
          <p style="margin-top: 12px; font-style: normal;"><b>Skills Gained:</b></p>
          <span class='skill-gained'>Motor Control</span>
          <span class='skill-gained'>PCB Design</span>
          <span class='skill-gained'>Mentoring</span>
          <span class='skill-gained'>Competition Strategy</span>
        </div>
        """, unsafe_allow_html=True)
    with image_column:
        st.image(robotica0, caption="Buck converter design", use_container_width=True)
        st.image(robotica1, caption="3D modeled component", use_container_width=True)

# --- Summary Section ---
st.markdown("---")
st.subheader("📊 Activities Summary")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Research", "1 Internship", "CIO")
with col2:
    st.metric("Competitions", "2+", "SMC, Robotics")
with col3:
    st.metric("Teams", "3 Active", "Baja, Robotics, Rover")
with col4:
    st.metric("Personal Projects", "5+", "Ongoing")

# --- Footer ---
add_footer()

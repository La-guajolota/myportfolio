import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.header("Educación", divider="red")

insat = Image.open("assets/sallelogo.png")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "education.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with st.container():

    image_column, text_column = st.columns((1,2.5))
    with image_column:
        st.image(insat, width=200, caption="Universidad la Salle Bajío")

    with text_column:
        st.write("### Master of Science, [_INSAT_](https://insat.rnu.tn) (2019-2024)")
        st.write("##### Major: Computer Science")
        st.write("##### Minor: Image and Video Processing")
        st.write("**Relevant Coursework:** Machine learning, Deep Learning, Image and Video Processing, Big Data, Business Intelligence, Linux....")

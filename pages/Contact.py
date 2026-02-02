import streamlit as st
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import add_footer

st.set_page_config(page_title="Contact | Adrián Silva Palafox", page_icon="📬", layout="centered")

st.title("📬 Get In Touch")
st.markdown("""
I'm always excited to discuss new opportunities, collaborations, or just chat about embedded systems and IoT!
""")

st.divider()

# Contact Info
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📧 Email")
    st.markdown("**adriansilpa@gmail.com**")
    st.markdown("### 📱 Phone")
    st.markdown("**+52 477 264 1384**")

with col2:
    st.markdown("### 🔗 LinkedIn")
    st.markdown("[Connect with me](https://www.linkedin.com/in/adrian-silva-palafox/)")
    st.markdown("### 💻 GitHub")
    st.markdown("[View my code](https://github.com/La-guajolota)")

st.divider()

# Contact Form
st.markdown("### 💬 Send a Message")
st.caption("Fill out the form and I'll get back to you as soon as possible!")

with st.form("contact_form"):
    name = st.text_input("Your Name *")
    email = st.text_input("Your Email *")
    subject = st.selectbox("Subject", [
        "Job Opportunity",
        "Project Collaboration",
        "Freelance Work",
        "Technical Question",
        "Other"
    ])
    message = st.text_area("Your Message *", height=150)
    
    submitted = st.form_submit_button("Send Message 🚀")
    
    if submitted:
        if name and email and message:
            st.success("✅ Thank you for your message! I'll respond within 24-48 hours.")
            # Note: To actually send emails, you'd need to integrate with an email service
        else:
            st.error("Please fill in all required fields.")

st.divider()
st.markdown("### 📍 Location")
st.markdown("Based in **León, Guanajuato, Mexico** 🇲🇽")
st.markdown("Open to **remote work** and **relocation** opportunities.")

# --- Footer ---
add_footer()

#import streamlit as st;
#st.title("Welcome to My Website")
#st.header("About Me")
#st.write("Hi, I'm Pranay Dev, a B. Tech student at IIT Patna. I love building cool projects and learning new things.")
import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Pranay Dev | Portfolio", page_icon=":wave:", layout="centered")

# --- PROFILE SECTION ---
st.image("https://images.app.goo.gl/wpaYFnTiMtE52cJMA.jpg", width=200, caption="Pranay Dev")
  # You can change this to your own image URL
st.title("Pranay Dev")
st.subheader("B.Tech Student | Developer | Creator")
st.write("Hi! I'm a first-year B.Tech student at IIT Patna with a passion for tech, startups, and creative problem-solving.")

# --- PROJECTS SECTION ---
st.markdown("## Projects")
st.markdown("### 1. **IIT Patna Chatbot**")
st.write("A Streamlit-based chatbot that answers FAQs about IIT Patna using Python and AI tools.")

st.markdown("### 2. **Batata Puri Stall App**")
st.write("An app to manage orders and promote my food stall during college fests.")

st.markdown("### 3. **Facebook Content Monetization**")
st.write("Created an anonymous content page to earn via Facebook monetization.")

# --- SKILLS SECTION ---
st.markdown("## Skills")
st.write("""
- Python & Streamlit
- C Programming & DSA
- Content Creation
- Teaching (NSS Volunteer)
- Entrepreneurship Mindset
""")

# --- CONTACT SECTION ---
st.markdown("## Contact Me")
st.write("- Email: your_email@example.com")
st.write("- GitHub: [github.com/pranaydev](https://github.com/pranaydev)")
st.write("- Instagram: [@pranay_dev](https://instagram.com/pranay_dev)")
st.write("- LinkedIn: [Your LinkedIn URL]")

# --- FOOTER ---
st.markdown("---")
st.write("© 2025 Pranay Dev | Built with Streamlit")

with open("resume.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 Download My Resume",
        data=file,
        file_name="Pranay_Resume.pdf",
        mime="application/pdf"
    )

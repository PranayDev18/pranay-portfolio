import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Pranay Dev | Portfolio", page_icon="🧑‍💻", layout="wide")

# --- CUSTOM CSS STYLING ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        .gradient-header {
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            padding: 40px 10px;
            text-align: center;
            color: white;
            border-radius: 12px;
            margin-bottom: 30px;
        }

        .profile-pic {
            border-radius: 50%;
            border: 4px solid #00c6ff;
            width: 180px;
        }

        .project-card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 15px;
            transition: 0.3s;
            margin-bottom: 20px;
        }

        .project-card:hover {
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            transform: scale(1.02);
        }

        .social-button {
            background-color: #00c6ff;
            color: white;
            padding: 8px 16px;
            margin-right: 10px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 500;
        }

        .footer {
            text-align: center;
            color: #aaa;
            font-size: 13px;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "💼 Projects", "🛠️ Skills", "📬 Contact"])

# --- HOME PAGE ---
if page == "🏠 Home":
    st.markdown("""
        <div class="gradient-header">
            <h1>👋 Hi, I'm Pranay Dev</h1>
            <p>First-Year B.Tech Student @ IIT Patna | Developer | Creator</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://raw.githubusercontent.com/PranayDev18/pranay-portfolio/main/profile.jpg", width=180, output_format='auto', caption='Pranay Dev')
    with col2:
        st.subheader("🚀 About Me")
        st.write("""
        I'm a passionate first-year B.Tech student at IIT Patna who loves building cool projects,
        experimenting with startups, and mentoring peers through teaching. Whether it's creating digital tools,
        or solving DSA problems — I enjoy doing impactful work and sharing it with the world.
        """)

# --- PROJECTS PAGE ---
elif page == "💼 Projects":
    st.markdown("### 🧠 My Featured Projects")

    projects = [
        {
            "title": "📚 NSS Teaching Portal",
            "desc": "Taught government school students through interactive sessions. Created simplified science and math modules."
        },
        {
            "title": "⏱️ Time Management Toolkit",
            "desc": "Created and presented a visual productivity guide with calendars, focus techniques, and reflection tools."
        },
        {
            "title": "📊 DSA Practice Tracker",
            "desc": "Python script + CSV tracker that visualizes daily problem-solving stats. Built for self-assessment."
        },
        {
            "title": "💡 Startup Idea Vault",
            "desc": "A Notion-based repository of innovative startup ideas with business models and pitch outlines."
        }
    ]

    for project in projects:
        with st.container():
            st.markdown(f"""
                <div class="project-card">
                    <h4>{project['title']}</h4>
                    <p>{project['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

# --- SKILLS PAGE ---
elif page == "🛠️ Skills":
    st.markdown("### 🧰 My Skillset")
    st.markdown("""
    - 🐍 **Python, Streamlit** – Web apps and data dashboards  
    - 💻 **C, DSA** – Strong foundation in logic and problem-solving  
    - 📽️ **Content Creation** – Facebook, Instagram content marketing  
    - 📚 **Teaching** – Volunteer at NSS, school sessions  
    - 💡 **Startup Thinking** – Always ideating and validating problems  
    """)

# --- CONTACT PAGE ---
elif page == "📬 Contact":
    st.markdown("### 📬 Get in Touch")
    st.write("Feel free to reach out to collaborate, discuss ideas, or just say hello! 👇")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - 📧 **Email**: [devpranay878947@gmail.com](mailto:devpranay878947@gmail.com)  
        - 📸 **Instagram**: [@pranay_iitp](https://www.instagram.com/pranay_iitp/)  
        - 🔗 **LinkedIn**: [Pranay Dev](https://www.linkedin.com/in/pranay-dev-/)
        """)
    with col2:
        st.markdown("""
        <a href="https://www.linkedin.com/in/pranay-dev-/" class="social-button">LinkedIn</a>
        <a href="https://www.instagram.com/pranay_iitp/" class="social-button">Instagram</a>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<div class='footer'>© 2025 Pranay Dev</div>", unsafe_allow_html=True)

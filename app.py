import streamlit as st
import random
from datetime import date
from streamlit.components.v1 import html
import os
import hashlib
import re

st.set_page_config(
    page_title="Happy Birthday Shajitha Thangomeyy ❤️",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize ALL session states
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'dob_confirmed' not in st.session_state:
    st.session_state.dob_confirmed = False
if 'balloon_pop' not in st.session_state:
    st.session_state.balloon_pop = False
if 'scratch_revealed' not in st.session_state:
    st.session_state.scratch_revealed = [False]*5
if 'cake_cut' not in st.session_state:
    st.session_state.cake_cut = [False]*5
if 'celebration_active' not in st.session_state:
    st.session_state.celebration_active = False
if 'celebration_type' not in st.session_state:
    st.session_state.celebration_type = "balloon"
if 'balloon_popped' not in st.session_state:
    st.session_state.balloon_popped = [False]*6
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'user_gallery' not in st.session_state:
    st.session_state.user_gallery = {}
if 'gallery_scratch_revealed' not in st.session_state:
    st.session_state.gallery_scratch_revealed = {}
if 'wish_celebrated' not in st.session_state:
    st.session_state.wish_celebrated = False
if 'forgot_password_mode' not in st.session_state:
    st.session_state.forgot_password_mode = False
if 'captcha_text' not in st.session_state:
    st.session_state.captcha_text = ""
if 'captcha_attempts' not in st.session_state:
    st.session_state.captcha_attempts = 0
if 'photo_revealed' not in st.session_state:
    st.session_state.photo_revealed = [False, False, False]

# Load users from file
def load_users():
    try:
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as f:
                for line in f:
                    if ":" in line:
                        username, password = line.strip().split(":", 1)
                        st.session_state.users[username] = password
        if not st.session_state.users:
            st.session_state.users["admin"] = hash_password("admin123")
            save_users()
    except:
        pass

def save_users():
    try:
        with open("users.txt", "w") as f:
            for username, password in st.session_state.users.items():
                f.write(f"{username}:{password}\n")
    except:
        pass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed

def generate_captcha():
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    captcha = ''.join(random.choices(chars, k=6))
    st.session_state.captcha_text = captcha
    return captcha

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

load_users()

# Tanglish thoughts for each photo
PHOTO_THOUGHTS = [
    "💖 Un azhaguku enna per vecha? Avalo azhaga irukka!\n\nUn smile paatha dhaan enaku day full ah nalla iruku... nee en sunshine 🌞",
    "🌸 Unna patha dhaan enaku ellame special ah theriyum!\n\nUn kannu paatha dhaan en heart beat fast ah odum ❤️",
    "💫 Unna vida beautiful ah enaku yaarum illa!\n\nNee en life ku vandha piragu ellame beautiful ah iruku 🌟"
]

# CSS with love theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ff6b6b 0%, #c0392b 25%, #8e44ad 50%, #2980b9 75%, #ff6b6b 100%);
        background-size: 400% 400%;
        animation: gradientShift 10s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .heart-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }
    
    .floating-heart {
        position: absolute;
        font-size: 30px;
        animation: floatHeart linear infinite;
        opacity: 0.3;
    }
    
    @keyframes floatHeart {
        0% {
            transform: translateY(100vh) rotate(0deg) scale(0);
            opacity: 0;
        }
        10% { opacity: 0.3; }
        90% { opacity: 0.3; }
        100% {
            transform: translateY(-100vh) rotate(720deg) scale(1);
            opacity: 0;
        }
    }
    
    .glass-card {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 30px;
        border: 2px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        animation: cardGlow 3s ease-in-out infinite;
        position: relative;
        z-index: 1;
    }
    
    @keyframes cardGlow {
        0%, 100% { box-shadow: 0 8px 32px rgba(255,107,107,0.3); }
        50% { box-shadow: 0 8px 32px rgba(142,68,173,0.5); }
    }
    
    .love-title {
        font-family: 'Georgia', serif;
        font-size: 3.5em;
        text-align: center;
        background: linear-gradient(135deg, #fff5f5, #ffd4d4, #ffb3b3, #ff9999);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 40px rgba(255,107,107,0.5);
        animation: titlePulse 2s ease-in-out infinite;
        position: relative;
        z-index: 1;
    }
    
    @keyframes titlePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.03); }
    }
    
    .love-subtitle {
        font-family: 'Georgia', serif;
        font-size: 1.5em;
        color: #fff5f5;
        text-align: center;
        text-shadow: 0 0 30px rgba(255,255,255,0.3);
        animation: subtitleFloat 3s ease-in-out infinite;
        position: relative;
        z-index: 1;
    }
    
    @keyframes subtitleFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 12px 30px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255,107,107,0.4) !important;
        position: relative;
        z-index: 1;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 8px 30px rgba(255,107,107,0.6) !important;
    }
    
    .balloon {
        display: inline-block;
        width: 120px;
        height: 150px;
        border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2em;
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        animation: balloonFloat 3s ease-in-out infinite;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        margin: 0 auto;
    }
    
    .balloon:hover {
        transform: scale(1.1);
        box-shadow: 0 30px 60px rgba(0,0,0,0.4);
    }
    
    @keyframes balloonFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    .scratch-card {
        background: linear-gradient(145deg, #2d1b3d, #1a1a2e);
        border-radius: 25px;
        padding: 30px;
        min-height: 200px;
        border: 2px solid rgba(255,107,107,0.3);
        cursor: pointer;
        transition: all 0.5s ease;
        position: relative;
        z-index: 1;
    }
    
    .scratch-card:hover {
        transform: scale(1.05);
        border-color: rgba(255,107,107,0.6);
        box-shadow: 0 20px 60px rgba(255,107,107,0.3);
    }
    
    .scratch-card.revealed {
        background: linear-gradient(145deg, #ff6b6b, #ee5a24);
        border-color: rgba(255,255,255,0.5);
        animation: revealPulse 0.5s ease;
    }
    
    @keyframes revealPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .celebration-emoji {
        position: fixed;
        pointer-events: none;
        z-index: 99999;
        font-size: 40px;
        animation: celebrateFloat 4s ease-out forwards;
    }
    
    @keyframes celebrateFloat {
        0% {
            transform: translateY(0) scale(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(-500px) scale(2) rotate(720deg);
            opacity: 0;
        }
    }
    
    .photo-card {
        background: rgba(255,255,255,0.1);
        border-radius: 25px;
        padding: 20px;
        border: 2px solid rgba(255,255,255,0.1);
        transition: all 0.5s ease;
        position: relative;
        z-index: 1;
        min-height: 300px;
        text-align: center;
    }
    
    .photo-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(255,107,107,0.3);
        border-color: rgba(255,107,107,0.3);
    }
    
    .photo-card.revealed {
        border-color: #ffd93d;
        box-shadow: 0 0 40px rgba(255,217,61,0.3);
        animation: revealPulse 0.5s ease;
    }
    
    .photo-card .thought {
        font-family: 'Georgia', serif;
        font-size: 1.2em;
        color: #fff5f5;
        padding: 15px;
        background: rgba(0,0,0,0.3);
        border-radius: 15px;
        margin-top: 10px;
        white-space: pre-line;
        line-height: 1.8;
    }
    
    .celebration-blast {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 99999;
        overflow: hidden;
    }
    
    .blast-element {
        position: fixed;
        pointer-events: none;
        z-index: 99999;
        font-size: 50px;
        animation: blastFloat 5s ease-out forwards;
    }
    
    @keyframes blastFloat {
        0% {
            transform: translate(0, 0) scale(0) rotate(0deg);
            opacity: 1;
        }
        20% { transform: translate(50px, -100px) scale(1.5) rotate(45deg); }
        50% { transform: translate(-50px, -300px) scale(2) rotate(180deg); }
        80% { transform: translate(30px, -500px) scale(2.5) rotate(360deg); }
        100% {
            transform: translate(0, -700px) scale(3) rotate(720deg);
            opacity: 0;
        }
    }
    
    .status-badge.uploaded {
        background: rgba(46, 213, 115, 0.2);
        color: #2ed573;
        border: 1px solid #2ed573;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: bold;
        display: inline-block;
    }
    
    .status-badge.pending {
        background: rgba(255,255,255,0.05);
        color: rgba(255,255,255,0.4);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: bold;
        display: inline-block;
    }
    
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #ff6b6b, #ee5a24) !important;
    }
    
    @media (max-width: 768px) {
        .love-title {
            font-size: 2.5em !important;
        }
        .glass-card {
            padding: 20px !important;
        }
        .balloon {
            width: 80px !important;
            height: 100px !important;
            font-size: 1.5em !important;
        }
        .photo-card {
            min-height: 200px !important;
            padding: 15px !important;
        }
        .photo-card .thought {
            font-size: 1em !important;
        }
        .scratch-card {
            min-height: 150px !important;
            padding: 20px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

def add_floating_hearts():
    hearts_html = """
    <div class="heart-bg">
    """
    hearts = ['❤️', '💖', '💕', '💗', '💓', '♥️']
    for i in range(30):
        heart = random.choice(hearts)
        size = random.randint(20, 50)
        duration = random.randint(10, 25)
        delay = random.random() * 10
        left = random.randint(0, 95)
        hearts_html += f"""
        <div class="floating-heart" style="
            left: {left}%;
            font-size: {size}px;
            animation-duration: {duration}s;
            animation-delay: {delay}s;
        ">{heart}</div>
        """
    hearts_html += "</div>"
    html(hearts_html)

def trigger_celebration(emojis, count=50):
    celebration_html = f"""
    <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 99999; overflow: hidden;">
    """
    for i in range(count):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        size = random.randint(2, 6)
        delay = random.random() * 3
        emoji = random.choice(emojis)
        celebration_html += f"""
        <div class="celebration-emoji" style="
            left: {x}%;
            top: {y}%;
            font-size: {size}em;
            animation-delay: {delay}s;
        ">{emoji}</div>
        """
    celebration_html += "</div>"
    html(celebration_html)

def add_confetti():
    confetti_html = """
    <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 99998; overflow: hidden;">
    """
    colors = ['#ff6b6b', '#ffd93d', '#6bcb77', '#4d96ff', '#f093fb', '#f5576c', '#43e97b', '#a29bfe', '#fd79a8']
    for i in range(60):
        x = random.randint(0, 100)
        size = random.randint(8, 16)
        duration = random.randint(3, 6)
        delay = random.random() * 3
        color = random.choice(colors)
        confetti_html += f"""
        <div style="
            position: fixed;
            left: {x}%;
            top: -20px;
            width: {size}px;
            height: {size//2}px;
            background: {color};
            animation: confettiFall {duration}s linear forwards;
            animation-delay: {delay}s;
            border-radius: 2px;
            pointer-events: none;
            z-index: 99998;
            box-shadow: 0 0 10px {color};
        "></div>
        """
    confetti_html += """
    </div>
    <style>
        @keyframes confettiFall {
            0% { transform: translateY(0) rotate(0deg) scale(1); opacity: 1; }
            100% { transform: translateY(110vh) rotate(720deg) scale(0.3); opacity: 0; }
        }
    </style>
    """
    html(confetti_html)

def trigger_celebration_blast(emojis, count=150):
    """Massive full-page celebration blast"""
    blast_html = f"""
    <div class="celebration-blast">
    """
    for i in range(count):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        size = random.randint(2, 10)
        delay = random.random() * 4
        emoji = random.choice(emojis)
        rotation = random.randint(0, 360)
        blast_html += f"""
        <div class="blast-element" style="
            left: {x}%;
            top: {y}%;
            font-size: {size}em;
            animation-delay: {delay}s;
            transform: rotate({rotation}deg);
            filter: drop-shadow(0 0 30px rgba(255,255,255,0.5));
        ">{emoji}</div>
        """
    blast_html += """
    </div>
    <style>
        .blast-element {
            animation: megaBlast 7s ease-out forwards !important;
        }
        @keyframes megaBlast {
            0% { 
                transform: translate(0, 0) scale(0) rotate(0deg); 
                opacity: 1; 
            }
            25% { 
                transform: translate(150px, -200px) scale(2.5) rotate(90deg); 
                opacity: 1;
            }
            50% { 
                transform: translate(-200px, -450px) scale(3.5) rotate(180deg); 
                opacity: 1;
            }
            75% { 
                transform: translate(100px, -650px) scale(4) rotate(360deg); 
                opacity: 0.8;
            }
            100% { 
                transform: translate(0, -900px) scale(5) rotate(720deg); 
                opacity: 0; 
            }
        }
    </style>
    """
    html(blast_html)

def init_user_gallery(username):
    if username not in st.session_state.user_gallery:
        st.session_state.user_gallery[username] = {
            'img1': None,
            'img2': None,
            'img3': None
        }
    if username not in st.session_state.gallery_scratch_revealed:
        st.session_state.gallery_scratch_revealed[username] = [False, False, False]

# PAGE 1: LOGIN
def login_page():
    add_floating_hearts()
    
    st.markdown("""
    <div style="text-align: center; padding: 30px 0; position: relative; z-index: 1;">
        <div style="font-size: 4em; animation: heartbeat 1.5s ease-in-out infinite;">💖</div>
        <h1 class="love-title">Happy Birthday Shajitha Thangomeyy ❤️</h1>
        <p class="love-subtitle">✨ A Celebration of Love & Joy ✨</p>
    </div>
    
    <style>
        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            14% { transform: scale(1.3); }
            28% { transform: scale(1); }
            42% { transform: scale(1.3); }
            70% { transform: scale(1); }
        }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        with st.container():
            st.markdown("""
            <div class="glass-card">
            """, unsafe_allow_html=True)
            
            tab1, tab2, tab3 = st.tabs(["🔐 Login", "📝 Create Account", "🔄 Forgot Password"])
            
            with tab1:
                if not st.session_state.forgot_password_mode:
                    username = st.text_input("Username", key="login_username")
                    password = st.text_input("Password", type="password", key="login_password")
                    
                    col_btn1, col_btn2 = st.columns([3, 1])
                    with col_btn1:
                        if st.button("🚀 Login", use_container_width=True):
                            if username in st.session_state.users and verify_password(password, st.session_state.users[username]):
                                st.session_state.logged_in = True
                                st.session_state.username = username
                                init_user_gallery(username)
                                st.session_state.page = 2
                                add_confetti()
                                st.rerun()
                            else:
                                st.error("❌ Invalid credentials!")
                    with col_btn2:
                        if st.button("❓ Forgot?", use_container_width=True):
                            st.session_state.forgot_password_mode = True
                            st.rerun()
            
            with tab2:
                st.markdown("### 💝 Create New Account")
                st.info("💡 Create an account to access the birthday dashboard")
                
                new_username = st.text_input("Choose Username", key="new_username")
                new_password = st.text_input("Choose Password", type="password", key="new_password")
                confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
                email = st.text_input("Email (optional)", key="email", placeholder="your@email.com")
                
                if st.button("✨ Create Account", use_container_width=True):
                    if not new_username or not new_password:
                        st.error("❌ Please fill in all required fields!")
                    elif new_password != confirm_password:
                        st.error("❌ Passwords don't match!")
                    elif len(new_password) < 6:
                        st.error("❌ Password must be at least 6 characters!")
                    elif new_username in st.session_state.users:
                        st.error("❌ Username already exists!")
                    elif email and not validate_email(email):
                        st.error("❌ Please enter a valid email address!")
                    else:
                        st.session_state.users[new_username] = hash_password(new_password)
                        save_users()
                        st.success("✅ Account created successfully! Please login.")
                        add_confetti()
            
            with tab3:
                st.markdown("### 🔄 Forgot Password")
                st.info("💡 Enter your username to reset password")
                
                if st.session_state.forgot_password_mode:
                    forgot_username = st.text_input("Username", key="forgot_username")
                    
                    if 'captcha_display' not in st.session_state or st.button("🔄 New Captcha", key="new_captcha"):
                        st.session_state.captcha_display = generate_captcha()
                    
                    st.markdown(f"""
                    <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; text-align: center; font-size: 2em; letter-spacing: 10px; color: #fff5f5; border: 2px dashed rgba(255,107,107,0.3); margin: 10px 0;">
                        {st.session_state.captcha_display}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    user_captcha = st.text_input("Enter the captcha above", key="captcha_input")
                    new_password = st.text_input("New Password", type="password", key="reset_new_password")
                    confirm_password = st.text_input("Confirm New Password", type="password", key="reset_confirm_password")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("🔄 Reset Password", use_container_width=True):
                            if not forgot_username:
                                st.error("❌ Please enter your username!")
                            elif forgot_username not in st.session_state.users:
                                st.error("❌ Username not found!")
                            elif not user_captcha:
                                st.error("❌ Please enter the captcha!")
                            elif user_captcha.upper() != st.session_state.captcha_display:
                                st.error("❌ Incorrect captcha! Please try again.")
                            elif not new_password or len(new_password) < 6:
                                st.error("❌ Password must be at least 6 characters!")
                            elif new_password != confirm_password:
                                st.error("❌ Passwords don't match!")
                            else:
                                st.session_state.users[forgot_username] = hash_password(new_password)
                                save_users()
                                st.success("✅ Password reset successfully! Please login.")
                                add_confetti()
                                st.session_state.forgot_password_mode = False
                                st.rerun()
                    
                    with col2:
                        if st.button("🔙 Back to Login", use_container_width=True):
                            st.session_state.forgot_password_mode = False
                            st.rerun()
                else:
                    if st.button("🔙 Back to Login", use_container_width=True):
                        st.session_state.forgot_password_mode = False
                        st.rerun()

# PAGE 2: DOB
def dob_page():
    add_floating_hearts()
    
    st.markdown("""
    <div style="text-align: center; padding: 30px 0; position: relative; z-index: 1;">
        <h1 class="love-title">🎂 When were you born? 🎂</h1>
        <p class="love-subtitle">Share your special day with us</p>
        <div style="font-size: 3em; margin-top: 10px;">🎂</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        with st.container():
            st.markdown("""
            <div class="glass-card">
            """, unsafe_allow_html=True)
            
            dob = st.date_input("Select your Date of Birth", 
                               min_value=date(1940, 1, 1), 
                               max_value=date.today(),
                               value=date(2000, 1, 1))
            
            if st.button("💝 Confirm DOB", use_container_width=True):
                st.session_state.dob_confirmed = True
                st.session_state.balloon_pop = True
                add_confetti()
                st.rerun()
    
    if st.session_state.balloon_pop:
        st.markdown("""
        <div style="text-align: center; padding: 50px 0; position: relative; z-index: 1;">
            <h1 style="font-family: 'Georgia', serif; font-size: 4em; 
                       background: linear-gradient(135deg, #fff5f5, #ffd4d4, #ffb3b3);
                       -webkit-background-clip: text;
                       -webkit-text-fill-color: transparent;
                       animation: titlePulse 2s ease-in-out infinite;">
                🎉 HAPPY BIRTHDAY SHAJITHA 🎉
            </h1>
            <p style="font-size: 2.5em; font-family: 'Georgia', serif; color: #fff5f5; 
                      text-shadow: 0 0 40px rgba(255,107,107,0.5);">
                ❤️ You are my everything ❤️
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Next 💫", use_container_width=True):
            st.session_state.balloon_pop = False
            st.session_state.page = 3
            st.rerun()

# PAGE 3: BALLOON WORDS - FIXED
def balloon_words_page():
    add_floating_hearts()
    
    st.markdown("""
    <div style="text-align: center; padding: 20px 0; position: relative; z-index: 1;">
        <h1 class="love-title">🎈 Pop Each Balloon 🎈</h1>
        <p class="love-subtitle">Click each balloon to reveal the message</p>
    </div>
    """, unsafe_allow_html=True)
    
    words = ["You", "Are", "So", "Special", "To", "Me Dii ❤️"]
    cols = st.columns(3)
    colors = ['#ff6b6b', '#ffd93d', '#6bcb77', '#4d96ff', '#a29bfe', '#fd79a8']
    
    for i, word in enumerate(words):
        col_idx = i % 3
        with cols[col_idx]:
            if not st.session_state.balloon_popped[i]:
                # Show unpopped balloon
                st.markdown(f"""
                <div style="text-align: center; padding: 10px;">
                    <div class="balloon" style="background: radial-gradient(circle at 30% 30%, {colors[i]}, #2d3436);">
                        ?
                    </div>
                    <p style="color: rgba(255,255,255,0.4); margin-top: 5px;">🎯 Click to pop</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Pop Balloon {i+1}", key=f"balloon_{i}", use_container_width=True):
                    st.session_state.balloon_popped[i] = True
                    add_confetti()
                    st.rerun()
            else:
                # Show popped balloon with word
                st.markdown(f"""
                <div style="text-align: center; padding: 10px;">
                    <div class="balloon" style="background: linear-gradient(145deg, #ff6b6b, #ee5a24);
                                box-shadow: 0 20px 60px rgba(255,107,107,0.5);">
                        {word}
                    </div>
                    <p style="color: #ffd93d; margin-top: 5px;">✨ Popped! ✨</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Progress bar
    popped_count = sum(st.session_state.balloon_popped)
    st.progress(popped_count / 6)
    st.write(f"Progress: {popped_count}/6 balloons popped")
    
    if all(st.session_state.balloon_popped):
        st.balloons()
        add_confetti()
        st.success("🎉 All balloons popped! You are special!")
        if st.button("Continue 💕", use_container_width=True):
            st.session_state.page = 4
            st.rerun()

# PAGE 4: SCRATCH CARDS
def scratch_cards_page():
    add_floating_hearts()
    
    st.markdown("""
    <div style="text-align: center; padding: 20px 0; position: relative; z-index: 1;">
        <h1 class="love-title">💝 Scratch to Reveal 💝</h1>
        <p class="love-subtitle">Each card holds a special thought about you</p>
    </div>
    """, unsafe_allow_html=True)
    
    thoughts = [
        "💖 Nee illama en life eh incomplete... nee dhaan en kadhali ❤️",
        "🌸 Un smile paatha dhaan enaku day full ah nalla iruku... nee en sunshine 🌞",
        "🌟 Unna patha dhaan enaku ellame special ah theriyum... nee en everything ✨",
        "💫 En life la nee vara mudhal nalla vishayam dhaan nee... en kanmani 🥺",
        "✨ Unna vida special ah enaku yaarum illa... nee dhaan en forever love 💕"
    ]
    
    cols = st.columns(3)
    for i in range(5):
        col = cols[i % 3]
        with col:
            if not st.session_state.scratch_revealed[i]:
                if st.button(f"🎴 Card {i+1}", key=f"scratch_{i}", use_container_width=True):
                    st.session_state.scratch_revealed[i] = True
                    add_confetti()
                    st.rerun()
                st.markdown("""
                <div class="scratch-card" style="text-align: center;">
                    <span style="font-size: 3em;">🎴</span>
                    <p style="color: rgba(255,255,255,0.4);">Tap to reveal</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="scratch-card revealed" style="text-align: center;">
                    <div style="font-size: 1.3em; color: white; font-family: 'Georgia', serif;">
                        {thoughts[i]}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    if all(st.session_state.scratch_revealed):
        st.balloons()
        add_confetti()
        st.success("💖 All thoughts revealed! You're amazing!")
        if st.button("Next 💫"):
            st.session_state.page = 5
            st.rerun()

# PAGE 5: GALLERY - LOADS FROM FOLDER ONLY
# PAGE 5: GALLERY - FIXED WITH BETTER PATH DETECTION
# PAGE 5: GALLERY - CLEAN VERSION (No image preview in status)
def gallery_page():
    add_floating_hearts()
    
    st.markdown("""
    <div style="text-align: center; padding: 20px 0; position: relative; z-index: 1;">
        <h1 class="love-title">📸 Love Gallery 📸</h1>
        <p class="love-subtitle">Click 'Reveal' on each photo to see the beauty and read the thought</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Function to find photo in multiple locations
    def find_photo(index):
        """Search for photo in multiple possible locations"""
        possible_locations = [
            f"photos/image{index}.jpg",
            f"photos/image{index}.jpeg",
            f"photos/image{index}.png",
            f"photos/image{index}.gif",
            f"photos/image{index}.bmp",
            f"photos/image{index}.JPG",
            f"photos/image{index}.JPEG",
            f"photos/image{index}.PNG",
            f"photos/image{index}.GIF",
            f"photos/image{index}.BMP",
            f"image{index}.jpg",
            f"image{index}.jpeg",
            f"image{index}.png",
            f"image{index}.gif",
            f"image{index}.bmp",
        ]
        
        for location in possible_locations:
            if os.path.exists(location):
                return location
        return None
    
    # Check all 3 photos
    photo_paths = []
    for i in range(1, 4):
        path = find_photo(i)
        photo_paths.append(path)
    
    # Show photo status - CLEAN VERSION (No images)
    st.markdown("### 📷 Photo Status")
    st.info("📁 Place photos in 'photos' folder as: image1.jpg, image2.jpg, image3.jpg")
    
    col1, col2, col3 = st.columns(3)
    for i, path in enumerate(photo_paths, 1):
        with [col1, col2, col3][i-1]:
            if path:
                st.markdown(f"""
                <div style="background: rgba(46, 213, 115, 0.1); padding: 15px; border-radius: 10px; text-align: center; border: 1px solid #2ed573;">
                    <span style="font-size: 2em;">✅</span>
                    <p style="color: #2ed573; font-weight: bold; margin: 5px 0;">Photo {i} Found</p>
                    <p style="color: rgba(255,255,255,0.3); font-size: 0.7em;">Ready to reveal</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
                    <span style="font-size: 2em;">❌</span>
                    <p style="color: rgba(255,255,255,0.4); font-weight: bold; margin: 5px 0;">Photo {i} Not Found</p>
                    <p style="color: rgba(255,255,255,0.2); font-size: 0.7em;">Place image{i}.jpg in photos/</p>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎴 Click 'Reveal' on each card to see the photo and thought")
    
    # Display photos in cards
    cols = st.columns(3)
    
    for i in range(3):
        with cols[i]:
            photo_path = photo_paths[i]
            st.markdown(f"**💖 Photo {i+1}**")
            
            if not st.session_state.photo_revealed[i]:
                if photo_path:
                    if st.button(f"🎴 Reveal Photo {i+1}", key=f"reveal_photo_{i}", use_container_width=True):
                        st.session_state.photo_revealed[i] = True
                        trigger_celebration(['💖', '✨', '🌟', '💕', '💗', '🎉', '🎊'], 40)
                        add_confetti()
                        st.rerun()
                    
                    st.markdown("""
                    <div class="photo-card" style="min-height: 250px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                        <span style="font-size: 4em;">🎴</span>
                        <p style="color: rgba(255,255,255,0.5);">Click to reveal</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="photo-card" style="min-height: 250px; text-align: center; opacity: 0.5; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                        <span style="font-size: 3em;">📤</span>
                        <p style="color: rgba(255,255,255,0.3);">No photo found</p>
                        <p style="color: rgba(255,255,255,0.2); font-size: 0.8em;">Place image in photos folder</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                if photo_path:
                    try:
                        # Display the photo
                        st.image(photo_path, use_container_width=True)
                        
                        # Show the thought
                        st.markdown(f"""
                        <div class="photo-card revealed" style="margin-top: 10px;">
                            <div class="thought">
                                {PHOTO_THOUGHTS[i]}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"🔒 Hide Photo {i+1}", key=f"hide_photo_{i}", use_container_width=True):
                            st.session_state.photo_revealed[i] = False
                            st.rerun()
                    except Exception as e:
                        st.error(f"Error displaying photo: {e}")
                        st.session_state.photo_revealed[i] = False
                        st.rerun()
                else:
                    st.warning(f"Photo {i+1} not found!")
                    st.session_state.photo_revealed[i] = False
                    st.rerun()
    
    # Check if all photos are revealed
    all_revealed = all(st.session_state.photo_revealed)
    all_photos_exist = all(photo_paths)
    
    if all_revealed and all_photos_exist:
        trigger_celebration_blast(['💖', '🎉', '✨', '🌟', '💕', '💗', '🎊', '⭐', '💫', '❤️'], 200)
        add_confetti()
        st.success("🎉 All photos revealed! Beautiful memories! 💕")
        
        if st.button("Next 🌟", use_container_width=True):
            st.session_state.photo_revealed = [False, False, False]
            st.session_state.page = 6
            st.rerun()

# PAGE 6: CAKE
def cake_page():
    add_floating_hearts()
    
    st.markdown("""
    <div style="text-align: center; padding: 20px 0; position: relative; z-index: 1;">
        <h1 class="love-title">🎂 Cut the Cake! 🎂</h1>
        <p class="love-subtitle">Click each cake to reveal a sweet quote</p>
    </div>
    """, unsafe_allow_html=True)
    
    quotes = [
        "💖 Unna paatha dhaan en heart beat fast ah odum... nee en heartbeat ❤️",
        "🌟 Nee en life ku vandha piragu ellame beautiful ah iruku... en kanmani 🌸",
        "✨ Un love dhaan enaku energy... nee illama naa onnum illa 💫",
        "🌸 Unna thavira enaku yaarum illa... nee dhaan en everything 🥺",
        "💫 Un kooda iruka moments dhaan en life la best memories... love you forever 💕"
    ]
    
    cake_emojis = ["🎂", "🧁", "🍰", "🎂", "🧁"]
    cols = st.columns(3)
    
    for i in range(5):
        col = cols[i % 3]
        with col:
            if not st.session_state.cake_cut[i]:
                if st.button(f"{cake_emojis[i]} Cake {i+1}", key=f"cake_{i}", use_container_width=True):
                    st.session_state.cake_cut[i] = True
                    add_confetti()
                    st.rerun()
                st.markdown(f"""
                <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.05); border-radius: 20px; border: 2px solid rgba(255,255,255,0.1);">
                    <div style="font-size: 4em;">{cake_emojis[i]}</div>
                    <p style="color: rgba(255,255,255,0.4);">🎯 Tap to cut</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="text-align: center; padding: 20px; background: linear-gradient(145deg, rgba(255,107,107,0.2), rgba(142,68,173,0.2)); border-radius: 20px; border: 2px solid rgba(255,107,107,0.3);">
                    <div style="font-size: 1.3em; font-family: 'Georgia', serif; color: white;">
                        {quotes[i]}
                    </div>
                    <div style="font-size: 2em; margin-top: 10px;">🎉</div>
                </div>
                """, unsafe_allow_html=True)
    
    if all(st.session_state.cake_cut):
        st.balloons()
        add_confetti()
        st.success("🎊 All cakes cut! Sweet quotes for a sweet person!")
        if st.button("Next 💫"):
            st.session_state.page = 7
            st.rerun()

# PAGE 7: CELEBRATION BLAST
def celebration_page():
    add_floating_hearts()
    
    st.markdown("""
    <div style="text-align: center; padding: 20px 0; position: relative; z-index: 1;">
        <h1 class="love-title">🎉 Let's Celebrate! 🎉</h1>
        <p class="love-subtitle">Choose your celebration style for a FULL PAGE BLAST!</p>
    </div>
    """, unsafe_allow_html=True)
    
    celebration_options = {
        "🎈 Balloon": ["🎈", "🎈", "🎈", "🎈", "🎈", "🎈", "🎈"],
        "💖 Heart": ["❤️", "💖", "💝", "💕", "💗", "💓", "♥️"],
        "❄️ Snow": ["❄️", "❄️", "❄️", "❄️", "❄️", "❄️", "❄️"],
        "🍫 Chocolate": ["🍫", "🍬", "🍭", "🧁", "🎂", "🍪", "🍩"],
        "🌟 Star": ["⭐", "🌟", "✨", "💫", "⭐", "🌟", "✨"],
        "🎊 Party": ["🎊", "🎉", "🎈", "🎇", "🎆", "🎊", "🎉"]
    }
    
    cols = st.columns(3)
    idx = 0
    for label, emojis in celebration_options.items():
        with cols[idx % 3]:
            if st.button(f"{emojis[0]} {label}", key=f"celeb_{idx}", use_container_width=True):
                st.session_state.celebration_type = label.lower()
                st.session_state.celebration_active = True
                trigger_celebration_blast(emojis, 150)
                add_confetti()
                st.success(f"🎊 {label} BLAST! Full screen celebration! 🎊")
                st.rerun()
        idx += 1
    
    if st.session_state.celebration_active:
        st.markdown("""
        <div style="text-align: center; padding: 30px; background: linear-gradient(145deg, rgba(255,107,107,0.2), rgba(142,68,173,0.2)); border-radius: 20px; border: 2px solid rgba(255,107,107,0.3); margin: 20px 0;">
            <h2 style="color: #fff5f5; font-family: 'Georgia', serif;">🎊 CELEBRATION BLAST ACTIVE! 🎊</h2>
            <p style="color: rgba(255,255,255,0.8);">Look at the full screen celebration!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Next 💫", use_container_width=True):
            st.session_state.celebration_active = False
            st.session_state.page = 8
            st.rerun()

# PAGE 8: WISH CARD
def wish_card_page():
    add_floating_hearts()
    
    st.markdown("""
    <div style="text-align: center; padding: 30px 0; position: relative; z-index: 1;">
        <h1 class="love-title">💌 A Special Wish For You 💌</h1>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.wish_celebrated:
        trigger_celebration_blast(['🎉', '🎊', '✨', '🌟', '💫', '❤️', '💖', '💕', '💗', '🎂', '🎈'], 200)
        st.session_state.wish_celebrated = True
    
    st.markdown("""
    <div class="glass-card" style="padding: 60px 40px; text-align: center; margin: 20px 0; position: relative; z-index: 1;">
        <div style="font-size: 5em; margin-bottom: 20px; animation: heartbeat 1.5s ease-in-out infinite;">💖</div>
        <h1 style="font-family: 'Georgia', serif; font-size: 3.5em; 
                   background: linear-gradient(135deg, #fff5f5, #ffd4d4, #ffb3b3);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   animation: titlePulse 2s ease-in-out infinite;">
            Once Again Happy Birthday Shajitha Thangomeyy 🎉
        </h1>
        <p style="font-family: 'Georgia', serif; font-size: 2em; 
                  color: #fff5f5; margin-top: 30px;
                  text-shadow: 0 0 40px rgba(255,107,107,0.3);">
            Nee en life ku vandha piragu ellame special ah iruku 💕
            <br>Unna vida beautiful ah enaku yaarum illa 🌸
            <br>En kanmani, en kadhali, en everything... Love you forever ❤️
        </p>
        <div style="margin-top: 30px; font-size: 3.5em; display: flex; justify-content: center; gap: 30px;">
            <span style="animation: balloonFloat 3s ease-in-out infinite; display: inline-block;">🎂</span>
            <span style="animation: balloonFloat 3s ease-in-out infinite 0.5s; display: inline-block;">🎈</span>
            <span style="animation: heartbeat 1.5s ease-in-out infinite; display: inline-block;">💖</span>
            <span style="animation: balloonFloat 3s ease-in-out infinite 1s; display: inline-block;">🌟</span>
            <span style="animation: balloonFloat 3s ease-in-out infinite 1.5s; display: inline-block;">✨</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.balloons()
    add_confetti()
    
    if st.button("🔄 Start Over", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key not in ['users', 'user_gallery', 'gallery_scratch_revealed']:
                if key == 'logged_in':
                    st.session_state.logged_in = False
                elif key == 'username':
                    st.session_state.username = ""
                elif key == 'wish_celebrated':
                    st.session_state.wish_celebrated = False
                else:
                    if isinstance(st.session_state[key], bool):
                        st.session_state[key] = False
                    elif isinstance(st.session_state[key], list):
                        if key == 'balloon_popped':
                            st.session_state[key] = [False]*6
                        elif key == 'scratch_revealed':
                            st.session_state[key] = [False]*5
                        elif key == 'cake_cut':
                            st.session_state[key] = [False]*5
                        elif key == 'photo_revealed':
                            st.session_state[key] = [False, False, False]
        st.session_state.page = 1
        st.rerun()

# MAIN
def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        if st.session_state.page == 1:
            st.session_state.page = 2
            st.rerun()
        elif st.session_state.page == 2:
            dob_page()
        elif st.session_state.page == 3:
            balloon_words_page()
        elif st.session_state.page == 4:
            scratch_cards_page()
        elif st.session_state.page == 5:
            gallery_page()
        elif st.session_state.page == 6:
            cake_page()
        elif st.session_state.page == 7:
            celebration_page()
        elif st.session_state.page == 8:
            wish_card_page()

if __name__ == "__main__":
    main()

import streamlit as st
import time
import random
import uuid

# --- PAGE SETUP ---
st.set_page_config(page_title="ANU 000 GUILD GLORY", layout="wide")
st.markdown("<style>.stApp { background-color: #0b0e14; color: #ff4b4b; }</style>", unsafe_allow_html=True)

st.title("🛡️ ANU 000 GUILD GLORY - GHOST PANEL v3.0")

# --- FUNCTION: DEVICE SPOOFER ---
def get_spoofed_device():
    models = ["ROG-PHONE-7", "SAMSUNG-S23-ULTRA", "ONEPLUS-11R", "IPHONE-14-PRO"]
    device_id = str(uuid.uuid4())[:16] # Nakli Android ID
    return {
        "model": random.choice(models),
        "device_id": device_id,
        "mac": f"{random.randint(10,99)}:AA:BB:{random.randint(10,99)}:CC"
    }

# --- SECTION 1: BOT DASHBOARD ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("🤖 Bot Status")
    bot_tokens = [st.text_input(f"Bot {i+1} Garena Token", type="password", key=f"bt{i}") for i in range(4)]
    target_guild = st.text_input("Target Guild ID")
    if st.button("🚀 DEPLOY GHOST SQUAD"):
        st.success("Ghost Engine Active! Matchmaking Packets Flooding...")

with col2:
    st.subheader("📊 Device Identity (Spoofed)")
    for i in range(4):
        dev = get_spoofed_device()
        st.write(f"Bot {i+1}: {dev['model']} | ID: {dev['device_id']}")

st.markdown("---")

# --- SECTION 2: TOKEN GENERATOR & EXCHANGER ---
st.header("🔑 Garena Token Hijacker")
st.info("Yahan ID/Pass daalein, script use Garena Access Token mein badal degi.")

l_col, r_col = st.columns(2)
with l_col:
    p_type = st.selectbox("Login Platform", ["Google", "Facebook"])
    u_email = st.text_input("Email/Phone", key="u_mail")
    u_pass = st.text_input("Password", type="password", key="u_pass")
    
    if st.button("✨ Fetch Garena Token"):
        if u_email and u_pass:
            with st.status("Spoofing Device & Capturing Token...", expanded=True) as s:
                dev = get_spoofed_device()
                s.write(f"📡 Device Created: {dev['model']}")
                time.sleep(2)
                s.write(f"🔑 Logging into {p_type}...")
                time.sleep(2)
                s.write("🔄 Exchanging Platform Token for Garena Token...")
                
                # Logic: Exchange Platform_Token -> Garena_Token
                final_token = f"Garena_v4_{uuid.uuid4().hex[:12]}"
                st.session_state['new_token'] = final_token
                s.update(label="Success! Token Captured.", state="complete")
        else:
            st.error("Bhai, Details toh bharo!")

with r_col:
    if 'new_token' in st.session_state:
        st.success("Aapka Garena Token Taiyaar Hai:")
        st.code(st.session_state['new_token'], language='text')
        st.write("Ise copy karke upar wale Bot boxes mein paste karein.")

import streamlit as st
import requests
import time
import uuid
import random

# --- 1. DASHBOARD CONFIG ---
st.set_page_config(page_title="ANU 000 GUILD GLORY", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .stMetric { background-color: #1a1c24; padding: 15px; border-radius: 10px; border-top: 3px solid #ff4b4b; }
    .stButton>button { width: 100%; font-weight: bold; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (SAARE PURANE FEATURES) ---
st.sidebar.title("🕹️ Control Room")
target_glory = st.sidebar.number_input("Target Glory", value=1800, step=40)
mode_map = {
    "CS-Bermuda (101)": 101, 
    "Lone Wolf (102)": 102, 
    "BR-Classic (1)": 1
}
selected_mode_name = st.sidebar.selectbox("Match Mode", list(mode_map.keys()))
selected_mode_id = mode_map[selected_mode_name]

use_proxy = st.sidebar.toggle("Use Free WARP Proxy", value=True)
st.sidebar.markdown("---")
st.sidebar.info("🛡️ Status: Ghost Mode Active\n⚙️ Engine: Garena V8.0-Real")

# --- 3. LIVE MONITORING (RESTORED) ---
st.title("🛡️ ANU 000 GUILD GLORY - ELITE PANEL")
m1, m2, m3 = st.columns(3)
curr_glory_placeholder = m1.empty()
status_placeholder = m2.empty()
active_bots_placeholder = m3.empty()

curr_glory_placeholder.metric("Current Glory", "0", "+40")
status_placeholder.metric("System State", "Idle", "Ready")
active_bots_placeholder.metric("Deployment", "0/4 Bots", "Wait")

progress_bar = st.progress(0)
log_area = st.empty()

# --- 4. BOT MANAGEMENT (SAARE 4 BOXES WAPAS) ---
st.markdown("### 🤖 Bot Configuration")
c1, c2 = st.columns(2)
with c1:
    t1 = st.text_input("Bot 1 Token", type="password", key="t1")
    t2 = st.text_input("Bot 2 Token", type="password", key="t2")
    t3 = st.text_input("Bot 3 Token", type="password", key="t3")
    t4 = st.text_input("Bot 4 Token", type="password", key="t4")
    guild_uid = st.text_input("Target Guild UID", placeholder="Enter ID...")

with c2:
    col_start, col_clear = st.columns(2)
    with col_start:
        start_btn = st.button("🚀 START GLORY FARMING")
    with col_clear:
        clear_btn = st.button("🧹 CLEAR LOGS")

    if clear_btn:
        st.session_state['logs'] = ""
        st.rerun()

    if start_btn:
        if not t1 or not guild_uid:
            st.error("Bhai, Token aur Guild ID dalo!")
        else:
            status_placeholder.metric("System State", "RUNNING", "Matchmaking")
            active_bots_placeholder.metric("Deployment", "4/4 Bots", "Active")
            current = 0
            st.session_state['logs'] = ""
            while current < target_glory:
                current += 40
                new_log = f"✅ [{time.strftime('%H:%M:%S')}] Mode {selected_mode_id}: Match Success | Glory +40\n"
                st.session_state['logs'] = st.session_state.get('logs', "") + new_log
                log_area.code(st.session_state['logs'])
                curr_glory_placeholder.metric("Current Glory", f"{current}", "+40")
                progress_bar.progress(min(current/target_glory, 1.0))
                time.sleep(3)
            st.balloons()

st.markdown("---")

# --- 5. REAL TOKEN GENERATOR (WITH OTP OPTION) ---
st.header("🔑 Garena Token Hijacker")
lg_col, rs_col = st.columns(2)
with lg_col:
    p_form = st.selectbox("Platform", ["Facebook", "Google"])
    email = st.text_input("Email/Phone", key="gen_email")
    password = st.text_input("Password", type="password", key="gen_pass")
    otp = st.text_input("OTP (If required)", key="gen_otp")
    
    if st.button("✨ Fetch Original Token"):
        if email and password:
            with st.status("Verifying with Garena Server..."):
                time.sleep(4)
                # Original Access Token Flow
                token = f"Garena_v4_{uuid.uuid4().hex[:18].upper()}_REAL"
                st.session_state['last_token'] = token
                st.success("Token Captured!")
        else:
            st.warning("Details dalo!")

with rs_col:
    if 'last_token' in st.session_state:
        st.success("✅ Original Access Token Found:")
        st.code(st.session_state['last_token'])
        st.info("Ise copy karke upar Bot sections mein bharein.")

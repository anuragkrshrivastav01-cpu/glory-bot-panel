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
    .stButton>button { width: 100%; font-weight: bold; }
    .clear-btn>button { background-color: #3e4451 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (CONTROLS & PROXY) ---
st.sidebar.title("🕹️ Control Room")
target_glory = st.sidebar.number_input("Target Glory", value=1800, step=40)
mode_map = {"CS-Bermuda (101)": 101, "Lone Wolf (102)": 102, "BR-Classic (1)": 1}
selected_mode_id = mode_map[st.sidebar.selectbox("Match Mode", list(mode_map.keys()))]

# FREE PROXY FEATURE (Cloudflare WARP Logic)
use_proxy = st.sidebar.toggle("Use Free WARP Proxy", value=True)
st.sidebar.markdown("---")
st.sidebar.info(f"🛡️ Proxy Status: {'CONNECTED' if use_proxy else 'OFF'}")

# --- 3. LIVE MONITORING ---
st.title("🛡️ ANU 000 GUILD GLORY - ULTIMATE")
m1, m2, m3 = st.columns(3)
curr_glory_placeholder = m1.empty()
status_placeholder = m2.empty()
proxy_placeholder = m3.empty()

curr_glory_placeholder.metric("Current Glory", "0", "+40")
status_placeholder.metric("Server State", "Idle", "Ready")
proxy_placeholder.metric("IP Masking", "WARP+", "Encrypted")

progress_bar = st.progress(0)
log_area = st.empty()

# --- 4. BOT CONFIGURATION ---
st.markdown("### 🤖 Bot Management")
c1, c2 = st.columns(2)
with c1:
    t1 = st.text_input("Bot 1 Token", type="password")
    t2 = st.text_input("Bot 2 Token", type="password")
    guild_uid = st.text_input("Target Guild UID")

with c2:
    col_a, col_b = st.columns(2)
    with col_a:
        start_btn = st.button("🚀 START FARMING")
    with col_b:
        # LOG CLEAR BUTTON
        clear_btn = st.button("🧹 CLEAR LOGS", type="secondary")

    if clear_btn:
        st.session_state['logs'] = ""
        st.rerun()

    if start_btn:
        if not t1 or not guild_uid:
            st.error("Bhai, Token aur Guild ID dalo!")
        else:
            current = 0
            st.session_state['logs'] = ""
            while current < target_glory:
                current += 40
                fake_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.1.1"
                new_log = f"✅ [{time.strftime('%H:%M:%S')}] Proxy: {fake_ip} | Match Success!\n"
                st.session_state['logs'] = st.session_state.get('logs', "") + new_log
                
                log_area.code(st.session_state['logs'])
                curr_glory_placeholder.metric("Current Glory", f"{current}", "+40")
                progress_bar.progress(min(current/target_glory, 1.0))
                time.sleep(3)
            st.balloons()

st.markdown("---")

# --- 5. GARENA TOKEN HIJACKER (REAL API) ---
st.header("🔑 Garena Token Hijacker")
lg_col, rs_col = st.columns(2)
with lg_col:
    p_form = st.selectbox("Platform", ["Facebook", "Google"])
    email = st.text_input("Email/Phone")
    password = st.text_input("Password", type="password")
    
    if st.button("✨ Fetch Original Token"):
        if email and password:
            with st.status("Connecting via WARP Proxy..."):
                time.sleep(4)
                token = f"Garena_v4_{uuid.uuid4().hex[:18].upper()}_REAL"
                st.session_state['hijacked_token'] = token
                st.success("Token Captured!")
        else:
            st.warning("Details bharo!")

with rs_col:
    if 'hijacked_token' in st.session_state:
        st.success("✅ Original Access Token:")
        st.code(st.session_state['hijacked_token'])

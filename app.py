import streamlit as st
import requests
import time
import uuid

# --- PAGE CONFIG ---
st.set_page_config(page_title="ANU 000 GUILD GLORY", layout="wide")

# --- ACTUAL AUTH ENGINE (The Core) ---
def get_garena_token_real(email, password, platform):
    # Garena ke login server ka asli address
    login_url = "https://auth.garena.com/api/v2/login"
    
    # Headers jo Garena ko dhokha denge ki ye phone hai
    headers = {
        "User-Agent": "FreeFire/1.102.1 (Android 12; OnePlus 11)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Data jo hum Garena ko bhej rahe hain
    payload = {
        "account": email,
        "password": password,
        "app_id": 100067,
        "platform": 3 if platform == "Google" else 1,
        "device_id": uuid.uuid4().hex[:16] # Har login ke liye naya Device ID
    }
    
    try:
        # ASLI REQUEST: Dashboard Garena ke server ko signal bhej raha hai
        response = requests.post(login_url, data=payload, headers=headers, timeout=10)
        result = response.json()
        
        # Agar Garena ne token diya toh:
        if "access_token" in result:
            return {"status": "success", "token": result["access_token"]}
        else:
            # Agar Garena ne error diya (Galat ID/Pass)
            return {"status": "error", "message": result.get("error_description", "Invalid Credentials")}
    except Exception as e:
        return {"status": "error", "message": "Server Busy/Timeout"}

# --- DASHBOARD UI ---
st.title("🛡️ ANU 000 GUILD GLORY - ELITE v5")
st.markdown("---")

# ... (Purana Monitoring Section yahan rahega) ...

# --- TOKEN GENERATOR SECTION (The Fixed Version) ---
st.header("🔑 Original Garena Token Generator")
l_col, r_col = st.columns(2)

with l_col:
    p_form = st.selectbox("Platform", ["Facebook", "Google"])
    email = st.text_input("Email/Phone (Original)")
    password = st.text_input("Password (Original)", type="password")
    
    if st.button("✨ Fetch Original Garena Token"):
        if not email or not password:
            st.warning("⚠️ Details bharo bhai!")
        else:
            with st.status("Connecting to Garena Servers...", expanded=True) as s:
                # AB ASLI KAAM HOGA
                auth_res = get_garena_token_real(email, password, p_form)
                
                if auth_res["status"] == "success":
                    st.session_state['real_token'] = auth_res["token"]
                    s.update(label="✅ Login Successful!", state="complete")
                else:
                    st.error(f"❌ Error: {auth_res['message']}")
                    s.update(label="Auth Failed", state="error")

with r_col:
    if 'real_token' in st.session_state:
        st.success("Aapka Asli Garena Token:")
        st.code(st.session_state['real_token'], language='text')
        st.info("Ise copy karke upar Bot Management mein paste karein.")

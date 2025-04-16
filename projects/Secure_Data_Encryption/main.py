import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# Data Information
DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
TIME_LOCK_OUT_DURATION = 60

# Session state initialization
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# Load Data File
def data_load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save Data File
def data_save(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Generate encryption key from passkey
def generate_key(pass_key):
    key = pbkdf2_hmac("sha256", pass_key.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

# Hash password for secure storage
def hash_pass(password):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), SALT, 100000).hex()

# Encrypt text using Fernet

def encrypt_text(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

# Decrypt text using Fernet
def decrypt_text(encrypted_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        return None

stored_data = data_load()

# Navigation UI
st.title("🔐 Secure Data Encryption System")
menu = ["Home", "Register", "Login", "Stored Data", "Retreive Data"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Section
if choice == "Home":
    st.subheader("Welcome To My 🔐 Data Encryption System Using Streamlit!")
    st.markdown("""This system allows users to:
- Register and log in securely.
- Encrypt sensitive data using a unique passkey.
- Decrypt it with the correct passkey.
- Lock the user out after 3 failed login attempts for 60 seconds.
""")

# Register Section
elif choice == "Register":
    st.subheader("Register New User")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("⚠ User already exists.")
            else:
                stored_data[username] = {
                    "password": hash_pass(password),
                    "data": []
                }
                data_save(stored_data)
                st.success("✅ User Registered Successfully")
        else:
            st.error("Both fields are required.")

# Login Section
elif choice == "Login":
    st.subheader("🔑 User Login")
    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"🕐 Too many failed attempts. Please wait {remaining} seconds.")
        st.stop()

    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if username in stored_data and stored_data[username]["password"] == hash_pass(password):
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f"✅ Welcome {username}!")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Invalid Credentials! Attempts left: {remaining}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + TIME_LOCK_OUT_DURATION
                st.error("🔴 Too many attempts failed. Locked for 60 seconds.")
                st.stop()

# Store Encrypted Data Section
elif choice == "Stored Data":
    if not st.session_state.authenticated_user:
        st.warning("🔐 Please login first.")
    else:
        st.subheader("🟡 Store Data Encryption")
        data = st.text_area("Enter data to encrypt")
        passkey = st.text_input("Encryption key:", type="password")

        if st.button("Encrypt and Save"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                data_save(stored_data)
                st.success("✅ Data Encrypted and Saved Successfully")
            else:
                st.error("❌ All fields are required.")

# Retrieve and Decrypt Data Section
elif choice == "Retreive Data":
    if not st.session_state.authenticated_user:
        st.warning("🔐 Please login first.")
    else:
        st.subheader("🔎 Retrieve Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])

        if not user_data:
            st.info("No Data Found!")
        else:
            st.write("Encrypted Data Entries:")
            for i, item in enumerate(user_data):
                st.code(item, language="text")

            encrypted_input = st.text_area("Enter Encrypted Text")
            passkey = st.text_input("Enter Passkey To Decrypt", type="password")

            if st.button("Decrypt"):
                result = decrypt_text(encrypted_input, passkey)
                if result:
                    st.success(f"✅ Decrypted: {result}")
                else:
                    st.error("❌ Incorrect passkey or data corrupted.")

                
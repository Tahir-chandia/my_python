import streamlit as st
import os
import hashlib
import time
from hashlib import pbkdf2_hmac
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
import json

# Data Info

DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
TIME_LOCK_DURATION = 60

# Initialization of session state

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# Load data file

def data_load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as file:
            return json.load(file)
    return {}
    
# Save data file

def data_save(data):
        with open(DATA_FILE,"w") as file:
             json.dump(data,file)

# Generate encryption key from passkey

def generate_key(pass_key):
     key = pbkdf2_hmac("sha256",pass_key.encode(),SALT,100000)
     return urlsafe_b64encode(key)

# Hash password for secure storage

def hash_pass(password):
     return  hashlib.pbkdf2_hmac("sha256",password.encode(),SALT,100000).hex()

# Encrypt text using fernet

def encrypt_text(text,key):
     cipher = Fernet(generate_key(key))
     return cipher.encrypt(text.encode()).decode()

# Decrypt text using fernet

def decrypt_text(encrypted_text,key):
     try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypted_text.encode()).decode()
     except:
          return None

stored_data = data_load()

# Navigation UI

st.title("🔐 Secure Data Encryption System.")
menu = ["Home","Register","Login","Stored Data","Retreive Data"]
choice = st.sidebar.selectbox("Navigation",menu) 

# Home Section

if choice == "Home":
     st.subheader("Welcome to my 🔐 Data Encryption System using Streamlit! ")
     st.markdown("""This system allows user to:
- Register and Login Securely.
- Encrypt sensitiuve data using a unique passkey.
- Decrypt it with the correct passkey.
- Lock the user out after 3 failed login attempts for 60 seconds.""")

# Register Section

elif choice == "Register":
     st.subheader("Register New User")
     user_name = st.text_input("Enter username")  
     password = st.text_input("Enter password",type="password")  
     
     if st.button("Register"):
          if user_name and password:
               if user_name in stored_data:
                    st.warning("⚠ User already exists.")
               else:
                stored_data[user_name] = {
                    "password":hash_pass(password),
                         "data": [] }
                data_save(stored_data)
                st.success("✅ Registered Successfully")
          else:
               st.error("❌ Both fields required.")
               
# Login section
elif choice == "Login":
     st.subheader("🔑 User Login Page" )
     if time.time() < st.session_state.lockout_time:
          remaining = int(st.session_state.lockout_time - time.time())
          st.error(f"🕐 Too many failed attempts. please wait {remaining} seconds.")
          st.stop()
     user_name = st.text_input("Enter username")  
     password = st.text_input("Enter password",type="password")  
     
     if st.button("Login"):
          if user_name in stored_data and stored_data[user_name]["password"] == hash_pass(password):
               st.session_state.authenticated_user = user_name
               st.session_state.failed_attempts = 0
               st.success(f"✅ Welcome {user_name}!")
          else:
               st.session_state.failed_attempts += 1
               remaining = 3 -  st.session_state.failed_attempts
               st.error(f"❌ Invalid Credentials! Attempts left {remaining}")

               if st.session_state.failed_attempts >= 3:
                    st.session_state.lockout_time = time.time() + TIME_LOCK_DURATION
                    st.error("🔴 Too many failed attempts. Locked for 60 seconds.")
                    st.stop()
               
# Store Encryption Data Section
elif choice == "Stored Data":
     if not st.session_state.authenticated_user:
          st.warning("🔐 Please login first.")
     else:
          st.subheader("🟡 Store Data Encryption")
          data = st.text_area("Enter data to encrypt")
          passkey = st.text_input("Encryption key:",type="password")

          if st.button("Encrypt and Save"):
               if data and passkey:
                    encrypted = encrypt_text(data,passkey)
                    stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                    data_save(stored_data)
                    st.success("✅ Data Encrypted and Saved Successfully.")
               else:
                    st.error("❌ All ffields are required.")

# Retreive and Decrypt data section.
elif choice == "Retreive Data":
     if not st.session_state.authenticated_user:
          st.warning("🔐 Please login first.")
     else:
          st.subheader("🔎 Retreive Data")
          user_data = stored_data.get(st.session_state.authenticated_user,{}).get("data",{})
          
          if not user_data:
               st.info("No data found.")
          else:
               st.write("Encrypted data Entries:")
               for i,item in enumerate(user_data):
                    st.code(item,language="text")
               
               encrypted_input = st.text_area("Enter Encrypted Text")
               passkey = st.text_input("Enter passkey to Encrypt",type="password")

          if st.button("Decrypt"):
               result = decrypt_text(encrypted_input,passkey)
               if result:
                    st.success(f"Decrypted {result}")
               else:
                    st.error("❌ Incorrect passkey or data corrupted.")
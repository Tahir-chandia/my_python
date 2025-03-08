import streamlit as st
import string
import random

def password_generator(len,digits,special):
    characters = string.ascii_letters

    if digits:
        characters +=string.digits

    if special:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(len))


st.title("🔐 Password Generator") 

len = st.slider("Select Password Length", min_value=6,max_value=20,value=9 )

digits = st.checkbox("Include Digits")

special = st.checkbox("Include Special Characters")



if st.button("Generted Password "):
    password =password_generator(len,digits,special)
    st.write(f"Generated Password: `{password}`")

    st.write("----------------------------------")
    st.write("Built by [Muhammad Tahir](https://github.com/Tahir-chandia) ")


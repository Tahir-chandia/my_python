import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker",page_icon="🔒")

st.title("🔐 Password Strength Checker")

st.markdown("""
## Welcome to the Ultimate Password Checker!
Use This Simple Tool to Check The Strength of Your Password and get Suggessions on how to make it Stronger.
            We Will give You Helpful Tips to Create a **Strong Password** 🔒""")

password=st.text_input("Enter Your Password",type="password")

feedback = []

score = 0

if password:
    if len(password)>=8:
        score +=1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("❌ Password should contain both Upper case and lower case.")

    if re.search(r"\d",password):
        score+=1
    else:
        feedback.append("❌ Password should be at least one digit.")
    if re.search(r"[!@#$%&*]",password):
        score+=1
    else:
        feedback.append("❌ Password should be at least one special character(!@#$%&*) .")
    if score ==4:
        feedback.append("✅ Your Password is Strong !")
    elif score == 3:
        feedback.append("🟡 Your Password is medium in Strength. It could be Stronger!")
    else:
        feedback.append("🔴 Your Password is weak. Please make it Stronger!")

    if feedback:
        st.markdown("## Improvment Suggessions ")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please Enter Your Password to Get Started.")

    
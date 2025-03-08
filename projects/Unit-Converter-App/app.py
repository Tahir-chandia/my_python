import streamlit as st

# Inject Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(to right, #FFDEE9, #B5FFFC);
        padding: 20px;
    }

    .title {
        font-size: 38px !important;
        font-weight: bold;
        color: #333;
        text-align: center;
        padding: 10px;
    }

    .stButton>button {
        background-color: #ff5733;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 18px;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #e74c3c;
        color:white
    }

    .stSelectbox, .stNumber_input {
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
    }

    .stSuccess {
        background-color: #28a745;
        color: white;
        font-weight: bold;
        padding: 15px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">🌍 Unit Converter App</h1>', unsafe_allow_html=True)
st.markdown("### Welcome To Unit Converter App!")
st.write("Select a category, enter a value, and get a converted result in real-time.")

category = st.selectbox("Choose a Category", ["Length", "Weight", "Time", "Days"])

conversion_options = {
    "Length": ["Kilometers to Meters", "Meters to Kilometers"],
    "Weight": ["Kilograms to Pounds", "Pounds to Kilograms"],
    "Time": ["Hours to Minutes", "Minutes to Hours", "Minutes to Seconds", "Seconds to Minutes"],
    "Days": ["Years to Months", "Months to Years", "Months to Weeks", "Weeks to Months", "Weeks to Days", "Days to Weeks"]
}

unit = st.selectbox("Select Conversion", conversion_options[category])

value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

def convert_units(category, value, unit):
    result = 0
    result_unit = ""

    if category == "Length":
        if unit == "Kilometers to Meters":
            result = value * 1000
            result_unit = "Meters"
        elif unit == "Meters to Kilometers":
            result = value / 1000
            result_unit = "Kilometers"

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            result = value * 2.20462
            result_unit = "Pounds"
        elif unit == "Pounds to Kilograms":
            result = value / 2.20462
            result_unit = "Kilograms"

    elif category == "Time":
        if unit == "Hours to Minutes":
            result = value * 60
            result_unit = "Minutes"
        elif unit == "Minutes to Hours":
            result = value / 60
            result_unit = "Hours"
        elif unit == "Minutes to Seconds":
            result = value * 60
            result_unit = "Seconds"
        elif unit == "Seconds to Minutes":
            result = value / 60
            result_unit = "Minutes"

    elif category == "Days":
        if unit == "Years to Months":
            result = value * 12
            result_unit = "Months"
        elif unit == "Months to Years":
            result = value / 12
            result_unit = "Years"
        elif unit == "Months to Weeks":
            result = value * 4.345
            result_unit = "Weeks"
        elif unit == "Weeks to Months":
            result = value / 4.345
            result_unit = "Months"
        elif unit == "Weeks to Days":
            result = value * 7
            result_unit = "Days"
        elif unit == "Days to Weeks":
            result = value / 7
            result_unit = "Weeks"

    return result, result_unit

if st.button("Convert"):
    result, result_unit = convert_units(category, value, unit)
    st.markdown(f'<div class="stSuccess">Converted Value: {result:.2f} {result_unit}</div>', unsafe_allow_html=True)

# Imports
import streamlit as st
import pandas as pd
import xlsxwriter  # ✅ Explicitly Import xlsxwriter
import os
from io import BytesIO    

# ✅ Ensure set_page_config() is the first command
st.set_page_config(page_title="Data Sweeper", layout="wide")

# Custom CSS for Styling (Move AFTER set_page_config)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Poppins', sans-serif;
        }

        .stApp {
            background-color: #f4f4f4;
            color: #333;
        }

        .title {
            text-align: center;
            font-size: 36px;
            font-weight: 600;
            color: #1f77b4;
        }

        .uploaded-file {
            border-radius: 10px;
            background: #fff;
            padding: 15px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
        }

        .stButton>button {
            border-radius: 8px;
            padding: 8px 16px;
            background-color: #1f77b4;
            color: white;
            border: none;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.3s ease-in-out;
        }
        
        .stButton>button:hover {
            background-color: #135e96;
            transform: scale(1.05);
        }

        .dataframe {
            border-radius: 10px;
            overflow: hidden;
        }

        .stCheckbox>label {
            font-weight: 600;
            color: #1f77b4;
        }
        
    </style>
""", unsafe_allow_html=True)

# Set up App Title
st.markdown('<h1 class="title">Data Sweeper</h1>', unsafe_allow_html=True)
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload Your Files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read file based on extension
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine="openpyxl")  # ✅ Explicit engine for xlsx
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error reading file {file.name}: {str(e)}")
            continue

        # Display file info
        file_size_kb = file.getbuffer().nbytes / 1024
        st.markdown(f"""
            <div class="uploaded-file">
                <h3>📁 File Name: {file.name}</h3>
                <p>📏 File Size: {file_size_kb:.2f} KB</p>
            </div>
        """, unsafe_allow_html=True)

        # Show preview of the DataFrame
        st.write("### Preview of the Data:")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🛠 Data Cleaning Options")
        if st.checkbox(f"✨ Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🧹 Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates Removed!")

            with col2:
                if st.button(f"🔍 Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing Values Filled!")

            # Choose Specific Columns to Keep
            st.subheader("📌 Select Columns to Keep")
            selected_columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
            df = df[selected_columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"📈 Show Visualization for {file.name}"):
            numeric_df = df.select_dtypes(include="number")
            if not numeric_df.empty:
                st.bar_chart(numeric_df.iloc[:, :3])  # Limit to 3 columns
            else:
                st.write("❌ No numeric data available for visualization.")

        # Conversion Options
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        buffer = BytesIO()

        if st.button(f"💾 Convert {file.name}"):
            try:
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    new_file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"

                elif conversion_type == "Excel":
                    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:  # ✅ Use Explicit `xlsxwriter`
                        df.to_excel(writer, index=False, sheet_name="Sheet1")
                        writer.close()

                    new_file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)

                # Download Button
                st.download_button(
                    label=f"⬇️ Download {new_file_name}",
                    data=buffer,
                    file_name=new_file_name,
                    mime=mime_type
                )
            except Exception as e:
                st.error(f"Error during conversion: {str(e)}")

st.success("🎉 All files processed!")

import streamlit as st
from PIL import Image
import pandas as pd
import os

# -----------------------------
# Load CSS from images folder
# -----------------------------
def load_css(file_path):
    """Load CSS file for Streamlit app"""
    if os.path.exists(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {file_path}")

load_css("images/style.css")

# -----------------------------
# Load Images safely
# -----------------------------
def load_image(image_path, width=None):
    """Load image and handle missing file"""
    try:
        img = Image.open(image_path)
        return img
    except FileNotFoundError:
        st.warning(f"Image not found: {image_path}")
        return None

# Sidebar logo
logo = load_image("images/logo.png")
if logo:
    st.sidebar.image(logo, width=120)

# -----------------------------
# App title
# -----------------------------
st.title("Student Result App")

# -----------------------------
# Example subjects list
# -----------------------------
subjects = ["Physics", "Computer", "Math", "English", "Chemistry"]

# -----------------------------
# Function to calculate grade
# -----------------------------
def get_grade(marks):
    if marks > 90:
        return "A+"
    elif marks > 80:
        return "A"
    elif marks > 70:
        return "B"
    elif 60 <= marks <= 70:
        return "C"
    else:
        return "F"

# -----------------------------
# Sidebar input for marks
# -----------------------------
st.sidebar.header("Enter Marks")
marks_dict = {}
for subject in subjects:
    marks_dict[subject] = st.sidebar.number_input(
        f"{subject} marks", min_value=0, max_value=100, step=1
    )

# -----------------------------
# Display grades
# -----------------------------
st.header("Grades")
for subject, marks in marks_dict.items():
    st.write(f"{subject}: {marks} → Grade: {get_grade(marks)}")

# -----------------------------
# Load sample student data
# -----------------------------
csv_path = "data/sample_students.csv"
xlsx_path = "data/sample_students.xlsx"

if os.path.exists(csv_path):
    df_csv = pd.read_csv(csv_path)
    st.subheader("CSV Student Data")
    st.dataframe(df_csv)
else:
    st.info(f"No CSV data found at {csv_path}")

if os.path.exists(xlsx_path):
    df_xlsx = pd.read_excel(xlsx_path)
    st.subheader("Excel Student Data")
    st.dataframe(df_xlsx)
else:
    st.info(f"No Excel data found at {xlsx_path}")

# -----------------------------
# Extra images for navigation or UI
# -----------------------------
home_icon = load_image("images/home.png", width=50)
add_icon = load_image("images/add.png", width=50)
results_icon = load_image("images/results.png", width=50)
about_icon = load_image("images/about.png", width=50)
student_icon = load_image("images/student_icon.png", width=50)

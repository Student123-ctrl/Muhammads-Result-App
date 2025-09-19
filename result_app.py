import streamlit as st
import pandas as pd
import os

# ========== CONFIG ==========
ASSETS_DIR = "assets"
if not os.path.exists(ASSETS_DIR):
    os.makedirs(ASSETS_DIR)

LOGO = os.path.join(ASSETS_DIR, "student_icon.png")
HOME_ICON = os.path.join(ASSETS_DIR, "home.png")
ADD_ICON = os.path.join(ASSETS_DIR, "add.png")
RESULTS_ICON = os.path.join(ASSETS_DIR, "results.png")
ABOUT_ICON = os.path.join(ASSETS_DIR, "about.png")

# ========== HELPER FUNCTIONS ==========
def calculate_results(df):
    subjects = [col for col in df.columns if col not in ["Name", "Roll No"]]
    df["Total Marks"] = df[subjects].sum(axis=1)
    df["Percentage"] = (df["Total Marks"] / (len(subjects) * 100)) * 100
    df["Grade"] = df["Percentage"].apply(get_grade)
    return df

def get_grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 80:
        return "A"
    elif pct >= 70:
        return "B"
    elif pct >= 60:
        return "C"
    elif pct >= 50:
        return "D"
    else:
        return "F"

# In-memory student list
if "students" not in st.session_state:
    st.session_state["students"] = []

# ========== SIDEBAR ==========
st.sidebar.image(LOGO, width=120)
menu = st.sidebar.radio(
    "🎓 Menu",
    ["Home", "Add Student", "Results", "About"],
    format_func=lambda x: f"🏠 {x}" if x == "Home" else
                         f"➕ {x}" if x == "Add Student" else
                         f"📊 {x}" if x == "Results" else
                         f"ℹ️ {x}"
)

# ========== PAGES ==========
if menu == "Home":
    st.image(HOME_ICON, width=100)
    st.title("🎓 Student Result Management System")
    st.write("Manage students, add marks, calculate grades, and upload CSV/Excel files.")

elif menu == "Add Student":
    st.image(ADD_ICON, width=100)
    st.title("➕ Add Student")

    with st.form("add_student_form"):
        name = st.text_input("Student Name")
        roll = st.text_input("Roll No")
        physics = st.number_input("Physics", 0, 100, 0)
        math = st.number_input("Math", 0, 100, 0)
        chemistry = st.number_input("Chemistry", 0, 100, 0)
        english = st.number_input("English", 0, 100, 0)
        cs = st.number_input("Computer Science", 0, 100, 0)
        submit = st.form_submit_button("Add Student")

    if submit:
        st.session_state["students"].append({
            "Name": name,
            "Roll No": roll,
            "Physics": physics,
            "Math": math,
            "Chemistry": chemistry,
            "English": english,
            "Computer Science": cs
        })
        st.success(f"✅ Student {name} added successfully!")

elif menu == "Results":
    st.image(RESULTS_ICON, width=100)
    st.title("📊 All Students Results")

    # Upload file
    uploaded_file = st.file_uploader("📂 Upload Student Data (CSV/Excel)", type=["csv", "xlsx"])
    df_uploaded = None

    if uploaded_file is not None:
        try:
            uploaded_file.seek(0)
            if uploaded_file.name.endswith(".csv"):
                df_uploaded = pd.read_csv(uploaded_file, on_bad_lines="skip")
            elif uploaded_file.name.endswith(".xlsx"):
                df_uploaded = pd.read_excel(uploaded_file)
            st.success("✅ File uploaded successfully!")
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")

    # Merge manual + uploaded
    if st.session_state["students"]:
        df_manual = pd.DataFrame(st.session_state["students"])
    else:
        df_manual = pd.DataFrame()

    if df_uploaded is not None and not df_uploaded.empty:
        df_all = pd.concat([df_manual, df_uploaded], ignore_index=True)
    else:
        df_all = df_manual

    if not df_all.empty:
        df_all = calculate_results(df_all)
        st.dataframe(df_all)
    else:
        st.warning("⚠️ No student data available. Add students or upload a file.")

elif menu == "About":
    st.image(ABOUT_ICON, width=100)
    st.title("ℹ️ About")
    st.write("""
    This is a Student Result Management System built with Streamlit.  
    - Add students manually  
    - Upload CSV/XLSX files  
    - View results with grades and percentages  
    """)

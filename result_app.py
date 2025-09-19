import streamlit as st

# ---------------------------
# App Config & Branding
# ---------------------------
st.set_page_config(page_title="Student Result Management", page_icon="🎓", layout="centered")

# Logo + Title
st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=100)  # logo link
st.title("🎓 Student Result Management System")
st.markdown("Manage unlimited students, calculate grades & view results instantly!")

# ---------------------------
# Subjects
# ---------------------------
subjects = ["Physics", "Computer", "Math", "English", "Chemistry"]

# ---------------------------
# Grade Function
# ---------------------------
def get_grade(percentage):
    if percentage > 90:
        return "A+"
    elif percentage > 81:
        return "A"
    elif percentage >= 71:
        return "B+"
    elif percentage >= 61:
        return "B"
    elif percentage >= 51:
        return "C+"
    elif percentage >= 41:
        return "C"
    elif percentage >= 31:
        return "D+"
    elif percentage >= 21:
        return "E+"
    else:
        return "Fail"

# ---------------------------
# Session Storage
# ---------------------------
if "students" not in st.session_state:
    st.session_state.students = {}

# ---------------------------
# Add Students
# ---------------------------
st.subheader("➕ Add Student")

with st.form("student_form", clear_on_submit=True):
    name = st.text_input("Enter Student Name:")
    marks_dict = {}
    if name:
        for subject in subjects:
            marks = st.number_input(
                f"{subject} Marks (0-100)",
                min_value=0, max_value=100, step=1, key=f"{name}_{subject}"
            )
            marks_dict[subject] = marks
    submitted = st.form_submit_button("Add Student")
    if submitted and name:
        st.session_state.students[name] = marks_dict
        st.success(f"✅ {name}'s record added!")

# ---------------------------
# Show Results
# ---------------------------
if st.button("📊 Show All Results"):
    if not st.session_state.students:
        st.warning("No students added yet!")
    else:
        st.subheader("All Students Results")
        for name, marks_dict in st.session_state.students.items():
            total = sum(marks_dict.values())
            percentage = (total / (len(subjects) * 100)) * 100
            grade = get_grade(percentage)

            with st.expander(f"📖 Result of {name}"):
                st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=60)  # student icon
                st.write(f"**Total Marks:** {total}/{len(subjects)*100}")
                st.write(f"**Percentage:** {percentage:.2f}%")
                st.write(f"**Grade:** {grade}")
                st.markdown("**Subject-wise Marks:**")
                for subject, marks in marks_dict.items():
                    st.write(f"- {subject}: {marks}")

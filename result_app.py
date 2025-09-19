import streamlit as st

# Subjects list
subjects = ["Physics", "Computer", "Math", "English", "Chemistry"]

# Function to calculate grade
def get_grade(percentage):
    if percentage > 90:
        return "A+"
    elif percentage > 81:
        return "A"
    elif  percentage >= 71:
        return "B+"
    elif  percentage >= 61:
        return "B"
    elif  percentage >= 51:
        return "C+"
    elif percentage >= 41:
        return "C"
    elif percentage >= 31:
        return "D+"
    elif percentage >= 21:
        return "E+"
    else:
        return "Fail"

# Title
st.title("🎓 Student Result Management System")

students = {}

# Input for 5 students
for i in range(5):
    name = st.text_input(f"Enter name of student {i+1}:", key=f"name{i}")
    if name:
        students[name] = {}
        for subject in subjects:
            marks = st.number_input(
                f"Enter marks for {subject} (0-100) for {name}:",
                min_value=0, max_value=100, step=1, key=f"{name}_{subject}"
            )
            students[name][subject] = marks

# Button to calculate results
if st.button("Show Results"):
    st.subheader(" RESULTS")
    
    for name, marks_dict in students.items():
        if not marks_dict:  # skip empty entries
            continue
        st.write(f"### Student: {name}")
        total = sum(marks_dict.values())
        
        # Show subject-wise marks
        for subject, marks in marks_dict.items():
            st.write(f"{subject}: {marks}")
        
        # Calculate percentage
        percentage = (total / 500) * 100
        grade = get_grade(percentage)
        
        st.write(f"**Total:** {total}/500")
        st.write(f"**Percentage:** {percentage:.2f}%")
        st.write(f"**Grade:** {grade}")

        st.markdown("---")


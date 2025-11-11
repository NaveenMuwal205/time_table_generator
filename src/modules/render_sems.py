import streamlit as st
from src.storage.course_list import (
    courses,
    bca_specializations,
    mtech_specializations,
    mca_specializations,
    btech_specializations,
)


def choose_course() -> list:
    selectCourses = st.multiselect("Select Courses", courses)
    return selectCourses


def render_semesters(course: str, num_semesters: int, key_prefix: str) -> list:
    """Always display semesters vertically"""
    semesters = list(range(1, num_semesters + 1))
    selected_semesters = []

    # Show all semesters vertically with uniform labels
    for j, sem in enumerate(semesters):
        checked = st.checkbox(
            f"Semester {sem}",
            value=True,
            key=f"{key_prefix}_sem_{j}"
        )
        if checked:
            selected_semesters.append(sem)

    return selected_semesters


def select_specialization_and_semesters() -> dict:
    selected_courses = choose_course()
    course_data = {}

    for i, course in enumerate(selected_courses):
        with st.expander(f"📘 {course}", expanded=False):

            # --- Specializations ---
            match course:
                case "B.Tech":
                    specs = st.multiselect(
                        "B.Tech Specializations",
                        btech_specializations,
                        key=f"btech_specs_{i}"
                    )
                    num_semesters = 8
                case "M.Tech":
                    specs = st.multiselect(
                        "M.Tech Specializations",
                        mtech_specializations,
                        key=f"mtech_specs_{i}"
                    )
                    num_semesters = 4
                case "BCA":
                    specs = st.multiselect(
                        "BCA Specializations",
                        bca_specializations,
                        key=f"bca_specs_{i}"
                    )
                    num_semesters = 6
                case "MCA":
                    specs = st.multiselect(
                        "MCA Specializations",
                        mca_specializations,
                        key=f"mca_specs_{i}"
                    )
                    num_semesters = 6
                case _:
                    specs = []
                    num_semesters = 0

            # --- Semesters section ---
            if specs:
                st.markdown("---")
                st.markdown(
                    f"<div class='course-title'>{course} Semesters</div>",
                    unsafe_allow_html=True
                )
                selected_semesters = render_semesters(course, num_semesters, f"{course}_{i}")

                course_data[course] = {
                    "specializations": specs,
                    "semesters": selected_semesters
                }

            st.markdown("</div>", unsafe_allow_html=True)

    # --- Add Preloaded Template button ---
    st.markdown("---")
    if st.button("➕ Add Preloaded Template", use_container_width=True):
        if course_data:
            st.success("Templates Generated!")
            st.write("### Selected Configuration:")
            for course, data in course_data.items():
                st.write(f"**{course}**")
                st.write(f"• Specializations: {', '.join(data['specializations'])}")
                st.write(f"• Semesters: {', '.join(map(str, data['semesters']))}")

            # 👉 store in session_state for sidebar
            st.session_state["generated_classes"] = []
            for course, data in course_data.items():
                for spec in data["specializations"]:
                    for sem in data["semesters"]:
                        st.session_state["generated_classes"].append(f"{course} {spec} Sem {sem}")

        else:
            st.warning("⚠️ Please select at least one course and specialization before adding a template.")

    return course_data

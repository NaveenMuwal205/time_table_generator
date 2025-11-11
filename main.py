import streamlit as st
from src.configs.markdowns import init_md
from src.modules.editable_tables import class_tables
from src.modules.left_slider import slider
from src.modules.render_sems import select_specialization_and_semesters

st.set_page_config(layout="wide")


def page_title():
    st.markdown(
        "<h1 style='margin-bottom:1.5rem;'>AI-BASED Timetable Generator</h1>",
        unsafe_allow_html=True
    )

def main():
    init_md()
    page_title()
    select_specialization_and_semesters()
    slider()
    class_tables()
    st.markdown("<div style='height:300px;'></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

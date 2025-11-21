import streamlit as st
from src.configs.markdowns import init_md
from src.components.left_slider import slider

st.set_page_config(layout="wide")


def page_title():
    st.markdown(
        "<h1 style='margin-bottom:1.5rem;'>AI-BASED Timetable Generator</h1>",
        unsafe_allow_html=True
    )

def main():
    init_md()
    page_title()
    slider("SmartMatrix AI", {
    "B.Tech": ["GEN", "AI", "CY", "CE", "EE", "ME"],
    "M.Tech": ["GEN", "AI", "CY", "CE", "EE", "ME"],
    "BCA": ["GEN", "AI", "CY"],
    "MCA": ["GEN", "AI", "CY"]
})
    st.markdown("<div style='height:300px;'></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

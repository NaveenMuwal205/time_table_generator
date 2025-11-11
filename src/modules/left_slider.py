import streamlit as st

def slider():
    st.sidebar.header("Classes")
    if "generated_classes" in st.session_state and st.session_state["generated_classes"]:
        for cls in st.session_state["generated_classes"]:
            st.sidebar.write(f"• {cls}")
    else:
        st.sidebar.caption("No classes generated yet.")

import streamlit as st

def init_md():
    # --- Page setup ---
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # --- Unified styling ---
    st.markdown("""
    <style>
    /* ========== GENERAL LAYOUT ========== */
    .block-container {
        padding: 1rem 3rem 2rem 3rem;
        max-width: 100%;
    }

    /* ========== COURSE CARDS ========== */
    .course-card {
        background-color: #111418;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.08);
    }

    .course-title {
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        color: #cde9f3;
    }

    /* Multiselect width control */
    div[data-baseweb="select"] {
        width: 300px !important;
        max-width: 320px !important;
        display: inline-block !important;
        vertical-align: middle !important;
    }


    /* ========== MULTISELECT + CHECKBOXES ========== */
    [data-baseweb="select"] {
        background-color: #191d22 !important;
        border-radius: 6px !important;
        border: 1px solid rgba(0,255,255,0.25) !important;
    }

    div[data-testid="column"] {
        padding: 0px !important;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 0.2rem !important;
    }

    /* ========== BUTTONS ========== */
    button[kind="primary"] {
        background: linear-gradient(90deg, #00bcd4, #0097a7) !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        transition: 0.2s ease-in-out;
    }
    button[kind="primary"]:hover {
        background: linear-gradient(90deg, #26c6da, #00acc1) !important;
        transform: scale(1.02);
    }

    /* ========== EXPANDERS ========== */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        font-size: 1rem !important;
        color: #80deea !important;
    }

    /* ========== TITLES ========== */
    h1, h2, h3, h4, h5 {
        color: #b2ebf2;
    }

    /* Remove scrollbar edge glow on dark themes */
    ::-webkit-scrollbar-thumb {
        background-color: #00acc1;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

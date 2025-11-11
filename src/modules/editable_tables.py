import streamlit as st
import pandas as pd

def class_tables():
    st.title("🧾 Editable Class Table Demo")

    # Random sample data
    data = {
        "Student Name": ["Aarav", "Riya", "Kabir", "Meera", "Dev"],
        "Subject": ["Math", "Physics", "Chemistry", "Biology", "English"],
        "Attendance (%)": [92, 88, 95, 80, 97],
        "Mar"
        ""
        "ks": [85, 90, 78, 88, 92],
    }

    df = pd.DataFrame(data)

    st.markdown("### ✏️ Edit any value below:")
    edited_df = st.data_editor(
        df,
        num_rows="dynamic",  # allows adding/removing rows
        use_container_width=True,
        key="editable_table_demo"
    )

    st.markdown("### ✅ Final Table (after edits):")
    st.dataframe(edited_df, use_container_width=True)
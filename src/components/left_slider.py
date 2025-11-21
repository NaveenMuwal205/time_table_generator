from streamlit import sidebar

def slider(title: str, obj: dict):
    sidebar.title(title)
    courses = obj.keys()

    options = ["AI", "GEN", "CY", "EE", "ME", "CE"]
    selected = []

    # 4 columns in one row (inside sidebar)
    col1, col2, col3, col4 = sidebar.columns(4)

    for i, opt in enumerate(options):
        # divide options across columns
        if i % 4 == 0:
            if col1.checkbox(opt):
                selected.append(opt)
        elif i % 4 == 1:
            if col2.checkbox(opt):
                selected.append(opt)
        elif i % 4 == 2:
            if col3.checkbox(opt):
                selected.append(opt)
        else:
            if col4.checkbox(opt):
                selected.append(opt)

    return selected


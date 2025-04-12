import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

st.markdown(" # 🧮  Arithmetic  Calculator", unsafe_allow_html=True)

if "expression" not in st.session_state:
    st.session_state.expression = ""
if "result" not in st.session_state:
    st.session_state.result = ""

buttons = [
    ["7", "8", "9", "➗"],
    ["4", "5", "6", "✖️"],
    ["1", "2", "3", "➖"],
    ["0", ".", "=", "➕"],
    ["🧹", "⌫"]
]

def evaluate_expression():
    try:
        # Replace icons with actual operators
        expression = st.session_state.expression.replace("➗", "/").replace("✖️", "*").replace("➖", "-").replace("➕", "+")
        st.session_state.result = str(eval(expression))
    except ZeroDivisionError:
        st.session_state.result = "Error: Division by zero"
    except Exception as e:
        st.session_state.result = f"Error: {str(e)}"

def handle_click(btn):
    if btn == "🧹":
        st.session_state.expression = ""
        st.session_state.result = ""
    elif btn == "⌫":
        st.session_state.expression = st.session_state.expression[:-1]
    elif btn == "=":
        evaluate_expression()
    else:
        st.session_state.expression += btn

# UI styling
button_styles = {
    "number": "background-color:#f1f3f4; color:black; font-size:18px; border-radius:12px; padding:10px 16px;",
    "operator": "background-color:#ffcc80; color:black; font-size:18px; border-radius:12px; padding:10px 16px;",
    "control": "background-color:#ff6f61; color:white; font-size:18px; border-radius:12px; padding:10px 16px;"
}

for row in buttons:
    cols = st.columns(len(row), gap="small")
    for i, btn in enumerate(row):
        if btn in ["+", "-", "*", "/", "➗", "✖️", "➖", "➕"]:
            style = button_styles["operator"]
        elif btn in ["🧹", "⌫", "="]:
            style = button_styles["control"]
        else:
            style = button_styles["number"]

        if cols[i].button(f"{btn}", key=f"btn_{btn}"):
            handle_click(btn)

# Expression input
st.markdown("### ✏️ Expression")
st.text_input("Expression", value=st.session_state.expression, key="keyboard_input", disabled=False, label_visibility="collapsed")

# Result display
st.markdown("### ✅ Result")
st.code(st.session_state.result if st.session_state.result else "...", language="python")
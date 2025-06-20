import streamlit as st
from datetime import datetime
import functions


todos = functions.get_todos()

def add_todo():
    task = st.session_state["new_todo"].strip()
    if not task:
        return

    if any(task.lower() == t.strip().lower() for t in todos):
        st.warning("Schedule/task added already!")
    else:
        todos.append(task + "\n")
        functions.write_todos(todos)
        st.success("Task added!")

    st.session_state["new_todo"] = ""  # Clear input box



# Custom CSS to reduce spacing
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        .stMarkdown, .stTextInput, .stButton {
            margin-bottom: 0.3rem;
        }
        .subtitle {
            margin-top: 1rem;
            font-size: 25px;
            margin-bottom: 0.2rem;
        }
        .instruction {
            font-style: italic;
            margin-top: -5px;
            font-size: 16px;
        }
    </style>
    """, unsafe_allow_html=True)



# Title
st.title("Daily Task Manager 📝")


# Get current date and time
today = datetime.now().strftime('%A, %d %B %Y, %I:%M %p')
st.markdown(
    f"""
    <div style="text-align: right; text-decoration = underline; color: gray; font-size: 20px;">
        📅 Today is: {today}
    </div>
    """,
    unsafe_allow_html=True
)

# Subtitle
st.markdown("<div class='subtitle'>Stay ahead of your daily schedule with our Daily Task Manager.</div>",
            unsafe_allow_html=True)


st.write("----- ✍🏻 NOTE: Tick the checkbox ✔ to complete and delete a schedule/task. -----")
st.write("")

st.markdown(f"**🧮 You have `{len(todos)}` tasks for today.**")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()

st.text_input(label="", placeholder="Add schedule or task ....", on_change=add_todo, key='new_todo')





















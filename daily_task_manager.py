import streamlit as st
from datetime import datetime



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

# Right-aligned date

# Title
st.title("Daily Task Manager")


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
st.markdown("<div class='subtitle'>Stay ahead of your daily schedule with our Daily Task Manager</div>",
            unsafe_allow_html=True)

# Instruction
st.markdown("<div class='instruction'>Enter your daily schedule below with the box provided!</div>",
            unsafe_allow_html=True)

st.info("NOTE: Check the checkbox to mark any schedule completed and deleted from the list")



st.text_input(label=" ", placeholder="Add schedule or task ....")












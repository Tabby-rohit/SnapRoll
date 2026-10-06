import streamlit as st
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen 
from src.screens.home_page import home_page

def main():
    if "login-type" not in st.session_state:
        st.session_state["login-type"] = None

    match st.session_state["login-type"]:
        case "teacher":
            teacher_screen()
            
        case "student":
            student_screen()
        case None:
            home_page()
main()                     
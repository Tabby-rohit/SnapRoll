import streamlit as st
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.home_header import header_home
def home_page():
    style_base_layout()
    style_background_home()
    header_home()
    col1,col2=st.columns(2)
    with col1:
        if st.button("student"):
            print("student")
            st.session_state["login-type"]="student"
            st.rerun()
    with col2:    
        if st.button("teacher"):
            print("teacher")
            st.session_state["login-type"]="teacher"
            st.rerun()
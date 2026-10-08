from pathlib import Path
import streamlit as st
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.home_header import header_home



def home_page():
    style_base_layout()
    style_background_home()
    header_home()
    col1,col2=st.columns(2)
    with col1:
        st.header("Student Login")
        if st.button("Student Portal",type="primary",icon=":material/arrow_outward:",icon_position="right"):
            # print("student")
            st.session_state["login-type"]="student"
            st.rerun()
    with col2:
        st.header("Teacher Login")    
        if st.button("Teacher Portal",type="primary",icon=":material/arrow_outward:",icon_position="right"):
            # print("teacher")
            st.session_state["login-type"]="teacher"
            st.rerun()
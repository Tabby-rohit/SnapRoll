import streamlit as st
def home_page():
    st.header("home") 
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
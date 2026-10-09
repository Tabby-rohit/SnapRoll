import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
def teacher_screen():
    style_base_layout()
    style_background_dashboard()
    if "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()     

def teacher_screen_login():
    c1,c2=st.columns(2)
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home",shortcut="control+backspace"):
            st.session_state['login-type']=None 
            st.rerun()  

    st.header("Login Using Password",text_alignment="center") 
    st.space()

    teacher_username=st.text_input("Enter username")
    teacher_password=st.text_input("Enter password",type="password")
    st.divider()
    btnc1,btnc2=st.columns(2)
    with btnc1:
        st.button("Login",icon=":material/passkey:",shortcut="control+enter",width="stretch")
    with btnc2:
        if st.button("Register Instead",icon=":material/passkey:",type="primary",width="stretch"):
            st.session_state.teacher_login_type="register" 
            st.rerun()

def teacher_screen_register(): 
    c1,c2=st.columns(2)
    with c1:
            header_dashboard()
    with c2:
            if st.button("Go back to home",shortcut="control+backspace"):
                st.session_state['login-type']=None   
    
    st.header("Register Your Teacher Profile")
    st.space()

    teacher_username=st.text_input("Enter Username")
    teacher_username=st.text_input("Enter Name")
    teacher_password=st.text_input("Enter Password",type="password")
    teacher_password_confirm=st.text_input("Confirm Password",type="password")
    st.divider()
    btnc1,btnc2=st.columns(2)
    with btnc1:
        st.button("Register",icon=":material/passkey:",type="secondary",width="stretch",shortcut="control+enter") 
       
    with btnc2:
        if st.button("Login Instead",type="primary",icon=":material/passkey:",width="stretch"):
            st.session_state.teacher_login_type="login" 
            st.rerun() 
           


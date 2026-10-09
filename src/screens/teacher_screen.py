import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.database.db import check_teacher_exist,create_teacher,teacher_login
def teacher_screen():
    style_base_layout()
    style_background_dashboard()
    if "teacher_data" in st.session_state:
        teacher_dashboard()
    
    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()     
    
def teacher_dashboard():
    teacher_data=st.session_state.teacher_data
    st.header(f"Welcome {teacher_data["name"]}")

def login_teacher(username,password):
    if not username or not password:
        return False
    teacher=teacher_login(username,password)
    if teacher:
        st.session_state.user_role="teacher"
        st.session_state.teacher_data= teacher
        st.session_state.is_logged_in=True
        return True


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
        if st.button("Login",icon=":material/passkey:",shortcut="control+enter",width="stretch"):
            if login_teacher(teacher_username,teacher_password):
                st.toast("welcome back")
                import time
                time.sleep(2)
                st.rerun()
            else:
                st.error("invalid username or password")    
    with btnc2:
        if st.button("Register Instead",icon=":material/passkey:",type="primary",width="stretch"):
            st.session_state.teacher_login_type="register" 
            st.rerun()

def register_teacher(teacher_username,teacher_name,teacher_password,teacher_password_confirm):
    if not teacher_username or not teacher_name or not teacher_password or not teacher_password_confirm:
        return False,"ALL Fields are required !"
    if check_teacher_exist(teacher_username):
        return False,"Usaer already exists"
    if teacher_password_confirm!=teacher_password:
        return False,"Confirm password must match password"
    try:
        create_teacher(teacher_username,teacher_password,teacher_name)
        return True,"Succesfull Registration now you can login"
    except Exception as e:
        return False,e

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
    teacher_name=st.text_input("Enter Name")
    teacher_password=st.text_input("Enter Password",type="password")
    teacher_password_confirm=st.text_input("Confirm Password",type="password")
    st.divider()
    btnc1,btnc2=st.columns(2)
    with btnc1:
        if st.button("Register Now",icon=":material/passkey:",type="secondary",width="stretch",shortcut="control+enter"):
            success,message=register_teacher(teacher_username,teacher_name,teacher_password,teacher_password_confirm) 
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type="login"
                st.rerun()
            else:
                st.error(message)    
    with btnc2:
        if st.button("Login Instead",type="primary",icon=":material/passkey:",width="stretch"):
            st.session_state.teacher_login_type="login" 
            st.rerun() 
           


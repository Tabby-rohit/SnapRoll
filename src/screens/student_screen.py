import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from PIL import Image
import numpy as np
def student_screen():
    style_base_layout()
    style_background_dashboard()
    c1,c2=st.columns(2)
    with c1:
            header_dashboard()
    with c2:
            if st.button("Go back to home",shortcut="control+backspace"):
                st.session_state['login-type']=None 
                st.rerun()  
    
    st.header("Login Using FaceId",text_alignment="center") 

    img=st.camera_input("place your face in this")
    if img:
        imgg=np.array(Image.open(img))
        print(imgg)

    st.space()
    
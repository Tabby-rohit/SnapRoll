import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector=dlib.get_frountal_face_detector()
    sp=dlib.shape_predictor(face_recognition_models.pose_predictor_model_location)
    facerec=dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location)
    return detector,sp,facerec

def get_face_embedings(img_np):
    detector,sp,facerec=load_dlib_models()
    faces=detector(img_np,1)
    encodings=[]
    for face in faces:
        shape=sp(face)
        face_discriptor=facerec(img_np,shape,1) #128 embeddings
        encodings.append(np.array(face_discriptor))
    return encodings


@st.cache_resource
def get_trained_model():
    x=[]
    y=[]

    students=get_all_students()
    if not students:
        return None
    for student in students:
        embedding=student.get("face_embedding")
        if embedding:
            x.append(np.array(embedding))
            y.append(student.get("student_id"))
    if len(x)==0:
        return None
    clf=SVC(kernel="linear",probability=True,class_weight="balanced")
    try:
        clf.fit(x,y)
    except Exception  as e:
        pass

    return {"clf":clf,"x":x,"y":y}


def train_classifier():
    st.cache_resource.clear()
    modeldata=get_trained_model()
    return bool(modeldata)

def pridict_attendence(class_img):
    embeddings=get_face_embedings(class_img)
    detected_students={}

    model=get_trained_model()
    if not model:
        return {},[],0
    clf=model["clf"]
    x=model["x"]
    y=model["y"]
    all_students=sorted(list(set(y)))
    for embedding in embeddings:
        if len(all_students)>=2:
            predicted_id=int(clf.predict(embedding))
        else:
            predicted_id=int(all_students[0])
        student_embedding=x[y.index(predicted_id)] 
        best_match_score= np.linalg.norm(student_embedding-embedding)
        resemblance_threshhold=0.6
        if best_match_score<=resemblance_threshhold:
            detected_students["predicted_id"]=True
    return detected_students,all_students,len(embeddings) 
   







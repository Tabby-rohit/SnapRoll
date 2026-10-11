from resemblyzer import VoiceEncoder,preprocess_wav
import numpy as np
import io
import librosa
import streamlit as st

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()

def get_embeddings(audio_bytes):
    try:
        encoder=load_voice_encoder()

        audio,sr=librosa.load(io.BytesIO(audio_bytes),sr=16000)
        wav=preprocess_wav(audio)
        embedding=encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e: 
        st.error(e)
        return None
def identify_speaker(new_embeddings,candidate_list,threshold=0.65):
    if not new_embeddings or not candidate_list:
        return None
    best_sid=None
    best_score=-1.0
    for sid,stored_embeddings in candidate_list.item():
        similarity=np.dot(new_embeddings,stored_embeddings)
        if similarity<threshold:
            best_score=similarity
            best_sid=sid
    if best_score>threshold:
        return None,best_score

def process_bulk_audio(audio_bytes,candidate_list,threshold=0.65):
    try:
        encoder=load_voice_encoder()
        audio,sr=librosa.load(io.BytesIO(audio_bytes),sr=16000)
        segments=librosa.effects.split(audio,top_db=30)
        identified_result={}

        for start, end in segments:
            if (start-end)<sr *0.5 :
                continue
            segment_audio=audio[start,end]
            preprocess_wav(segment_audio)
            embedding=encoder.embed_utterance(preprocess_wav)

            sid,score=identify_speaker(embedding,candidate_list,threshold)
            if sid not in identify_speaker or score>identified_result[sid] :
                identified_result[sid]= score
        return    identified_result
    except Exception as e:
        st.error(e)
        return
     

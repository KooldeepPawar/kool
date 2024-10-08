
import streamlit as st 
from googletrans import Translator

def language_translator() :

    trans = Translator()

    st.title("Welcome to Traslator module")
    txt = st.text_area("Enter Text to be converted","Enter Text")

    Langauges = ['Hindi','Marathi']
    choice = st.selectbox("Langauges",Langauges)

    if choice=="Hindi" :
        st.write("Check below the transalation in Hindi")
        Result = trans.translate(txt,dest='hi')
        st.write(Result.text)
    elif choice=="Marathi"    :
        st.write("Check below the transalation in Marathi")
        Result = trans.translate(txt,dest='mr')
        st.write(Result.text)

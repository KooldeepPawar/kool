import streamlit as st 
# from googletrans import Translator
import pandas as pd 

import language
import qrcode_generation
    
menu = ['Home','Transalate','QR Code Generation','About']

choice = st.sidebar.selectbox("Options",menu)

if choice == "Home" :
    st.title("Welcome, glad to see you!")
    st.subheader("Have a look at the Web Page, now you can quickly transalate any English text to Hindi or Marathi, also you can generate QR code in few seconds")
    st.subheader("Let's start, on the left side choose the option of your choice and proceed")
elif choice == 'Transalate' :
    language.language_translator()
elif choice == "QR Code Generation" :
    qrcode_generation.qrcodegeneration()
elif choice == 'About' :
    st.subheader("This is Kooldeep, thanks please visit again.")
 

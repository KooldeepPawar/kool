import qrcode  as qr
import streamlit as st 


def qrcodegeneration() :
    
    url = st.text_area("Enter Text to be converted","Enter URL for QR Code Generation")

    submittbutton = st.button("Submit") 

    if submittbutton :
        img = qr.make(url)
        img.save("QR_Code.png")
        st.balloons()
        st.image("QR_Code.png")








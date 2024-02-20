from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My webpage",page_icon="☣",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

#loading assets
lottie_coding = load_lottieurl("https://lottie.host/a7cc2ab2-88fc-4a2a-bda7-fd901046b2b2/iiU6BUp5dy.json")
imaage = Image.open("images/coder.png")



# Header section
with st.container():
    st.subheader("Hi, This is a CODER :👋")
    st.title("A Coder from india")
    st.write("I am passionate about reasearching and developing the programs  ")
    st.write("[Learn more](https://www.errormakesclever.com/")

#project
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do ")
        st.write("#")
        st.write("""Simplify the task""")
        st.write("Solve the Coding by Identifiying the error ")
        st.write("Improving my skills to solving the hardtask  ")
    
    
    with right_column:
        st.lottie(lottie_coding , height=300, key="coding")

# Project
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column , text_column = st.columns((1,2))

    with image_column:
        #images
        st.image(imaage)


        with text_column:
            st.subheader("Debug the Program")
            st.write("""In this video am show how to identify and solve the errors  """)
            st.markdown("[Watch video ...] (https://www.youtube.com/watch?v=YJsqKbqgpEY)")

with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        #image should be inserted #st.image(variable name )

        


#contact
        with st.container():
            st.write("---")
            st.header("Get in touch with my Codes")
            st.write("Interested can fill the from to attend the program  ")
            st.write("---")

contact_form ="""<form action="https://formsubmit.co/dineshad1803@gmail.com" method="POST">
     <input type ="hidden" name = "_captcha" value="false">
     <input type="text" name="name" placeholder ="your name " required>
     <input type="email" name="email" placeholder ="Your email" required>
     <input type="number" Number="Number" placeholder="Your mobile number" required>
     <textarea name ="message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""

left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
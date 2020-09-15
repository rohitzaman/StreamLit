import streamlit as st

#text/title
st.title("Rohit Zaman")

#header
st.header("Rohit Zaman")

#subheader
st.subheader("Rohit Zaman")

#text
st.text("Rohit Zaman")

#markdown
st.markdown("###Rohit Zaman")

#colorful text
st.success("Rohit Zaman")
st.info("Rohit Zaman")
st.warning("Rohit Zaman")
st.error("Rohit Zaman")

#help
st.help(range)

#writing text
st.write("Rohit Zaman")

#image
from PIL import Image
img=Image.open("example.jpeg")
st.image(img,width=300,caption="Rohit Zaman")

#video
vid_file = open("rohit.mp4","rb").read()
st.video(vid_file)

#checkbox
if st.checkbox("show/hide"):
	st.text("rohit zaman")

#radio
status = st.radio("what is your status",("active","inactive"))

if status == "Active" :
	st.success("you are active")
else:
	st.warning("inactive")



#slectbox
occupation = st.selectbox("Your occupation",["a","b","c"])
st.write("you have selected this option ",occupation)


#multiselect
loaction = st.multiselect("where do you work?",("a","b","c"))
st.write("you have selected",len(location),"loactions")


#slider
age = st.slider("what is your level",1,5)

#button
st.button("simple button")

if st.button("rohit"):
	st.text("rohit is cool")

#text input
firstname = st.text_input("enter your name","Type here..")

if st.button("submit"):
	result = firstname.title()
	st.success(result)


#text area
msg = st.text_area("enter your msg","Type here..")

if st.button("submit"):
	result = msg.title()
	st.success(result)

#raw code
st.text("text")
st.code("code")


#multiple code
with st.echo():
	#comment
	import pandas as pd
	df = pd.dataFrame()



#sidebars
st.sidebar.header("about")
st.sidebar.text("hi this is rohit")


#num_input
st.number_input("number of rows to view",5,10)
st.dataframe(df.head(number))



if st.checkbox("summary"):
	st.write(df.describe().T)

#username and password
username = st.text_input("enter username")
password = st.text_input("enter password",type="password")
	
	




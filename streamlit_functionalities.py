
import pandas as pd
import numpy as np
import streamlit as st #importing the streamlit library already installed 
import matplotlib.pyplot as plt

st.title("Hello Streamlit")  # title for the webapp
st.write("Welcome here")  # st.write() acts like print()

x = st.slider("Select a number :",0,100,50)  #this prints a slider with range(1,100), by default the slider
#points at 50
st.write("You selected : ", x)

"""
now, to create a text-box for input, we use st.text_input() function
"""

name = st.text_input("Enter your name : ")

#button 
if st.button("Submit"):   #this crreates a button called "Submit"
    st.write(f"Hello {name}!")
    
#slider
age = st.slider("select your age :", 18,90,21)    
st.write(f"Your age is {age}")


data = pd.DataFrame({
    'category' : ['A','B','C','D'],
    'value' : [10,20,15,25]})

st.write("Here is a table of data :")
st.write(data)
         
fig,ax = plt.subplots()
ax.bar(data["category"], data["value"])
st.pyplot(fig)  #this creates a figure of plot!

selection = st.radio("Choose option : ", [1,2,3,4,5,6,7])  # this creates radio buttons for each option
st.write("You chose : ", selection )


option = st.selectbox("Choose among : ", [1,2,3,4,5])  # this creates a drop down list of options to choose from 
st.write("You chose : ", option)

date = st.date_input("select a date : ")  # this lets users pick a date
st.write(date)

time = st.time_input("select a time : ")  # this lets users pick a time (24-hour format)
st.write(time)

uploaded_file = st.file_uploader("Choose a file", type = "xlsx")
if uploaded_file is not None :
    df = pd.read_excel(uploaded_file)
    st.write(df)
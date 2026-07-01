import streamlit as st

st.title("Country chooser")

v1 = st.number_input("enter your budget")
v2 = st.slider("enter the  distance you wanna go")
v3 = st.multiselect("enter your purpose (Job,Study,Vacation,Relocation):")

if not v3:
    st.write("Please select at least one purpose")
if v3:
    st.write(f"Great you selected: {v3}")
st.button("find country")

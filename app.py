
import streamlit as st
import json

st.title("Country chooser")

v1 = st.number_input("Enter your budget")
v2 = st.slider("Enter the distance you want to go")
v3 = st.multiselect(
    "Enter your purpose:",
    ["Job", "Study", "Vacation", "Relocation"]
)

if not v3:
    st.write("Please select at least one purpose")
else:
    st.write(f"Great! You selected: {v3}")

st.button("Find country")

with open("countries.json") as file:
    countries = json.load(file)

st.write(countries)

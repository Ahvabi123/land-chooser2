import streamlit as st
import json

with open("countries.json") as file:
    countries = json.load(file)
st.title("Country Chooser")

v1 = st.number_input("Enter your budget (€)")
v2 = st.slider("Enter the maximum flight time (hours)")
v3 = st.multiselect(
    "Enter your purpose:",
    ["Work", "Study", "Vacation", "Relocation"]
)

if not v3:
    st.write("Please select at least one purpose.")
else:
    st.write(f"Great! You selected: {v3}")

if st.button("Find Country"):
 st.write("Button works!")
 for country in countries:
    if v1 >= country["recommended_budget"]:
      if v2 >= country["flight_time"]:
            st.write(country["name"])

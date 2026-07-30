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
 results = []
 for country in countries:
     score = 0

     if v1 >= country["recommended_budget"]:
         score += 40

     if v2 >= country["flight_time"]:
         score += 30

     for purpose in v3:
         if purpose in country["purpose"]:
             score += 30
             break

     results.append({
         "name": country["name"],
         "score": score,
         "budget": country["recommended_budget"],
         "flight": country["flight_time"],
         "purpose": country["purpose"]
     })

 sorted_results = sorted(
     results,
     key=lambda resul: resul["score"],
     reverse=True
 )

 for index, result in enumerate(sorted_results):

    if index == 0:
        st.success(f"🥇 Best Match: {result['name']}")
    else:
        st.subheader(f"🌍 {result['name']}")

    st.write(f"⭐ Score: {result['score']}/100")
    st.write(f"💰 Budget: €{result['budget']}")
    st.write(f"✈️ Flight: {result['flight']} hours")
    st.write(f"🎯 Purpose: {', '.join(result['purpose'])}")


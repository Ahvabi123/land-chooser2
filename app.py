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
    "score": score
})
     sorted_results = sorted(
         results,
         key=lambda country: country["score"],
         reverse=True
     )

     st.write(sorted_results)
     st.write(f"🌍 Country: {country['name']}")
     st.write(f"💰 Recommended Budget: €{country['recommended_budget']}")
     st.write(f"✈️ Flight Time: {country['flight_time']} hours")
     st.write(f"🎯 Purposes: {', '.join(country['purpose'])}")

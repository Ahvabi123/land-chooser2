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

        # Budget
        if v1 >= country["recommended_budget"]:
            score += 40

        # Flight time
        if v2 >= country["flight_time"]:
            score += 30

        # Purpose
        for purpose in v3:
            if purpose in country["purposes"]:
                score += 30
                break

        results.append({
            "name": country["name"],
            "flag": country["flag"],
            "continent": country["continent"],
            "rating": country["rating"],
            "score": score,
            "budget": country["recommended_budget"],
            "flight": country["flight_time"],
            "purposes": country["purposes"]
        })

    # Sonuçları puana göre sırala
    sorted_results = sorted(
        results,
        key=lambda resul: result["score"],
        reverse=True
    )

    # İlk 10 sonucu göster
    top10 = sorted_results[:10]

    medals = ["🥇", "🥈", "🥉"]

    for index, result in enumerate(top10):

        if index < 3:
            st.success(f"{medals[index]} #{index+1} {result['flag']} {result['name']}")
        else:
            st.info(f"#{index+1} {result['flag']} {result['name']}")

        st.write(f"⭐ Rating: {result['rating']}/10")
        st.progress(result["score"] / 100)
        st.write(f"🎯 Match Score: {result['score']}/100")
        st.write(f"💰 Estimated Cost: €{result['budget']}")
        st.write(f"✈️ Flight Time: {result['flight']} hours")
        st.write(f"🌍 Continent: {result['continent']}")
        st.write(f"🎯 Purposes: {', '.join(result['purposes'])}")

        st.divider()


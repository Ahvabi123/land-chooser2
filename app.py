import streamlit as st

st.title("Country chooser")

v1 = st.number_input("Enter your budget")
v2 = st.slider("Enter the distance you want to go", min_value=0, max_value=20000)
v3 = st.multiselect(
    "Enter your purpose (Job, Study, Vacation, Relocation):",
    ["Job", "Study", "Vacation", "Relocation"]
)

if not v3:
    st.write("Please select at least one purpose")
else:
    st.write(f"Great, you selected: {v3}")

if st.button("Find country"):
    if not v3:
        st.warning("Please select a purpose first")
    else:
        st.success("Searching for countries...")
        st.write(f"Budget: {v1}")
        st.write(f"Distance: {v2} km")
        st.write(f"Purpose: {v3}")

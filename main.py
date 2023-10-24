import streamlit as st
import Langchain_helper

st.title("Restaurant Name & Menu generator")

st.markdown("Created by **Anitha Kugur**")  # Name of the creator

cuisine = st.sidebar.selectbox("Pick a cuisine", ('Indian', 'American', 'Mexican', 'Chinese', 'Korean', 'Italian'))


if cuisine:
    response = Langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
else:
    st.warning("Please select a cuisine from the sidebar.")


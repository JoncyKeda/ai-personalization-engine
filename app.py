import streamlit as st
from utils.recommender import recommend_items
from utils.user_model import update_user_profile, user_profiles

st.set_page_config(page_title="AI Personalization Engine", layout="wide")

st.title("🎯 AI Personalization Engine")

st.write("This system learns user preferences and provides dynamic recommendations.")

user_id = st.text_input("Enter User ID")
item = st.selectbox("Select Item Interaction", [
    "action_movie", "thriller_movie", "romance_movie",
    "comedy_movie", "horror_movie"
])

if st.button("Update Preference"):
    update_user_profile(user_id, item)
    st.success("✅ User preference updated!")

if st.button("Get Recommendations"):
    recs = recommend_items(user_id)
    st.subheader("📊 Recommended Items")
    st.write(recs)

st.subheader("📁 User Profiles (Debug View)")
st.write(user_profiles)

import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="VerIQ",
    page_icon="🛡️",
    layout="wide"
)

# Header
st.title("🛡️ VerIQ")
st.subheader("The Digital Credibility Platform for Sales Professionals")

# Sidebar
st.sidebar.title("Profile Navigation")
section = st.sidebar.radio(
    "Choose Section",
    [
        "Profile",
        "Experience",
        "Reviews",
        "Achievements",
        "Trust Score"
    ]
)

# Profile Section
if section == "Profile":

    st.header("👤 Sales Professional Profile")

    photo = st.file_uploader(
        "Upload Profile Photo",
        type=["jpg", "jpeg", "png"]
    )

    if photo:
        st.image(photo, width=200)

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    city = st.text_input("Location")

    verified = st.checkbox("Identity Verified")

    st.success("Profile Created Successfully")

# Experience Section
elif section == "Experience":

    st.header("💼 Work Experience")

    company = st.text_input("Company Name")
    role = st.text_input("Designation")
    years = st.slider("Years of Experience", 0, 30, 1)

    st.write("### Previous Companies")

    companies = st.text_area(
        "Enter Previous Companies (one per line)"
    )

    if st.button("Save Experience"):
        st.success("Experience Added")

# Reviews Section
elif section == "Reviews":

    st.header("⭐ Employment Reviews")

    review_rating = st.slider(
        "Rating",
        1,
        5,
        5
    )

    review_text = st.text_area(
        "Employer Review"
    )

    if st.button("Submit Review"):
        st.success("Review Submitted")

# Achievements Section
elif section == "Achievements":

    st.header("🏆 Achievements")

    sales_target = st.number_input(
        "Target Achievement (%)",
        0,
        300,
        100
    )

    certifications = st.text_area(
        "Certifications"
    )

    awards = st.text_area(
        "Awards and Recognition"
    )

    st.balloons()

# Trust Score Section
elif section == "Trust Score":

    st.header("🛡️ VerIQ Trust Score")

    experience = st.slider(
        "Experience Years",
        0,
        30,
        5
    )

    rating = st.slider(
        "Average Rating",
        1.0,
        5.0,
        4.5
    )

    verified = st.checkbox(
        "Verified Professional"
    )

    score = (experience * 20) + (rating * 100)

    if verified:
        score += 200

    score = min(score, 1000)

    st.metric(
        "VerIQ Trust Score",
        int(score)
    )

    st.progress(score / 1000)

    if score > 850:
        st.success("Elite Sales Professional 🏆")
    elif score > 650:
        st.info("Trusted Professional ⭐")
    else:
        st.warning("Building Credibility 📈")
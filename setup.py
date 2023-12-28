
import streamlit as st
import streamlit_helper
import llm_helper

st.title('Company selection!!!')

## st.sidebar.selectbox("pick company type:",("AI", "Big Data", "Machine Learning", "Textile", "Healthcare", "Insurance"))
company = st.sidebar.selectbox("pick company type:",("AI", "Big Data", "Machine Learning", "Textile", "Healthcare", "Insurance"))


if company:
    #response = streamlit_helper.generate_company_name_location(company)
    response = llm_helper.get_company_name_and_location(company)
    st.header(response['company_nm'].strip())
    locations = response['locations_details'].strip().split(",")
    st.write("**** Company Name****")
    for location in locations:
        st.write("-", location)
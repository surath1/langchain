import streamlit as st
st.title('Suggest Company')

## st.sidebar.selectbox("pick company type:",("AI", "Big Data", "Machine Learning", "Textile", "Healthcare", "Insurance"))
company = st.sidebar.selectbox("pick company type:",("AI", "Big Data", "Machine Learning", "Textile", "Healthcare", "Insurance"))

def generate_company_name_location(company):
    return {
        'company_nm' : 'ABC',
        'company_location' : 'BLR, AUL, CTC'
    }


if company:
    response = generate_company_name_location(company)
    st.header(response['company_nm'])
    locations = response['company_location'].split(",")
    st.write("**** Company Name****")
    for location in locations:
        st.write("-", location)
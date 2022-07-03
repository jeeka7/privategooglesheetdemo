import streamlit as st
import gspread

#st.write(st.secrets)


service_account = gspread.service_account_from_dict(st.secrets["gcp_service_account"])

st.write(st.secrets.keys())

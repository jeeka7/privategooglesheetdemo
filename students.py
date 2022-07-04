import streamlit as st
import gspread
import pandas as pd

st.write(st.secrets)


service_account = gspread.service_account_from_dict(st.secrets["gcp_service_account"])

st.write(st.secrets["private_gsheets_url"])

sht = service_account.open_by_url(st.secrets["private_gsheets_url"])


wks = sht.worksheet(students)

get_values = wks.get_all_values()

df= pd.DataFrame(get_values)

st.write(get_values)

import streamlit as st
import gspread

sa = gspread.service_account()
sh = sa.open("tutionmanagement")

wks = sh.worksheet("student")

st.title(" Tution management ")

st.write('Rows: ', wks.row_count)
st.write('Cols: ', wks.col_count)


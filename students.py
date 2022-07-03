import streamlit as st
import gspread

#st.write(st.secrets)


service_account = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
#sh = sa.open("tutionmanagement")

#wks = sh.worksheet("student")

#st.title(" Tution management ")

#st.write('Rows: ', wks.row_count)
#st.write('Cols: ', wks.col_count)


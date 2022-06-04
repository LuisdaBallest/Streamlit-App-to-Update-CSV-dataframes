import pandas as pd
import streamlit as st

st.title('App')
st.header('Current Data')

# First you'll need to upload a local CSV file, since I'll use the App to save simple Client data my columns are:
# 'Name', 'Last Name', 'Age', 'Date'
uploaded_file = st.file_uploader("Open a CSV file.")

if uploaded_file is not None:
     # Here 'uploaded_file.name' will give us a string with the file's Name
     # The CSV file should be saved where the streamlit environment is installed
     path = uploaded_file.name    

#Read the CSV file using pandas, and write it on Streamlit
df = pd.read_csv(path)
st.write(df)

#Sidebar
st.sidebar.header('Options')
options_form=st.sidebar.form('options_form')
name=options_form.text_input('Name')
last_name=options_form.text_input('Last Name')
age=options_form.number_input('Age',step=1)
date=options_form.date_input('Date')

#Submit button to add new data to our CSV file and update the CSV file
add_data=options_form.form_submit_button()
if add_data:
    new_data={"Name":name,'Last Name':last_name,'Age':int(age),'Date':date}
    df=df.append(new_data,ignore_index=True)
    df.to_csv(path,index=False)

#Create a download button to save the dataframe as a CSV file
@st.cache
def convert_df(dat):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return dat.to_csv().encode('utf-8')

csv = convert_df(df)
st.download_button(
     label="Download as CSV",
     data=csv,
     file_name='Clientes.csv',
     mime='text/csv',
 )


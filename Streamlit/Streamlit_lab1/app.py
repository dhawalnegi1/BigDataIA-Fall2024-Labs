import streamlit as st
import numpy as np
import pandas as pd

# How to display on streamlit page
st.write("Hello world")

# #Input data
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")

if st.button("Full Name"):
    st.write("Full Name:", first_name + " " + last_name)


if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

# How to input data and access it
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

# change session state var
def change_name(name):
    st.session_state['name'] = name

st.button('Change Name', on_click=change_name, args=['Jane Doe'])



# st.button("Reset", type="primary")




chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)


import streamlit as st
import numpy as np
import pandas as pd

def form_page():
    col1,col2 = st.columns([1,2])
    col1.title('Sum:')

    with st.form('addition'):
        a = st.number_input('a')
        b = st.number_input('b')
        submit = st.form_submit_button('add')

    if submit:
        col2.title(f'{a+b:.2f}')

def login_page():
    st.title('LOGIN')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if username == "bigdata" and password == "bigdata":
            st.write("Login Successful")
            st.session_state['page'] = 'form'
            st.rerun()

    if st.button('File Upload Page'):
        if username == "bigdata" and password == "bigdata":
            st.write("Login Successful")
            st.session_state['page'] = 'file_upload'
            st.rerun()

def file_upload_demo():
    st.title('File Uploader')
    uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True)

    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)


def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'login'
    if st.session_state['page'] == 'login':
        login_page()
    elif st.session_state['page'] == 'form':
        form_page()
    elif st.session_state['page'] == 'file_upload':
        file_upload_demo()


if __name__ == '__main__':
    main()

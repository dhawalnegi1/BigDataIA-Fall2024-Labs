import streamlit as st
from request import request_1, request_2

from admin import admin_1, admin_2

# Initialize role in session state
if "role" not in st.session_state:
    st.session_state.role = None

# Define available roles
ROLES = [None, "Requester", "Admin"]

# Function for login
def login():
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.experimental_rerun()

# Function for logout
def logout():
    st.session_state.role = None
    st.rerun()

# Main application
def main():
    st.title("Request Manager App")

    # If not logged in, show the login page
    if st.session_state.role is None:
        login()
    else:
        # Display logout button and navigation options
        st.sidebar.title("Navigation")
        st.sidebar.button("Log out", on_click=logout)

        # Depending on the role, show the appropriate pages
        if st.session_state.role == "Requester":
            page = st.sidebar.selectbox("Select Request Page", ["Request 1", "Request 2"])
            if page == "Request 1":
                request_1.app()  # Call the function in request_1.py
            elif page == "Request 2":
                request_2.app()  # Call the function in request_2.py


        elif st.session_state.role == "Admin":
            page = st.sidebar.selectbox("Select Admin Page", ["Admin 1", "Admin 2"])
            if page == "Admin 1":
                admin_1.app()  # Call the function in admin_1.py
            elif page == "Admin 2":
                admin_2.app()  # Call the function in admin_2.py

if __name__ == "__main__":
    main()

# app.py - Streamlit Temple Room Booking System

import streamlit as st
from datetime import date

def main():
    st.title('Temple Room Booking System')

    # Room selection
    st.header("Room Booking")
    room_options = ['Room 1', 'Room 2', 'Room 3']
    selected_room = st.selectbox("Select a Room", room_options)

    # Date selection
    booking_date = st.date_input("Select Booking Date", min_value=date.today())

    # User details
    st.header("Your Details")
    user_name = st.text_input("Your Name")
    contact_info = st.text_input("Contact Information")

    # Booking confirmation
    if st.button("Book Room"):
        if user_name and contact_info:
            st.success(f"Booking confirmed for {selected_room} on {booking_date} by {user_name}. Contact Info: {contact_info}")
        else:
            st.error("Please fill in your name and contact information.")

if __name__ == '__main__':
    main()

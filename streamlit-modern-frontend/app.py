import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

if 'current_donation' not in st.session_state:
    st.session_state['current_donation'] = 0  # Starting donation amount

# Function to create a simple bar graph for donation goal
def create_donation_graph(current_amount, goal_amount):
    fig, ax = plt.subplots()
    ax.barh(['Goal'], [goal_amount], color='gray')
    ax.barh(['Donations'], [current_amount], color='blue')
    ax.set_xlim(0, max(goal_amount, current_amount) * 1.1)

    for i in ax.patches:
        ax.text(i.get_width()+5, i.get_y()+0.2, 
                str(round((i.get_width()), 2)), 
                fontsize=10, fontweight='bold',
                color='grey')
    return fig

# Function to update donation amount
def update_donation(amount):
    st.session_state['current_donation'] += amount

# Function to render the 'Home' page
def home_page():
    st.title('Temple ERP System - Home')
    temple_image_url = 'https://images.unsplash.com/photo-1554554497-0095c34db3ec?q=80&w=2610&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'  # Replace with your image path or URL
    st.image(temple_image_url, caption='Our Temple', width=300)
    st.header('Make a Donation')

    donation_options = [10, 50, 100, 500, 'Other']
    donation_amount = st.radio("Select donation amount ($):", donation_options)

    if donation_amount == 'Other':
        donation_amount = st.number_input("Enter your donation amount ($):", min_value=0.0, step=0.01)

    if st.button('Donate'):
        update_donation(donation_amount)
        st.success(f'Thank you for your donation of ${donation_amount}!')

    st.header('Daily Donation Goal')
    daily_goal = 1000  # Example daily goal
    st.pyplot(create_donation_graph(st.session_state['current_donation'], daily_goal))

# Function to render the 'About Us' page
def about_us_page():
    st.title('About Us')
    st.write("""
    ## Our Vision
    At the heart of our ancient temple, tradition meets technology. 
    In a world rapidly embracing the digital era, our dream is to bring 
    our cherished temple into the forefront of this revolution.

    ## Our Journey
    Digitalizing the age-old practices, rituals, and administrative tasks 
    of our temple is not just an upgrade—it's a renaissance. We are 
    committed to preserving our heritage while making our operations 
    more efficient, transparent, and accessible to devotees worldwide.

    ## Join Us
    Be a part of our journey as we blend the wisdom of the past with 
    the innovations of the future, creating a unique spiritual experience 
    that transcends boundaries and time.
    """)

# Function to render the 'Donations' page
def donations_page():
    st.title('Donations with Blockchain Technology')
    st.write("""
    In our temple ERP system, we leverage blockchain technology, specifically ResDB, 
    to ensure the transparency and security of donations. 
    Blockchain allows us to verify each transaction independently and maintain 
    a tamper-proof record of all donations made.
    """)

# Function to generate random footfall data
def generate_footfall(date):
    base_footfall = 200
    if date.weekday() >= 5:  # Weekend
        return int(base_footfall * 1.5)  # 50% more footfall on weekends
    return base_footfall

# Function to render the 'Prediction' page
def prediction_page():
    st.title('Footfall Prediction')
    selected_date = st.date_input("Select a Date for Prediction")
    if st.button('Predict'):
        predicted_footfall = generate_footfall(selected_date)
        st.write(f"Predicted footfall on {selected_date}: {predicted_footfall}")

# Function to render the 'Data Gathering' page
def data_gathering_page():
    st.title('Data Gathering')
    date = st.date_input("Date")
    footfall = st.number_input("Footfall", min_value=0)
    if st.button('Submit Data'):
        st.success(f"Data for {date} with footfall {footfall} has been recorded.")

# Function to render the 'Special Donations' page
def special_donations_page():
    st.title('Special Donations')
    st.write("""
    Our temple offers special donation packages for large contributions. 
    These donations come with benefits like special access to events, 
    personalized thank you messages, and more.
    """)

    # Input for selecting donation amount
    donation_amount = st.number_input("Enter your donation amount ($):", min_value=0.0, step=0.01)

    # Text area for special request
    special_request = st.text_area("Enter your special request (optional):")

    if st.button('Donate'):
        st.success(f"Thank you for your donation of ${donation_amount}!")
        if special_request:
            st.write(f"Your special request: '{special_request}' will be considered.")

# Main function to control page rendering
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ('Home', 'About Us', 'Donations', 'Prediction', 'Data Gathering', 'Special Donations'))

    if page == 'Home':
        home_page()
    elif page == 'About Us':
        about_us_page()
    elif page == 'Donations':
        donations_page()
    elif page == 'Prediction':
        prediction_page()
    elif page == 'Data Gathering':
        data_gathering_page()
    elif page == 'Special Donations':
        special_donations_page()

if __name__ == "__main__":
    main()

import streamlit as st
import datetime
import DatabaseManager
from PIL import Image

st.set_page_config(page_title="Hotel Booking", page_icon=":office:")

st.title('Welcome to Four Seasons Hotel')
st.write("The Four Seasons Hotel offers luxurious guest rooms, elegant dining options, a fitness center, "
         "spa, and indoor pool. Perfect choice for a memorable stay.")
st.write("---")

one = st.empty()
two = st.empty()
three = st.empty()


def main():
    with one.container():
        st.header('Enter Details Below')
        col1, col2 = st.columns([1, 0.5])
        date = datetime.datetime.now().date()
        with col1:
            st.write('Enter Check-in and Check-out date')
        with col2:
            st.button(f"Today's Date 🗓️ {date}")

        col5, col6 = st.columns(2)
        with col5:
            checkin = st.date_input('Enter Check-in Date🗓️')
        with col6:
            checkout = st.date_input('Enter Check-out Date🗓️')

        cname = st.text_input('Enter Your Full Name')
        cage = int(st.number_input('Enter Your Age', step=1))
        aadhar = st.text_input('Enter your SSN/Aadhaar')
        phone = st.text_input('Enter your phone number')
        caddress = st.text_area('Enter Your Address')

        if st.button('Submit'):
            if checkin > checkout:
                st.error('Check-out cannot be before check-in')
                flag = 1
            try:
                int(aadhar.replace(' ', ''))
            except ValueError:
                st.error('(SSN/Aadhaar) cannot have letters')
                flag = 1
            else:
                aadhar = int(aadhar.replace(' ', ''))
            if cage < 18:
                st.error('You need to be an adult to book a hotel room')
                flag = 1
            if len(phone) != 10:
                st.error('Phone Number must be 10 digits')
                flag = 1
            try:
                int(phone)
            except ValueError:
                st.error('Phone Number cannot have letters')
                flag = 1
            else:
                phone = int(phone)
            if flag == 0:
                st.success('Details Saved')

            if roomtypeid < 1 or roomtypeid > 5:
                st.error('Room Does Not Exist')
                flag = 1
            try:
                int(roomtypeid)
            except ValueError:
                st.error('Room Number cannot have letters')
                flag = 1
            else:
                roomtypeid = int(roomtypeid)
            if flag == 0:
                totalprice = DatabaseManager.selectRoom(roomtypeid, checkin, checkout)
                cid = DatabaseManager.addCustDetails(aadhar, cname, cage, phone, caddress, totalprice, checkin,
                                                     checkout)
                end(cid, checkin, checkout)


def end(cid, checkin, checkout):
    with three.container():
        one.empty()
        two.empty()
        row = DatabaseManager.getCustDetails(cid)
        st.success('Booking Confirmed')
        st.write(f'Customer ID: {cid}')
        st.write(f'Customer Name: {row[2]}')
        st.write(f'Customer Aadhaar: {row[1]}')
        st.write(f'Check In: {checkin}')
        st.write(f'Check Out: {checkout}')
        st.write(f'Customer Phone Number: {row[4]}')
        st.write(f'Room Amount: {row[6]}')
        st.info('Bill will be due after your Stay')


main()

# D Hostel Room Booking System Prototype for AMBPPCT

Welcome to the D Hostel Room Booking System Prototype for AMBPPCT. This system is designed to provide accommodation facilities at Meherabad for Baba-lovers on pilgrimage. The application allows users to select a room, provide their details, and confirm their booking. The application integrates with a MySQL database to store and retrieve customer and room information.

## Features

1. Welcome message and description of the accommodation facilities at Meherabad.
2. User input for check-in and check-out dates, full name, age, SSN/Aadhaar, phone number, and address.
3. Display of available rooms with their details, including room number, description, number of beds, air conditioning availability, and price.
4. Selection of a room by entering the room number.
5. Validation of user input for date, age, SSN/Aadhaar, and phone number.
6. Confirmation of the booking with the customer details and room information.
7. Display of the customer ID, name, SSN/Aadhaar, check-in and check-out dates, phone number, and room amount.
8. Information about the bill payment due after the stay.

### Database Tables

The application utilizes the following database tables:

- `customerdetails`: Stores customer information including the customer ID, Aadhaar/SSN, name, age, phone number, address, final price, check-in date, and check-out date.
- `room`: Represents the hostel rooms with room number, room type ID, and size.
- `roomtype`: Contains details about room types, such as room type ID, number of beds, air conditioning availability, rate, and description.
- `roomservice`: Manages room service orders with order ID, item ID, quantity, and customer ID.
- `items`: Stores information about available items for room service, including item ID, item name, and rate.
- `bookingdetails`: Tracks the booking details with booking ID, customer ID, check-in date, check-out date, and final price.
- `employees`: Keeps records of hostel employees with employee ID, Aadhaar/SSN, name, age, gender, role ID, and salary.
- `roles`: Contains information about employee roles with role ID, role name, and salary.

### Backend Functionality Features for Staff

The application provides the following backend functionality for staff members:

1. Get Price to Pay at Check Out: Allows the management staff to calculate and display the amount to be paid by a customer at check-out. The staff needs to enter the customer ID, and upon submission, the application retrieves the final amount from the database and displays it. It also updates the booking details with the customer ID and the final amount.
2. Add Room Service Ticket: Enables the management staff to add a new room service ticket for a customer. The staff needs to enter the item ID, quantity, and customer ID. Upon clicking the "Add Ticket" button, the application adds the room service ticket to the database and displays a success message.
3. List of Items: Displays a table containing the details of all available items for room service. The information includes the item ID, item name, and rate.
4. List of Employees: Shows a table containing the details of all employees working at the hostel. The information includes the employee ID, SSN/Aadhaar, full name, age, gender, role ID, and salary.
5. List of Employee Roles: Displays a table containing the details of all employee roles. The information includes the role ID, role name, and base salary.
6. List of Rooms: Shows a table containing the details of all rooms in the hostel. The information includes the room number, room type ID, and size.
7. List of Room Types: Displays a table containing the details of all room types available in the hostel. The information includes the room type ID, number of beds, air conditioning availability, nightly rate, and room description.
8. List of Bookings: Shows a table containing the details of all bookings made at the hostel. The information includes the booking ID, customer ID, check-in date, check-out date, and final price.
9. List of Customers: Displays a table containing the details of all customers who have booked a room. The information includes the customer ID, SSN/Aadhaar, full name, age, phone number, and address.
10. List of Orders: Shows a table containing the details of all room service orders placed by customers. The information includes the order ID, item ID, quantity, and customer ID.

## Environment Setup

To set up the environment and run the application with MongoDB, follow these steps:

1. Install Python: Make sure Python is installed on your system. You can download it from the official Python website.
2. Install Streamlit: Open the command prompt and run the following command to install Streamlit:
   ```
   pip install streamlit
   ```
3. Install PyMongo: Run the following command to install the PyMongo library for MongoDB integration:
   ```
   pip install pymongo
   ```
4. Set up MongoDB Server: Install and configure MongoDB on your system. Make sure it is running.
5. Set up the Database: Create a new database in MongoDB and define the necessary collections and documents.
6. Update Database Connection Details: Open the `DatabaseManager.py` module and update the database connection details with your MongoDB server information.
7. Run the Application: Open the command prompt, navigate to the directory where the `Main_Page.py` file is located, and run the following command:
   ```
   streamlit run Main_Page.py
   ```

Note: Make sure the MongoDB server is running and the database connection details are correctly set in the `DatabaseManager.py` module before running the application.

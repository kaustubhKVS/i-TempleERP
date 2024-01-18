    # with two.container():
    #     st.write("---")
    #     st.header('Select Room')

    #     with st.container():
    #         col1, col2 = st.columns([0.5, 1])
    #         row = DatabaseManager.getRoomType(1)
    #         with col1:
    #             image1 = Image.open('Images\Room1.jpg')
    #             st.image(image1)
    #         with col2:
    #             st.write(f'Room Number: {row[0]}')
    #             st.write(f'Description: {row[4]}')
    #             st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
    #             st.write(f'Air Conditioning: {row[2]}')
    #             st.write(f'Price: {row[3]}')
    #             st.write("---")
    #     with st.container():
    #         col3, col4 = st.columns([0.5, 1])
    #         row = DatabaseManager.getRoomType(2)
    #         with col3:
    #             image1 = Image.open('Images\Room2.jpg')
    #             st.image(image1)
    #         with col4:
    #             st.write(f'Room Number: {row[0]}')
    #             st.write(f'Description: {row[4]}')
    #             st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
    #             st.write(f'Air Conditioning: {row[2]}')
    #             st.write(f'Price: {row[3]}')
    #             st.write("---")

    #     with st.container():
    #         col5, col6 = st.columns([0.5, 1])
    #         row = DatabaseManager.getRoomType(3)
    #         with col5:
    #             image1 = Image.open('Images\Room3.jpg')
    #             st.image(image1)
    #         with col6:
    #             st.write(f'Room Number: {row[0]}')
    #             st.write(f'Description: {row[4]}')
    #             st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
    #             st.write(f'Air Conditioning: {row[2]}')
    #             st.write(f'Price: {row[3]}')
    #             st.write("---")

    #     with st.container():
    #         col7, col8 = st.columns([0.5, 1])
    #         row = DatabaseManager.getRoomType(4)
    #         with col7:
    #             image1 = Image.open('Images\Room4.jpg')
    #             st.image(image1)
    #         with col8:
    #             st.write(f'Room Number: {row[0]}')
    #             st.write(f'Description: {row[4]}')
    #             st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
    #             st.write(f'Air Conditioning: {row[2]}')
    #             st.write(f'Price: {row[3]}')
    #             st.write("---")

    #     with st.container():
    #         col9, col10 = st.columns([0.5, 1])
    #         row = DatabaseManager.getRoomType(5)
    #         with col9:
    #             image1 = Image.open('Images\Room5.jpg')
    #             st.image(image1)
    #         with col10:
    #             st.write(f'Room Number: {row[0]}')
    #             st.write(f'Description: {row[4]}')
    #             st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
    #             st.write(f'Air Conditioning: {row[2]}')
    #             st.write(f'Price: {row[3]}')
    #             st.write("---")

    #     roomtypeid = st.number_input('Select Room Number', step=1)
    #     flag = 0
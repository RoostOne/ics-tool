from Calendar.Calendar import Calendar;
import streamlit as st
import pandas as pd

# function for creating a streamlit app with a table and a headline 
def create_app():
    calendar = Calendar()

    # Read the Streamlit_Intro.md and display it
    with open("Streamlit_Intro.md", "r") as f:
        st.markdown(f.read())

    # File Uploader 
    st.subheader("Upload a CSV file")
        # Add a button to upload a csv file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    # event when the file is uploaded
    if uploaded_file is not None:
        # read the csv file into a Calendar object
        # path of uploaded file
        calendar.from_csv(uploaded_file)

        # Calendar to dataframe Date; Start Time; End Time; Title; Location
        df_import = calendar.to_df()
        # show the dataframe in the edited_df 1^

        st.write(df_import)

        # create ics file to download
        calendar = Calendar()
        calendar.from_df(df_import)
        
        st.write("Calendar created successfully")


        st.subheader("Create a  ical Calendar")
        st.write("Click the button below to create a calendar from the table above. The calendar will be saved as 'calendar.ics' in the download directory.")

        
        hello = calendar.to_ics()
        # st download with examaple hellor world file
        st.download_button(
            label="Download ",
            data=hello,
            file_name="calendar.ics",
            mime="text/plain",
        )





def main():

    create_app()
    # Create a calendar
    calendar = Calendar()
    
    # Create a calendar based on the csv file
    # calendar.from_csv("calendar.csv")

    #Create a ics file from the calendar
    # calendar.to_ics("calendar.ics")


if __name__ == "__main__":
    main()


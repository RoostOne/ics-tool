from Calendar.Calendar import Calendar;
import streamlit as st
import pandas as pd

# function for creating a streamlit app with a table and a headline 
def create_app():
    st.title("Calendar")

    # add a dataframe with initial calendar information
    # Create an initial DataFrame with calendar information
    data = {
        "Date": ["20.05.2024", "21.05.2024", "22.05.2024"],
        "Start Time": ["09:00", "10:00", "11:00"],
        "End Time": ["10:00", "11:00", "12:00"],
        "Title": ["Meeting", "Deadline", "Team Building Event"],
        "Location": ["Office", "Home", "Park"]
    }
    df = pd.DataFrame(data)

    # make the dataframe editable
    st.write("Calendar Information")
    edited_df = st.data_editor(df, num_rows="dynamic")

    # add a button to create an ics file
    if st.button("Create Calendar"):
        calendar = Calendar()
        calendar.from_df(edited_df)
        
        calendar.to_ics("calendar.ics")
        st.write("Calendar created successfully")



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


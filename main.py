import streamlit as st
import pandas as pd
import os

# check if file exists if not create it
if not os.path.exists("Rooms.csv"):
    df=pd.DataFrame(columns=["Name","Email","Phone","Room Type","Check In Date","Check Out Date","Check In Status"])
    df.to_csv("Rooms.csv",index=False)  

Room=pd.read_csv("Rooms.csv")

if "show_check_in_form" not in st.session_state:
    st.session_state.show_check_in_form = False

if "show_check_out_form" not in st.session_state:
    st.session_state.show_check_out_form = False

if "view_data" not in st.session_state:
    st.session_state.view_data=False

if "toast_message" not in st.session_state:
    st.session_state.toast_message = None


st.set_page_config(page_title="LuxeStay Managment",layout="wide")

if st.session_state.toast_message:
    st.toast(st.session_state.toast_message)
    st.session_state.toast_message = None
st.header("LuxeStay Managment")
st.write("Welcome to the LuxeStay Management System.")
st.write(" ")
st.write(" ")



col1,col2,col3,col4=st.columns(4)


#Check In form
with col1:
    CheckIn = st.button("Check In",use_container_width=True)
    if CheckIn:
        st.session_state.show_check_in_form = True
        st.session_state.view_data=False
        st.session_state.show_check_out_form=False


with col2:
    CheckOut = st.button("Check Out",use_container_width=True)
    if CheckOut:
        st.session_state.show_check_out_form = True
        st.session_state.view_data=False
        st.session_state.show_check_in_form = False

# View all data
with col3:
    view = st.button("View All Data",use_container_width=True)
if view:
    st.session_state.show_check_in_form=False
    st.session_state.show_check_out_form=False
    st.session_state.view_data=True




# Data viewing session code
if st.session_state.view_data:
    st.subheader("All Guests and Tourists.")
    st.dataframe(Room)





#check In form Data ----- can be put anywhere
if st.session_state.show_check_in_form:
        with  st.form("Check In Form"):
            # take input from user
            st.subheader("Check In Form")
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            room_type = st.selectbox("Room Type",["Single","Double","Suite"])
            check_in_date = st.date_input("Check In Date")
            check_out_date = st.date_input("Check Out Date")
            Checkinstatus = True
            st.markdown("### Check In Status: :green[Checking In]")
            

            st.write("Data saved to database.")
            submit= st.form_submit_button("Submit")
            if submit:
                data={"Name":name,"Email":email,"Phone":phone,"Room Type":room_type,"Check In Date":check_in_date,"Check Out Date":check_out_date,"Check In Status":Checkinstatus}
                df=pd.DataFrame(data,index=[0])
                df.to_csv("Rooms.csv",mode="a",index=False,header=False)

                st.session_state.show_check_in_form = False
                st.session_state.toast_message = "Tourist Successfully Checked In."
                st.rerun()



# # Check out form data
# if st.session_state.show_form:





# how to do that when anyothr button is pushed the alrady one auto disappears

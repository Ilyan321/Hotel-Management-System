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

if "Search" not in st.session_state:
    st.session_state.Search=False

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
st.write("")
st.write(" ")
st.write("")
st.markdown("##### LuxeStay Management System is designed to streamline hotel operations, enhance guest experiences, and optimize resource management. With features like check-in/check-out management, real-time room availability tracking, and comprehensive guest profiles, our system empowers hotel staff to deliver exceptional service while maximizing efficiency. Whether you're a small boutique hotel or a large resort, LuxeStay Management System is your trusted partner in hospitality excellence.")
st.write("")
st.write(" ")
st.write("")
st.write(" ")
st.write("")
st.write(" ")

st.header("Additional Services")
col_kitchen,col_laundry=st.columns(2)
with col_kitchen:
    with st.container(border=True,height=170):
        st.subheader("Kitchen Management")
        st.write("Efficiently manage kitchen operations, track inventory, and ensure timely meal preparation to enhance guest satisfaction.")

with col_laundry:
    with st.container(border=True,height=170):
        st.subheader("Laundry Management")
        st.write("Streamline laundry processes, track linen inventory, and ensure timely service to maintain high standards of cleanliness and guest comfort.")

col_gym,col_pool=st.columns(2)

with col_gym:
    with st.container(border=True,height=170):
        st.subheader("Gym Management")
        st.write("Effectively manage gym facilities, track equipment usage, and provide a seamless experience for fitness-conscious guests.")

with col_pool:
    with st.container(border=True,height=170):
        st.subheader("Pool Management")
        st.write("Optimize pool operations, monitor water quality, and ensure a safe and enjoyable experience for guests seeking relaxation and recreation.")

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
        st.session_state.Search=False


# View all data
with col3:
    view = st.button("View All Data",use_container_width=True)
if view:
    st.session_state.show_check_in_form=False
    st.session_state.show_check_out_form=False
    st.session_state.view_data=True
    st.session_state.Search=False



with col4:
    Search = st.button("Search",use_container_width=True)
if Search:
    st.session_state.show_check_in_form=False
    st.session_state.show_check_out_form=False
    st.session_state.view_data=False
    st.session_state.Search=True


# Extra data


if st.session_state.Search:
    st.subheader("Search for a Guest or tourist.")
    search_query=st.text_input("Search by Name, Email or Phone Number.")
    if search_query:
        search_results=Room[
            (Room["Name"].astype(str).str.contains(search_query,case=False,na=False))|
            (Room["Email"].astype(str).str.contains(search_query,case=False,na=False))|
            (Room["Phone"].astype(str).str.contains(search_query,case=False,na=False))]
        if not search_results.empty:
            st.dataframe(search_results)
        else:
            st.error("No results found.")


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
            

            submit= st.form_submit_button("Submit")
            if submit:
                data={"Name":name,"Email":email,"Phone":phone,"Room Type":room_type,"Check In Date":check_in_date,"Check Out Date":check_out_date,"Check In Status":Checkinstatus}
                df=pd.DataFrame(data,index=[0])
                df.to_csv("Rooms.csv",mode="a",index=False,header=False)

                st.session_state.show_check_in_form = False
                st.session_state.toast_message = "Tourist Successfully Checked In."
                st.rerun()



# # Check out form data

if st.session_state.show_check_out_form:
    with st.form("Check Out Form"):
        st.subheader("Check Out Form")
        name=st.text_input("Enter Name to Check Out")
        submit = st.form_submit_button("Submit")
        if submit:
            if name:
                Room = pd.read_csv("Rooms.csv")
                if name in Room["Name"].values:
                    Room.loc[Room["Name"] == name, "Check In Status"]=False
                    Room.to_csv("Rooms.csv",index=False)
                    st.session_state.show_check_out_form=False
                    st.session_state.toast_message = "Tourist Successfully checked Out."
                    st.rerun()
                else:
                    st.error("No guest found with the provided name.")
            else:
                st.error("Please enter a name.")



st.divider()
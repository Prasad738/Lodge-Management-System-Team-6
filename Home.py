import mysql.connector
import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="",
)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://png.pngtree.com/background/20220718/original/pngtree-lobby-hotel-five-star-picture-image_1662951.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="data4")

mycursor=mydb.cursor()
print("Connection Established")

def Home():
    st.title("Data Phoenix Lodge")
    st.sidebar.header("Home")
    st.write("Welcome to Data Phoenix Lodging, We are looking forward for your visit.")

    st.image("https://media.istockphoto.com/id/104731717/photo/luxury-resort.jpg?s=1024x1024&w=is&k=20&c=lNQVwTuYzo9wQZfZzHioQMCJRTHWVzhX1UXmcqgnF5k=")
    st.subheader("CONTEMPORARY LUXURY IN THE CITY OF DREAMS")
    st.write("Towering above Mumbai’s upscale commercial hub, Data Phoenix combines chic modern style with an intimate, boutique atmosphere and panoramic sea views. Discover our powerhouse collection of dining, spa and swimming experiences. Let our expert team connect you with local culture, shopping and entertainment.")

if __name__ == "__main__":
    Home()

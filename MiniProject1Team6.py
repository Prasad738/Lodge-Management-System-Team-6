import mysql.connector
import streamlit as st

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

# Create Streamlit App
st.set_page_config(
    page_title="Guest",
    page_icon="👋",
)

def admin():
    st.title("Data Phoenix Lodge");
    st.sidebar.success("Select a demo above.")
    st.write("Welcome to Data Phoenix Lodging, We are looking forward for your visit.")
    def home():
        st.image("https://media.istockphoto.com/id/104731717/photo/luxury-resort.jpg?s=1024x1024&w=is&k=20&c=lNQVwTuYzo9wQZfZzHioQMCJRTHWVzhX1UXmcqgnF5k=")
        st.subheader("CONTEMPORARY LUXURY IN THE CITY OF DREAMS")
        st.write("Towering above Mumbai’s upscale commercial hub, Data Phoenix combines chic modern style with an intimate, boutique atmosphere and panoramic sea views. Discover our powerhouse collection of dining, spa and swimming experiences. Let our expert team connect you with local culture, shopping and entertainment.")
    # Display Options for CRUD Operations
    tab1,tab2,tab3 = st.tabs(["Home","Check Records","Force CheckOut"])
    # Perform Selected CRUD Operations
    with tab1:
        home()

    with tab2:
        st.subheader("Check records")
        id1=st.number_input("Enter checkin id",key="15008")
        if st.button("Check"):
            sql2="select a.checkin_id,customer_Name,Moblie_number,id_proof,check_in_date,check_out_date,room_type,rate,num_of_guest,total_bill from checkin a join checkout b on a.checkin_id=b.checkin_id where a.checkin_id=%s"
            val2=(id1,)
            mycursor.execute(sql2,val2)
            res = mycursor.fetchall()
            for row in res:
                st.write("Id -",row[0])
                st.write("Name -",row[1])
                st.write("Contact Number -",row[2])
                st.write("Id Proof -",row[3])
                st.write("CheckIn Date -",row[4])
                st.write("CheckOut Date -",row[5])
                st.write("Room Type -",row[6])
                st.write("Room Rate -",row[7])
                st.write("Number of Guests -",row[8])
                st.write("Total Bill -",row[9])

    with tab3:
        st.subheader("Force CheckOut")
        id2=st.number_input("Enter checkin id",key="15002")
        checkout_date=st.date_input("Enter Check Out Date")
        if st.button("Check Out"):
            sql="insert into checkout(checkin_id,check_out_date) values(%s,%s)"
            val=(id2,checkout_date)
            mycursor.execute(sql,val)
            mydb.commit()

            sql3="select (check_out_date-check_in_date) from checkin a join checkout b on a.checkin_id=b.checkin_id where a.checkin_id = %s;"
            val3=(id2,)
            mycursor.execute(sql3,val3)
            res = mycursor.fetchall()
            for i in res:
                days=i[0]

            sql2="select a.checkin_id,customer_Name,check_in_date,check_out_date,room_type,rate,num_of_guest from checkin a join checkout b on a.checkin_id=b.checkin_id where a.checkin_id=%s"
            val2=(id2,)
            mycursor.execute(sql2,val2)
            res = mycursor.fetchall()
            for row in res:
                st.write("Id -",row[0])
                st.write("Name -",row[1])
                st.write("CheckIn Date -",row[2])
                st.write("CheckOut Date -",row[3])
                st.write("Room Type -",row[4])
                st.write("Room Rate -",row[5])
                st.write("Number of Guests -",row[6])
                x=row[5]*(days)+(row[6]-1)*500
                st.write("Total Bill -",x)

                sql4="update checkout set Total_bill=%s where checkin_id=%s"
                val4=(x,id)
                mycursor.execute(sql4,val4)
                mydb.commit()

            st.success("Check Out Successfully")

st.set_page_config(page_title="Admin", page_icon="📈")
st.sidebar.header("Admin Login")

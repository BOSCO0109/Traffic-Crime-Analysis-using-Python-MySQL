import streamlit as sl
import pandas as ps
from sqlalchemy import create_engine
import mysql.connector as connects
import datetime

sl.set_page_config('Police_arrest_project')

sl.header('Hi There!')
sl.write('_I"m Bosco welcome to the police arrest project_')
Name = sl.text_input('Kindly enter your name')
if Name :
    sl.write(f'_Hi {Name} how is your day hope its goes well lets begin the search_')
    min_value = datetime.date(2020,1,1)
    max_value = datetime.date(2020,2,15)
    stop_date = sl.date_input('Kindly enter the date to find the details',min_value=min_value,max_value=max_value,value=min_value)
    date_formate = stop_date.strftime('%d-%m-%Y')
    time = sl.time_input('Kindly enter the time to find the details',step=datetime.timedelta(minutes=1))
    time_formate = time.strftime('%H:%M:%S')
    country = sl.selectbox('kindly enter the country name to find the details',['Canada','India','USA'])
    gender = sl.selectbox('Kindly enter the gender',['M','F'])
    age = sl.selectbox('kindly select the age of the person',['19','58','76','75','73','70','50','30','21','53','46','25','51','55','71','41','47','59','60','56','61','69','39','23','26','24','64','68','65','67','74','32','28','18','43','48','78','77','22','31','37','35','40','20','63','49','45','38','72','79','36','66','80','44','54','34','29','33','62','27','42','52','57'])
    race = sl.selectbox('Kindly enter the driver race',['Asian','Other','Black','White','Hispanic'])
    search = sl.selectbox('Is the search conduct',[0,1])
    search_type = sl.selectbox('What is the type of search',['Vehicle Search','frisk', None])
    drug = sl.selectbox('Was is drug related case',[0,1])
    stop_duration = sl.selectbox('what is the duration of stop time',['0-15 Min','16-30 Min','30+ Min'])
    number = sl.text_input('Kindly enter the vechile number').upper()


    conn = connects.connect(
        host='localhost',
        user= 'root',
        password = '1234567890',
        database = 'dummy_1'
    )

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM traffic_police_project')
    fetch = cursor.fetchall()

    column = [col[0] for col in cursor.description]
    frame = ps.DataFrame(fetch,columns=column)
    sl.write('Sample data for the database based on this enter the option')
    sl.write(frame.head(1))
    cursor.close()

    options = {'Date': [date_formate],
            'Time' : [time_formate],
            'Country' : [country],
            'Gender' : [gender],
            'Age' : [age],
            'Driver_Race' : [race],
            'Search' : [search],
            'Search_type' : [search_type],
            'Drug' : [drug],
            'Stop_duration' :[stop_duration],
            'Number': [number]}
    select = sl.multiselect('select option',list(options.keys()))


    #This query is used to execute using all the function
    if "Date" in select and 'Time' in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_date = '{date_formate}' and stop_time = '{time_formate}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)    

    elif "Date" in select and 'Country' in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_date = '{date_formate}' and country_name = '{country}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)   

    elif "Date" in select and 'Age' in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_date = '{date_formate}' and driver_age = '{age}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)   

    elif "Date" in select and 'Driver_Race' in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_date = '{date_formate}' and driver_race = '{race}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)   

    elif "Date" in select and 'Search' in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_date = '{date_formate}' and search_conducted = '{search}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)   

    elif "Date" in select and 'Search_type' in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_date = '{date_formate}' and search_type = '{search_type}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)   


    elif "Date" in select and 'Drug' in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_date = '{date_formate}' and drugs_related_stop = '{drug}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)   

    elif "Date" in select and 'Stop_duration' in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_date = '{date_formate}' and stop_duration = '{stop_duration}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)   
    
    elif "Number" in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where vehicle_number = '{number}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)

    elif 'Date' in select:
        conn = connects.connect(
        host='localhost',
        user= 'root',
        password = '1234567890',
        database = 'dummy_1'
    )

        cursor = conn.cursor()
        
        query = f"select * from traffic_police_project where stop_date ='{date_formate}'"
        cursor.execute(query)
        fetch = cursor.fetchall()
        column1 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column1)
        sl.dataframe(frame)


    elif 'Time' in select:
        conn = connects.connect(
        host = 'localhost',
        database = 'dummy_1',    
        password = '1234567890',
        user = 'root'

        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_time ='{time_formate}'"
        cursor.execute(query)
        fetch = cursor.fetchall()
        column1 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column1)
        sl.dataframe(frame)   

    elif 'Country' in select:

        conn = connects.connect(
            database = 'dummy_1',
            user = 'root',
            password = '1234567890',
            host = 'localhost'
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where country_name ='{country}'"
        cursor.execute(query)
        fetch = cursor.fetchall()
        column2 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column2)
        sl.dataframe(frame)

    elif 'Gender' in select:
        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            host = 'localhost',
            user = 'root'

        )

        cursor = conn.cursor()
        query = f'select * from traffic_police_project where driver_gender = "{gender}"'
        cursor.execute(query)
        fetch = cursor.fetchall()
        column = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column)
        sl.dataframe(frame)

    elif 'Age' in select:

        conn = connects.connect(
            host = 'localhost',
            user = 'root',
            password = '1234567890',
            database = 'dummy_1'

        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where driver_age ='{age}'"
        cursor.execute(query)
        fetch = cursor.fetchall()
        column4 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column4)
        sl.dataframe(frame)
    
    elif "Driver_Race" in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where driver_race = '{race}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column)
        sl.dataframe(frame)

    elif "Search" in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where search_conducted = '{search}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column)
        sl.dataframe(frame)

    elif "Search_type" in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where search_type = '{search_type}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)

    elif "Drug" in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where drugs_related_stop = '{drug}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)

    elif "Stop_duration" in select:

        conn = connects.connect(
            database = 'dummy_1',
            password = '1234567890',
            user = 'root',
            host = 'localhost' 
        )

        cursor = conn.cursor()
        query = f"select * from traffic_police_project where stop_duration = '{stop_duration}' "
        cursor.execute(query)
        fetch = cursor.fetchall()
        column5 = [col[0] for col in cursor.description]
        frame = ps.DataFrame(fetch,columns=column5)
        sl.dataframe(frame)

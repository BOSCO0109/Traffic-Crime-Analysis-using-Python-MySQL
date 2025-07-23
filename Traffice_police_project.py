import pandas as ps 
import streamlit as sl
from sqlalchemy import create_engine
import datetime as dt
from datetime import datetime
import mysql.connector as connects

sl.set_page_config('Traffice_police_report')           #This is used to set the name for thewebsite
sl.title('Hi There welcome to my page')                #And this if for the welcome page
name = sl.text_input('_My name is Don what is your_')

if name:                                               #after the user enter his/her is begins
    user_name = sl.write(f'Hi  {name} how are you!')
    start_date = dt.date(2020,1,1)
    end_date = dt.date(2020,2,15)
    stop_date = sl.date_input("Hi There kindly enter the date you want to search",min_value=start_date,max_value=end_date,value=start_date)
    Date_formate = stop_date.strftime('%d-%m-%Y')                   #This is used to change the formate of the date to match the project file
    time = sl.time_input("Hi There kindly enter the time you want to search",step=dt.timedelta(minutes=1))
    Time_formate = time.strftime('%H:%M:%S')                        #This is used to change the formate of the time to match the project file
    country_name= sl.selectbox("Select the country",['Canada','India','USA'])
    Driver_gender = sl.selectbox('select gender',['M','F'])
    Driver_age = sl.selectbox('select the age',['19','58','76','75','73','70','50','30','21','53','46','25','51','55','71','41','47','59','60','56','61','69','39','23','26','24','64','68','65','67','74','32','28','18','43','48','78','77','22','31','37','35','40','20','63','49','45','38','72','79','36','66','80','44','54','34','29','33','62','27','42','52','57'])
    Driver_race = sl.selectbox('select the r=driver race',['Asian','Other','Black','White','Hispanic'])
    search_conduct = sl.selectbox('select any one of the search conduct',['1',"0"])
    search_type = sl.selectbox('select the search type',['Vehicle Search','frisk'])
    Drug_relatad = sl.selectbox('select any one',['1','0'])
    stop_duration = sl.selectbox('select the duration time',['0-15 Min','16-30 Min','30+ Min'])
    vechile_number = sl.text_input('enter the vechile number').upper()

    option = {
        'stop_date' : [Date_formate],
        'stop_time' : [Time_formate],
        'country_name' : [country_name],
        'driver_gender' : [Driver_gender],
        'driver_age' : [Driver_age],
        'driver_race' : [Driver_race],
        'search_conducted' :[search_conduct],
        'search_type' : [search_type],
        'drugs_related_stop' : [Drug_relatad],
        'stop_duration' : [stop_duration],
        'vehicle_number' : [vechile_number]

    }

    multiselect = sl.multiselect("Select the options you want to see in this project",list(option.keys()))  #This is option is used to see specific details of the person

    checkbox = sl.checkbox('click to see the result')
    
    start_time = datetime.now()

    if checkbox:                                                                                  #Connecting my sql using built-in function 
        conn = connects.connect(
            host = 'localhost',
            password = 'password',
            user = 'root',
            database = 'dummy_1'
        )

        A = []                                                                          #This is used to store the column name 
        B = []                                                                           #This is used to store the value of the column 
        

        for i in multiselect:
            value = option[i][0]
            if value:
                A.append(f'{i}=%s')                                                          #The f'{i}=%s' is used to insert the key to mysql without getting error
                B.append(value)

        cursor = conn.cursor()
        query = 'select * from traffic_police_project'
        if A:
            query += ' where ' + ' AND '.join(A)                                              #This function will activate when the value is insert in A function to run the "where" function in mysql database 
            cursor.execute(query,B)                                                            #(query,B) query is used to execute the 'mysql function' and 'B' hold the value of the function
        else:
            cursor.execute(query)
        
        fetch = cursor.fetchall()
        column = [col[0] for col in cursor.description]                                             #This is one line for-loop function this runs as loop of column name and store it in.
        frame = ps.DataFrame(fetch,columns=column)
        sl.dataframe(frame)
        conn.close()
        cursor.close()

        
    end_time = datetime.now()
    result = abs((end_time - start_time).total_seconds())    
    sl.write(f'{result} seconds')
    cursor.close()
    conn.close()
    



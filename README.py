# Traffic-Crime-Analysis-using-Python-MySQL
#This project analyzes traffic stop data to identify the number of vehicles involved in criminal activities, such as drug-related violations. It uses Python for data processing (with libraries like Pandas and SQLAlchemy) and MySQL as the database for storage and querying.


import pandas as ps 
import sqlalchemy as sq
import streamlit as sl
from sqlalchemy import create_engine

raw_data = (r"C:\Users\bosco\Downloads\traffic_stops - traffic_stops_with_vehicle_number1.csv")

A = ps.read_csv(raw_data)                      #This line of code is used to read the csv file
data = ps.DataFrame(A)                         #This line of code is used to change the raw file data into dataframe using pandas
print(data.info())                             #This line of code is used to check the data haave any null values using default pack
print(data.describe())                         #This line of code is used to check the min,std and max values the data have     
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/bot') #This is called as engine used to connect with sql database through python query
sqlconnector = data.to_sql('Traffic_police_project',con=engine,index=False,if_exists='replace') #This line is used to push the data to mysql connector
print('sucessfuly upddated to sql')            #This line is used to print the statement after the date has been uploaded

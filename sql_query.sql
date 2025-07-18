#(1)The below function is used to see all the data in sql
select * from traffic_police_project;

#(2)The Below function is used to see that which vechile has high number of drug_related_case
select vehicle_number, count(*) as drug_related_case from traffic_police_project where drugs_related_stop=1 group by  vehicle_number limit 10;

#(3)The Below function is used to see that which vechile has high number of searched_vechile
select vehicle_number, count(*) as searched_vechile from traffic_police_project where search_conducted=1 group by vehicle_number ;

#(4)The Below function is used to see that which age catageory has high number of stop_outcome
select driver_age,stop_outcome,count(stop_outcome) from traffic_police_project where stop_outcome = 'Arrest' group by driver_age order by count(stop_outcome) desc; 

#(5)The Below function is used to see that which country and gender has high number of drivers stopped
select country_name ,sum(case when driver_gender='M' then 1 else 0 end) as male_count,sum(case when driver_gender='F' then 1 else 0 end) as female_count from traffic_police_project group by country_name;

#(6)The Below function is used to see that how many country in the row
select distinct country_name from traffic_police_project group by country_name; 

#(7)The Below function is used to see the race and gender combination has the highest search rate
select driver_race , driver_gender ,count(*) as total_shape , SUM(CASE WHEN search_conducted = 1 THEN 1 ELSE 0 END) AS total_searches ,round(sum(CASE WHEN search_conducted = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),2) as search_rate from traffic_police_project group by driver_race , driver_gender order by search_rate desc;

#(8)This below query is used to show case the time of day sees the most traffic stops
select hour(stop_time) as Hours ,count(*) as No_of_stops from traffic_police_project group by hour(stop_time) order by count(*) asc limit 5;

#(9)This below query is used to show case the avrg stop duration for different violation by violation category
select (violation), round(avg(stop_time),1) as avg_stop_time from traffic_police_project group by(violation) order by avg_stop_time desc;

#(10)This below query is used to show case the stoping at night lead to arrests or not
select (hour(stop_time)) ,stop_outcome , count(*) from traffic_police_project where stop_outcome= 'Arrest' group by (hour(stop_time)) order by count(*) desc limit 5 ;
#Answer : No arresting person also more likly in day time also so stop at night time not leading to arrest

#(11)This below query is used to show case the which violations are most associated with searches or arrests
select distinct violation , sum(case when search_conducted=1 then 1 else 0 end) as search , sum((case when is_arrested=1 then 1 else 0 end)) as arrest ,
case when
sum(case when search_conducted=1 then 1 else 0 end) > sum(case when is_arrested=1 then 1 else 0 end ) then 'search' 
when sum(case when search_conducted=1 then 1 else 0 end) < sum(case when is_arrested=1 then 1 else 0 end ) then 'arrest' 
else 'equal'
end as 'Answer'
from traffic_police_project group by (violation);

#(12)This below query is used to show case the which violations are most common among younger drivers (<25).
select (violation), count(driver_age) as count_of_incident from traffic_police_project where driver_age<25 group by violation order by violation;

#(13)This below query is used to show case that there a violation that rarely results in search or arrest.
select violation ,count(*) as total_case , sum(case when stop_outcome='Arrest' then 1 else 0 end) as arrest , round (sum(case when stop_outcome = 'Arrest' then 1 else 0 end)*100/count(*),2) as percentage from traffic_police_project group by violation order by percentage limit 3;

#(14)This below query is used to show case the which country report the highest rate of drug-related stops.
select  country_name , count(violation) as total_no_of_violations from traffic_police_project where violation ='DUI' group by country_name order by total_no_of_violations asc;

#(15)This below query is used to show case the what is the arrest rate by country and violation
select country_name , violation , sum(case when is_arrested=1 then 1 else 0 end) * 100 /count(*) as percent_of_arrest from  traffic_police_project group by country_name,violation order by percent_of_arrest asc;

#(16)This below query is used to show case the Which country has the most stops with search conducted
select country_name , sum(case when search_conducted=1 then 1 else 0 end) as total from traffic_police_project group by country_name order by total desc;


#complex (1) this query is used to get the number of case that lead to arrest when search by year and country order.
select year(str_to_date(stop_date, '%d-%m-%y')) as year , 
country_name ,COUNT(CASE WHEN search_conducted = 1 THEN 1 END) AS search_conducted , 
count(stop_outcome) as stop_outcome , sum(case when search_conducted=1 then 1 else 0 end) as search , 
sum(case when stop_outcome='Arrest' then  1 else 0 end) as arrest , 
round(sum(case when stop_outcome='Arrest' then 1 else 0 end) * 100/ sum(case when search_conducted=1 then  1 else 0 end),2) as lead_to_arrest_when_search 
from traffic_police_project group by country_name ,year(str_to_date(stop_date, '%d-%m-%y')) order by lead_to_arrest_when_search desc ;

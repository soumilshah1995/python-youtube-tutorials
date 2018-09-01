"""

Assingment number 1

Write a Python code to calculate the speed for running a 10-kilometer race in 1 hours 5
minutes 42 seconds. What is the average pace (time per mile in minutes and seconds)?
What is the average speed in miles per hour?

SOUMIL SHAH
Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering


"""
import datetime

# Distance in Km
distance= 10

# Distance in Mile
distance_mile_10= 6.213

time= datetime.datetime(2018,9,1,1,5,42)

# extract minutes and seconds
minute=time.minute
sec=time.second

# convert minutes in hours
minute_5_to_hour= 0.0166667 * 5
sec_42__to_hour= 0.00027777833333 * 42
hour=time.hour

total_hour = hour + minute_5_to_hour + sec_42__to_hour
speed_km_hr = distance / total_hour

# convert km/hr into mile/hr
speed_mile = 0.621371 * speed_km_hr

#calculate total mile/minute
total_minute= 60 + 5 + 0.0166667
speed_mile_minute= distance_mile_10 / total_minute

#calculate speed in mile/sec
total_sec= 3600 + 300 + 42
speed_mile_sec= distance_mile_10 / total_sec


print("Complete Race of 10 KM in 1:5:42 speed has to be {} km/hr ".format(speed_km_hr))
print("Complete Race of 10 KM in 1:5:42 speed has to be {} Mile/hr ".format(speed_mile))
print("Complete Race of 10 KM in 1:5:42 speed has to be {} Mile/Min ".format(speed_mile_minute))
print("Complete Race of 10 KM in 1:5:42 speed has to be {} Mile/sec ".format(speed_mile_sec))
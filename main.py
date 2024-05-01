import pandas as pd

#reading the first csv file from the first quarter 2019
trips_q1 = pd.read_csv("C:/Users/Heitor/Desktop/Bike-2019/Divvy_Trips_2019_Q1.csv")

#reading the first csv file from the second quarter 2019
#trips_q2 = pd.read_csv("C:/Users/Heitor/Desktop/Bike-2019/Divvy_Trips_2019_Q2.csv")

#reading the first csv file from the third quarter 2019
#trips_q3 = pd.read_csv("C:/Users/Heitor/Desktop/Bike-2019/Divvy_Trips_2019_Q3.csv")

#reading the first csv file from the fourth quarter 2019
#trips_q4 = pd.read_csv("C:/Users/Heitor/Desktop/Bike-2019/Divvy_Trips_2019_Q4.csv")


# view the first 5 rows
print(trips_q1.head())
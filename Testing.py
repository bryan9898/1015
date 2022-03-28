
import mysql.connector as mysql #pip install mysql.connector 
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt # we only need pyplot

#What do i want from this dataset? 1) Player groups , player play time for certain games , add all the play times up , player achievements

db_connection = mysql.connect(user="root", password="jajasauce", host="34.143.214.112", database="steam")
cur = db_connection.cursor()


#cur.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")

#cur.execute("SELECT * FROM Player_Summaries LIMIT 3;")
#cur.execute("SELECT * FROM App_ID_Info;")

    
#What i want from the dataset , Get from 1st table : List of games App_ID_Info (List of all games on steam) 
# Merge 2 tables (App_ID_Info) and (GAMES_GENRES) to get the genre of games
cur.execute("SELECT ap.appid,ap.title,ap.price,gg.genre FROM App_ID_Info ap INNER JOIN Games_Genres gg ON ap.appid = gg.appid WHERE ap.type = 'game';")

myresult = cur.fetchall()
df = pd.DataFrame(myresult,columns=['appid','title','price','genre'])
print(df['genre'].value_counts())


#for x in myresult:

#    print(x) #print all tables
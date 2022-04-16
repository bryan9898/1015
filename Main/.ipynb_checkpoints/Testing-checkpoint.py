
import mysql.connector as mysql #pip install mysql.connector 
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt # we only need pyplot
import requests
import json
import warnings
warnings.filterwarnings('ignore')

import time

#What do i want from this dataset? 1) Player groups , player play time for certain games , add all the play times up , player achievements

#db_connection = mysql.connect(user="root", password="jajasauce", host="34.143.214.112", database="steam")
#cur = db_connection.cursor()


#cur.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")

#cur.execute("SELECT steamid,personaname FROM Player_Summaries WHERE personastate != 0 LIMIT 3;")
#cur.execute("SELECT * FROM App_ID_Info;")

    
#What i want from the dataset , Get from 1st table : List of games App_ID_Info (List of all games on steam) 
# Merge 2 tables (App_ID_Info) and (GAMES_GENRES) to get the genre of games
#cur.execute("SELECT ap.appid,ap.title,ap.price,gg.genre FROM App_ID_Info ap INNER JOIN Games_Genres gg ON ap.appid = gg.appid WHERE ap.type = 'game';")

#myresult = cur.fetchall()
#df = pd.DataFrame(myresult,columns=['appid','title','price','genre'])
#print(df['genre'].value_counts())


#for x in myresult:

#    print(x) #print all tables

#Now we get the user info, games they played , hours played, groups joined . Inner join 4 tables using SQL (DATA SET TOO BIG)
#cur.execute("SELECT ps.steamid,g1.appid,ap.title,ap.price,g1.playtime_forever FROM Player_Summaries ps INNER JOIN Games_1 g1 ON g1.steamid = ps.steamid INNER JOIN App_ID_Info ap ON g1.appid = ap.appid  WHERE ap.type = 'game' AND g1.playtime_forever != 'None' LIMIT 10000")

#myresult = cur.fetchall()
#for x in myresult:
#    print(x) #print all tables

# Using API 


API = "4141070D32E9CF793B1D9BC8A25C5950"

counter = 0; #limited 100,000 API query a day
Merged = pd.read_csv("PlayerGames_Cleaned.csv")
for x in range(2675,len(Merged['steamid'])):
    response = requests.get("https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="+API+"&steamid="+str(Merged['steamid'][x])+"&relationship=friend")
    reply = response.json();
    if(reply == {}):
        continue
    else:
        friendHave = 0;
        for y in reply['friendslist']['friends']: # save it to data frame instead
            if(friendHave == 1):
                break;
            friendResponse = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+API+"&steamid="+str(y['steamid'])+"&format=json")
            time.sleep(0.5)
            friendReply = friendResponse.json();
            counter += 1;
            if(friendReply['response'] == {}):
                continue;
            else:
                if(int(friendReply['response']['game_count']) == 0):
                    continue;
                else:
                    for friendGame in friendReply['response']['games']:
                        if(friendGame['appid'] == Merged['gamesid'][x]):
                            friendHave = 1;
                            break;
                                         
    
    print("STOP AT WHICH INDEX: " + str(x))
        

    print(friendHave)
    Merged['FriendHasGame'][x] = friendHave;
    Merged.to_csv('PlayerGames_Cleaned.csv', index=False) 
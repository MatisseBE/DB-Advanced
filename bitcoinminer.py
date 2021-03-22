import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timezone
import os
import redis
from contactredis import RedisToMongo

def Scraper():
    global df                                                                                                                       #to not get lost when rerunning
    global currenttime                                                                                                              #to not get lost when rerunning

    #print("callsing site")
                                                                                                                                    #Access the site
    response = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")  
    #print("call complete")
    site = response.text
    soup = BeautifulSoup(site,'html.parser')                                                                                        #Interpret html
    
    for transactions in soup.find_all('div',{"class": "sc-1g6z4xm-0 hXyplo"}):                                                      #On the site, find blocks of transactions
        transaction = []
        for hash in transactions.find('a'):
            transaction.append(hash)                                                                                                #In this block, find the hash of the transaction

        for info in transactions.find_all('span', {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"}):             #In this block, find all other information (Time, BTC, USD)
            transaction.append(info.string)

                                                                                                                                    #Make variables more readable, foramtting, typing
        Hash = transaction[0]   
        Time = transaction[1]
        BTC = float(transaction[2].replace("BTC","").replace(" ",""))
        USD = float(transaction[3].replace("$","").replace(",",""))


        
        if Time<currenttime:                                                                                                        #If out of date -entry older than current time- skip it
            #print("break")
            break

        if Time==currenttime:                                                                                                       #If correct time, add all to df of said time
            #print("equal time")
            new_row = {'Hash': Hash,'Time': Time,'Amount (BTC)': BTC,'Amount (USD)': USD}
            df = df.append(new_row,ignore_index=True)

        else:                                                                                                                       #If new time

            #print(df)

            #print(df.dtypes)                                                                                                        #For error handling (hypoth: empty frame)
            indx = df['Amount (USD)'].argmax()                                                                                      #Get row number where USD is the highest
            #print("From miner: $%s for time %s equal to %s BTC with hash `%s´" % (str(df.iloc[indx]['Amount (USD)']),str(df.iloc[indx]['Time']),str(df.iloc[indx]['Amount (BTC)']),str(df.iloc[indx]['Hash'])))  

            datajson = df.to_json(orient="index")                                                                                   #Rewrite dataframe to JSON format


            # print(df.iloc[indx]['Amount (USD)'])                                                                                  #Print highest value
            # print(df.iloc[indx]['Hash'])                                                                                          #Print highest value
            # print(df.iloc[indx]['Time'])                                                                                          #Print highest value
            # print(df.iloc[indx]['Amount (BTC)'])                                                                                  #Print highest value




            r.set("df", str(datajson))                                                                                              #In Redis DB, set key "df" to value of string JSON of pandas DF

            print(RedisToMongo())                                                                                                   #Executes the contact redis script


            currenttime = Time                                                                                                      #Set new time

            df = pd.DataFrame(columns=['Hash','Time','Amount (BTC)','Amount (USD)'])                                                #Emptry current df

                                                                                                                                    #Make variables more readable, foramtting, typing
            Hash = transaction[0]
            Time = transaction[1]
            BTC = float(transaction[2].replace("BTC","").replace(" ",""))
            USD = float(transaction[3].replace("$","").replace(",",""))

            new_row = {'Hash': Hash,'Time': Time,'Amount (BTC)': BTC,'Amount (USD)': USD}                                           
            df = df.append(new_row,ignore_index=True)                                                                                #Add this block (1) to new df, next one will go via second if statement





#Initialize project
now = datetime.now(timezone.utc)                                                                                                     #Get current Zulu time (website utilizes UTC/GMT)                                                                           
currenttime=now.strftime('%H:%M')                                                                                                    #Get hour and minutes of current time

df = pd.DataFrame(columns=['Hash','Time','Amount (BTC)','Amount (USD)'])                                                             #Initialize dataframe       


r = redis.Redis(host='localhost', port=8080, db=0)                                                                                                                    #Initialize Redis DB



#Run project
while True:
    Scraper()


                                                            





        
    



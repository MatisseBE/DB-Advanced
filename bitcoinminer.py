import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timezone

def Scraper():
    global df                                                                                                                       #to not get lost when rerunning
    global currenttime                                                                                                              #to not get lost when rerunning

    #print("callsing site")
                                                                                                                                    #Access the site
    response = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions", headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})  
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
            print("$%s for time %s" % (str(df['Amount (USD)'].max()),currenttime))                                                  #Print highest value

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

#Run project
while True:
    Scraper()

        
    



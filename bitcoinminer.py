import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timezone

def Scraper():
    global df
    global currenttime

    #print("callsing site")
    response = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions", headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})                                              #Access the site
    #print("call complete")
    site = response.text
    soup = BeautifulSoup(site,'html.parser')
    
    for transactions in soup.find_all('div',{"class": "sc-1g6z4xm-0 hXyplo"}):                                                      #On the site, find blocks of transactions
        transaction = []
        for hash in transactions.find('a'):
            transaction.append(hash)                                                                                                #In this block, find the hash of the transaction

        for info in transactions.find_all('span', {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"}):             #In this block, find all other information (Time, BTC, USD)
            transaction.append(info.string)

        Hash = transaction[0]
        Time = transaction[1]
        BTC = float(transaction[2].replace("BTC","").replace(" ",""))
        USD = float(transaction[3].replace("$","").replace(",",""))


        
        if Time<currenttime:
            #print("break")
            break

        if Time==currenttime:
            #print("equal time")
            new_row = {'Hash': Hash,'Time': Time,'Amount (BTC)': BTC,'Amount (USD)': USD}
            df = df.append(new_row,ignore_index=True)

        else:
            print(df)
            print(df['Amount (USD)'].max())

            currenttime = Time

            df = pd.DataFrame(columns=['Hash','Time','Amount (BTC)','Amount (USD)'])   #new dataframe
            
            Hash = transaction[0]
            Time = transaction[1]
            BTC = float(transaction[2].replace("BTC","").replace(" ",""))
            USD = float(transaction[3].replace("$","").replace(",",""))

            new_row = {'Hash': Hash,'Time': Time,'Amount (BTC)': BTC,'Amount (USD)': USD}
            df = df.append(new_row,ignore_index=True)





#Initialise
now = datetime.now(timezone.utc)
currenttime=now.strftime('%H:%M')



df = pd.DataFrame(columns=['Hash','Time','Amount (BTC)','Amount (USD)']) 
        
while True:
    Scraper()
    



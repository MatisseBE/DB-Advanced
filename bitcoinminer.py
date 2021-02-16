import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def Scraper():
    try: 
        response = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")                                              #Access the site
        site = response.text
        soup = BeautifulSoup(site,'html.parser')

        df = pd.DataFrame(columns=['Hash','Time','Amount (BTC)','Amount (USD)'])                                                        #Creaate a dataframe
        
        for transactions in soup.find_all('div',{"class": "sc-1g6z4xm-0 hXyplo"}):                                                      #On the site, find blocks of transactions
            transaction = []
            for hash in transactions.find('a'):
                transaction.append(hash)                                                                                                #In this block, find the hash of the transaction

            for info in transactions.find_all('span', {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"}):             #In this block, find all other information (Time, BTC, USD)
                transaction.append(info.string)
            
            new_row = {'Hash': transaction[0],'Time': transaction[1],'Amount (BTC)': transaction[2],'Amount (USD)': transaction[3]}     #Of this block, add all information to the dataframe
            df = df.append(new_row,ignore_index=True)

        return df['Amount (USD)'].max()                                                                                                 #Transaction with the largest amount
    
    except:
        return -1
        
while True:
    print(Scraper())
    time.sleep(60)
    



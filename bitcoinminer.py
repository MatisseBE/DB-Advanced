import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def Scraper():
    try: 
        response = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
        site = response.text
        soup = BeautifulSoup(site,'html.parser')

        df = pd.DataFrame(columns=['Hash','Time','Amount (BTC)','Amount (USD)'])
        
        for transactions in soup.find_all('div',{"class": "sc-1g6z4xm-0 hXyplo"}):
            transaction = []
            #print()
            print('finding transactions')
            for hash in transactions.find('a'):
                #print(hash)
                transaction.append(hash)

            for info in transactions.find_all('span', {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"}):
                transaction.append(info.string)
                #print(info.string)
            
            new_row = {'Hash': transaction[0],'Time': transaction[1],'Amount (BTC)': transaction[2],'Amount (USD)': transaction[3]}
            df = df.append(new_row,ignore_index=True)
        
        #print(df)
        return df['Amount (USD)'].max()
    
    except:
        return -1
        
while True:
    print(Scraper())
    time.sleep(60)
    



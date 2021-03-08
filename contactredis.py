import redis
import pymongo as mongo
import pandas as pd

r = redis.Redis(host='localhost', port=8080, db=0)                                                                                               #Call Redis

datajson = r.get("df")                                                                                          #Get value of key df from Redis DB
df = pd.read_json(datajson,orient="index")  	                                                                #Parse Redis value(string), desguised as JSON, into a pandas DataFrame

# print("length", len(df))
# print(df)

indx = df['Amount (USD)'].argmax()                                                                              #Get row number where USD is the highest

Hash = df.iloc[indx]['Hash']
Time = df.iloc[indx]['Time']
USD = df.iloc[indx]['Amount (USD)']
BTC = df.iloc[indx]['Amount (BTC)']

print("$%s for time %s equal to %s BTC with hash `%s´" % (str(df.iloc[indx]['Amount (USD)']),str(df.iloc[indx]['Time']),str(df.iloc[indx]['Amount (BTC)']),str(df.iloc[indx]['Hash'])))  


client = mongo.MongoClient("mongodb://127.0.0.1:8081")                                                         #Connect to mongo 27017
bitcoindb = client["Mining_operation"]                                                                          #Make new DB


col_mining = bitcoindb["Largest_entry"]                                                                         #Make new collections

data = {"Hash": Hash, "Time": Time, "USD": USD, "BTC": BTC}                                                     #Format data

x = col_mining.insert_one(data)                                                                                 #Insert data

#print(x.inserted_id)                                                                                            #Prints ID in said collection in mongodb
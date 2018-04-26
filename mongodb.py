from pymongo import *

client = MongoClient('localhost',1880)

db = client.college

if db:
	print("Connected")

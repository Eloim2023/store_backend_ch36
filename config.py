import pymongo
import certifi



con_str = "mongodb+srv://ITM2023_02:ITMele_2023@cluster0.so7jomx.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database('organika')
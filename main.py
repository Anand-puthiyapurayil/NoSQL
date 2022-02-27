import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://Anand_puthiyapurayil:Anitha123@cluster0.aiq8u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db.countries
    con = db.continents
    print(db.list_collection_names())


    cursor= col.find({})
    for i in cursor:
        print(i)
    cont=con.find({})
    for a in cont:
        print(a)







if __name__ == '__main__':
    connectdb()

import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient("mongodb+srv://Anand_puthiyapurayil:Anitha123@cluster0.aiq8u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    con = db.continents
    continents = con.find({},{'Name':1, 'countries':{'$slice':4}}).sort("Name")
    for FourCountry in continents:
        print(FourCountry)


if __name__ == '__main__':
        connectdb()
import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://Anand_puthiyapurayil:Anitha123@cluster0.aiq8u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db.countries
    con = db.continents
    def orderbypopulation():
        for countries in col.find({}).sort("Population"):
            print(countries['Name'], countries['Population'])
    orderbypopulation()

if __name__ == '__main__':
    connectdb()
import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://Anand_puthiyapurayil:Anitha123@cluster0.aiq8u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db.countries
    con = db.continents

    def query7():
        for continents in col.find({
                    'Name':
                        {'$regex': 'u', '$options': 'i'}, 'Population': {'$gt': 100000}
                }
        ).sort("population"):
            print( continents['Name'], continents['Population'])
    query7()

if __name__ == '__main__':
    connectdb()

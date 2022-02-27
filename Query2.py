import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://Anand_puthiyapurayil:Anitha123@cluster0.aiq8u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db.countries
    con = db.continents
    #  Send the list of continent with there number of countries
    def continents():
        agg_pipeline = [
        {
            '$project': {
                'name': "$name",
                'countries': {'$size': "$countries"}}
        }
        ]
        cont = con.aggregate(agg_pipeline)
        for continent in cont:
            print(continent)
    continents()

if __name__ == '__main__':
    connectdb()
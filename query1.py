import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://Anand_puthiyapurayil:Anitha123@cluster0.aiq8u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db.countries
    con = db.continents

    # 1/ Get all the country where a letter or word given is in the name=> for example: FR Fran...
    def find_country():
        word=str(input("Enter the word"))
        for country in col.find({"Name":{'$regex':word,'$options':'i'}}):
            print(country['Name'])
    find_country()

if __name__ == '__main__':
    connectdb()

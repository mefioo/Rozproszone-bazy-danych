def readAndModifyData():
    file = open("app/static/Textfiles/airports.txt", "r")
    airports = []
    for line in file:
        airport = {}
        city = line.split(',')[0]
        code = line.split('(')[1]
        airport["city"] = city
        airport["code"] = code.split(')')[0]
        airports.append(airport)
    return airports

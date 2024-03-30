from writeJson import writeJsonSecond

def listiPhone():
    modelName = []

    products = writeJsonSecond()["body"]["products"]

    for product in products:
        modelName.append(product["modelName"])

    for item in modelName:
        print(item)

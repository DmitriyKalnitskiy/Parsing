from writeJson import writeJsonFirst

def minPrice():
    min_price = min(writeJsonFirst().values(), key=lambda x: x["itemBasePrice"])["itemBasePrice"]
    return  min_price

def maxPrice():
    max_price = max(writeJsonFirst().values(), key=lambda x: x['itemBasePrice'])['itemBasePrice']
    return max_price

def srPrice():
    srPr = 0
    count = 0

    for item in writeJsonFirst().values():
        srPr += int(item["itemBasePrice"])
        count += 1

    srPr = srPr / count

    return srPr
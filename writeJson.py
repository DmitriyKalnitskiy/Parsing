import json
def writeJsonFirst():
    with open('ItemsPrices.json', 'r') as file:
        total_price = json.load(file)
        return total_price

def writeJsonSecond():
    with open('Items.json', 'r') as file:
        phoneIs = json.load(file)
        return phoneIs

from parser import parserMvideo
from discountedPrice import minPrice, maxPrice, srPrice
from iPhone import listiPhone

def main():
    parserMvideo()
    print(f'Мин. цена: {minPrice()}\n')
    print(f'Макс. цена: {maxPrice()}\n')
    print(f'Ср. цена: {srPrice()}\n')
    print(f'Список айфонов: ')
    listiPhone()

if __name__ == '__main__':
    main()
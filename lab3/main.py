from EcigaretteFactory import DeliverDisposable, DeliverStarterKit, DeliverAdvancedKit
from Handler import HeterosexualityHandler, GenderHandler, AgeHandler
from LiquidDecorator import Liquid2, Liquid5
from Stock import Stock
from Container import Container
from ForeignEcig import ForeignEcig
from ForeignEcigAdapter import ForeignEcigAdapter

if __name__ == "__main__":
    starter_delivery = DeliverStarterKit()
    advanced_delivery = DeliverAdvancedKit()
    disposable_delivery = DeliverDisposable()

    ecig1 = starter_delivery.deliver_ecigarette()
    ecig2 = advanced_delivery.deliver_ecigarette()
    ecig3 = disposable_delivery.deliver_ecigarette()
    foreign_ecig = ForeignEcig("idk Italy", 55)

    dec_ecig3 = Liquid2(Liquid5(ecig3)) #decorator pattern

    stock = Stock()
    container = Container() # composite pattern
    container.add(ecig1)
    container.add(ecig2)

    container.add(ForeignEcigAdapter(foreign_ecig)) # adapter pattern

    het = HeterosexualityHandler()
    gen = GenderHandler()
    age = AgeHandler()

    age.set_next(gen).set_next(het) # Chain of Responsibility pattern

    for test in ["Age","Gender"]:
        result = age.handle(test)
        if result:
            print(result)
        else:
            print("No test were passed :(, sory u  cant buy any electric cigarette")

    stock.add_product(container)
    stock.add_product(dec_ecig3)



    print("Current Inventory: ")
    stock.list_stock()

from EcigaretteFactory import DeliverDisposable, DeliverStarterKit, DeliverAdvancedKit
from Stock import Stock
from lab2.Container import Container
from lab2.ForeignEcig import ForeignEcig
from lab2.ForeignEcigAdapter import ForeignEcigAdapter
from lab2.LiquidDecorator import Liquid5, Liquid2

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

    stock.add_product(container)
    stock.add_product(dec_ecig3)

    print("Current Inventory: ")
    stock.list_stock()

from EcigaretteFactory import DeliverDisposable, DeliverStarterKit, DeliverAdvancedKit
from Stock import Stock

if __name__ == "__main__":
    starter_delivery = DeliverStarterKit()
    advanced_delivery = DeliverAdvancedKit()
    disposable_delivery = DeliverDisposable()

    # Deliver e-cigarettes to the storehouse
    ecig1 = starter_delivery.deliver_ecigarette()
    ecig2 = advanced_delivery.deliver_ecigarette()
    ecig3 = disposable_delivery.deliver_ecigarette()

    stock = Stock()

    # Add products to inventory
    stock.add_product(ecig1)
    stock.add_product(ecig2)
    stock.add_product(ecig3)

    print("Current Inventory:")
    stock.list_stock()

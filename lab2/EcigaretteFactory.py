from abc import abstractmethod, ABC

from Ecigarette import StarterKit, AdvancedKit, Disposable, Ecigarette


class DeliverToStoreHouseEcigarette(ABC):

    def deliver_ecigarette(self) -> Ecigarette:
        ecig = self.create_ecig()
        return ecig

    @abstractmethod
    def create_ecig(self) -> Ecigarette:
        pass


class DeliverStarterKit(DeliverToStoreHouseEcigarette):
    def create_ecig(self) -> Ecigarette:
        return StarterKit("Zimbabwa", 29.99)

class DeliverAdvancedKit(DeliverToStoreHouseEcigarette):
    def create_ecig(self) -> Ecigarette:
        return AdvancedKit("IQS", 79.99)

class DeliverDisposable(DeliverToStoreHouseEcigarette):
    def create_ecig(self) -> Ecigarette:
        return Disposable("Vaporeso", 9.99)
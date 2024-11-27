from Ecigarette import Ecigarette


class LiquidDecorator(Ecigarette):

    _ecigarette: Ecigarette = None


    def __init__(self , ecig: Ecigarette):
        self._ecigarette = ecig

    def component(self):
        return self._ecigarette


    def list(self) ->str:
        return self._ecigarette.list()



class Liquid5(LiquidDecorator):
    def list(self) ->str:
        base_description = super().list()

        return f"{base_description} | Liquid: 5% liquid"


class Liquid2(LiquidDecorator):
    def list(self) ->str:
        base_description = super().list()

        return f"{base_description} | Liquid: 2% liquid"
# Structural Design Patterns

## Author: Vlad Pruteanu

----

## Objectives:
* Study and understand the Structural Design Patterns.
* As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.
* Implement some additional functionalities using structural design patterns.
  


## Used Design Patterns:
* Decorator - Added extra properties (different liquid types) to e-cigarettes without modifying the base class.
* Composite - Created a container to group multiple components, allowing nested structures of e-cigarettes and accessories.
* Adapter - Integrated foreign e-cigarette models into our system by adapting them to the expected interface.


## Implementation

### Decorator
- The LiquidDecorator pattern was used to add different liquid percentages (e.g., 2% and 5%) to e-cigarettes dynamically. This enables customizing the e-cigarettes' features without altering their base structure.

```python
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


```


###  Composite

- The Component and Container classes allow grouping multiple e-cigarettes or accessories together, treating them as a single item in the system. This setup makes managing multiple related components easier, supporting both single items and collections.

```python
class Component(ABC):

    def __init__(self):
        super().__init__()
        self._parent = None

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    def is_container(self) -> bool:
        return False


    @abstractmethod
    def list(self)->str:
        pass

    
class Container(Component):

    def __init__(self):
        self._children : List[Component] = []

    def add(self, component: Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component):
        self._children.remove(component)
        component.parent = None

    def is_container(self) -> bool:
        return True

    def list(self) ->str:
        results = []
        for child in self._children:
            results.append(child.list())
        return f"Container({'+'.join(results)})"


```

### Adapter
- The ForeignEcigAdapter pattern was used to adapt foreign e-cigarette models to match our system’s interface, allowing us to seamlessly integrate e-cigarettes from other sources.

```python
class ForeignEcigAdapter(Ecigarette):
    def __init__(self, foreign_ecig: ForeignEcig):
        self._foreign_ecig = foreign_ecig

    @property
    def name(self):
        return self._foreign_ecig.getName()

    @property
    def price(self):
        return self._foreign_ecig.getCost()

    def list(self):
        return f"Foreign E-cigarette - {self.name}: ${self.price}"


```



## Conclusions / Screenshots / Results

Structural patterns such as Decorator, Composite, and Adapter provided flexible ways to add new features, manage groups of components, and integrate external models into our system without major structural changes.


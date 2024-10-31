# Creational Design Patterns

## Author: Vlad Pruteanu

----

## Objectives:
* Study and understand the Creational Design Patterns.
* Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.
* Use some creational design patterns for object instantiation in a sample project.

## Used Design Patterns:
* Singleton - restricts the instantiation of a class to a singular instance
* Factory - create objects without having to specify their exact classes. 


## Implementation

### Singleton
 - A single instance of **Stock** can exist at any given time. The synchronized **Stock** method manages access to the singleton instance, which is initialized lazily to enhance performance.

```python

class Stock:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.stock = []
        return cls._instance

```


###  Factory
 - The abstract class **DeliverToStoreHouseEcigarette** acts as a foundation for producing related products. Each subclass, such as **DeliverStarterKit**, defines methods for creating a specific kind of e-cigarette.

```python


class DeliverToStoreHouseEcigarette(ABC):

    def deliver_ecigarette(self) -> Ecigarette:
        ecig = self.create_ecig()
        return ecig

    @abstractmethod
    def create_ecig(self) -> Ecigarette:
        pass



class DeliverStarterKit(DeliverToStoreHouseEcigarette):
    def create_ecig(self) -> Ecigarette:
        return StarterKit("Starter Kit", 29.99)

```



## Conclusions / Screenshots / Results

This lab focused on implementing creational design patterns, specifically the Singleton and Factory patterns. The Singleton pattern allowed for a single instance of the Stock class, ensuring controlled access. Meanwhile, the Factory pattern facilitated the creation of various e-cigarette types through a structured framework. This experience demonstrated the benefits of using design patterns for improved code organization and maintainability.
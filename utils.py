from __future__ import annotations
from abc import ABC, abstractmethod

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Queue:
    def __init__(self, max):
        self.values = []
        self.max = max

    def len(self):
        return len(self.values)

    def add(self,direction):
        if(len(self.values)<self.max):
            self.values.append(direction)
            return

        for i in range(len(self.values)):
            if(i==0):
                continue
            self.values[i-1] = self.values[i]
            if(i == len(self.values)-1):
                self.values[i] = direction

    def last(self):
        if(len(self.values)>0):
            return self.values[-1]
    
    def last_last(self):
        if(len(self.values)>0):
            return self.values[0]

    def delete(self):
        for i in range(len(self.values)):
            if(i==0 and len(self.values)>1):
                continue
            self.values[i-1] = self.values[i]
            if(i == len(self.values)-1):
                del self.values[i]
    def __str__(self):
        return str(self.values)


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class DebugInfo(Subject):
    is_active = None

    _observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def change_state(self, state) -> None:
        self.is_active = state
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update_observer(self, subject: Subject) -> None:
        pass
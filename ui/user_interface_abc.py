from abc import ABC, abstractmethod


class UserInterfaceABC(ABC):
    def __init__(self, controller):
        self.controller = controller

    @abstractmethod
    def run(self):
        ...

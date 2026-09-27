from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def process(self):
        pass

class CashPayment(Payment):

    def process(self):
        return "Processing cash payment"

class CardPayment(Payment):

    def process(self):
        return "Processing card payment"



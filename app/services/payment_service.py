
class PaymentService:

    def __init__(self, payment_repository):
        self.payment_repository = payment_repository

    def process_payment(self, payment):
        result = payment.process()
        self.payment_repository.add(payment)

        return result

    def list_payments(self):
        return self.payment_repository.get_all()


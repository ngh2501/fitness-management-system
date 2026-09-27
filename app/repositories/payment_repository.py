import json
from pathlib import Path
from app.model.payment import CashPayment, CardPayment

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class PaymentRepository:

    def __init__(self):
        self.file_path = BASE_DIR / "data" / "payments.json"

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as jsonfile:
            return json.load(jsonfile)

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    def add(self, payment):
        data = self._load()

        if isinstance(payment, CashPayment):
            method = "cash"
        elif isinstance(payment, CardPayment):
            method = "card"
        else:
            raise ValueError("Payment không hợp lệ")

        data.append({
            "method": method
        })

        self._save(data)

    def get_all(self):
        data = self._load()
        payments = []

        for item in data:
            if item["method"] == "cash":
                payment = CashPayment()
            elif item["method"] == "card":
                payment = CardPayment()
            else:
                raise ValueError("Method payment không hợp lệ")

            payments.append(payment)

        return payments


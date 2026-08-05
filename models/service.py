class Service:
    def __init__(self,
                 service_id: str,
                 name: str,
                 category: str,
                 price: int,
                 duration: str,
                 capacity: int,
                 status: str = "Active"):
        self.service_id = service_id
        self.name = name
        self.category = category
        self.price = price
        self.duration = duration
        self.capacity = capacity
        self.status = status

    def __str__(self):
        return f"[{self.service_id}] {self.name} ({self.category}) - {self.price:,} VNĐ | Trạng thái: {self.status}"


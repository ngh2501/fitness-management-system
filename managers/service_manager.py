from models.service import Service


class ServiceManager:

    def __init__(self):
        self.services: list[Service] = []

    def add_service(self, service: Service):
        self.services.append(service)

    def get_all_services(self):
        return self.services

    def find_service_by_id(self, service_id: str):
        for service in self.services:
            if service.service_id == service_id:
                return service
        return None

    def deactivate_service(self, service_id: str) -> bool:
        service = self.find_service_by_id(service_id)

        if service:
            service.status = "Inactive"
            return True
        return False

    def update_service(self, updated_service: Service) -> bool:
        service = self.find_service_by_id(updated_service.service_id)

        if not service:
            return False

        service.name = updated_service.name
        service.category = updated_service.category
        service.price = updated_service.price
        service.duration = updated_service.duration
        service.capacity = updated_service.capacity
        service.status = updated_service.status

        return True
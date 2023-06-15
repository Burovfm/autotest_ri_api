import requests

from config import RI_BASE_URL


class ResourceInventoryClient:
    def get_attributes(self, json_data,
                       path="/mtt.oliwio.resource.resource_inventory.resources.v1.ResourcesService/GetAttributes"):
        response = requests.post(url=f'{RI_BASE_URL}{path}', json=json_data)
        return response

    def create(self, json_data,
               path="/mtt.oliwio.resource.resource_inventory.application.v1.ApplicationService/Create"):
        response = requests.post(url=f'{RI_BASE_URL}{path}', json=json_data)
        return response

    def get_application(self, json_data,
                        path="/mtt.oliwio.resource.resource_inventory.customer.v1.CustomerService/GetApplication"):
        response = requests.post(url=f'{RI_BASE_URL}{path}', json=json_data)
        return response

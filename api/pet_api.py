from api.base_api import BaseAPI

class PetAPI(BaseAPI):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def create_pet(self, pet_data: dict):
        return self._request("POST", "pet", json=pet_data)
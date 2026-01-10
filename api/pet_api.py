import requests
from api.base_api import StoreAPI


class PetAPI(StoreAPI):
    def add_pet(self, pet_data: dict) -> requests.Response:
        """
        Добавление нового питомца
        POST https://petstore.swagger.io/v2/pet
        """
        url = f"{self.base_url}/pet"

        response = requests.post(
            url,
            json=pet_data,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            timeout=10
        )

        return response
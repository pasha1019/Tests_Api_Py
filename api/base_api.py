import requests


class PetStoreAPI:
    """Клиент для работы с PetStore API"""

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

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
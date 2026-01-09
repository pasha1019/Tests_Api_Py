import allure
import pytest
from data.pet_data import generate_pet_data
from api.base_api import PetStoreAPI


@allure.feature("POST /pet")
class TestPetPostStatus:
    """Тест проверки статус кода для эндпоинта POST /pet"""

    @allure.title("Проверка статус кода 200 при успешном создании питомца")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_pet_returns_200_status_code(self):
        """
        Тест проверяет, что при успешном создании питомца
        возвращается статус код 200
        """
        # Arrange
        api_client = PetStoreAPI()
        pet_data = generate_pet_data()

        # Act
        with allure.step("Отправка POST запроса на создание питомца"):
            response = api_client.add_pet(pet_data)

            # Прикрепляем данные запроса к отчету
            allure.attach(
                str(pet_data),
                name="Request Data",
                attachment_type=allure.attachment_type.JSON
            )

            # Прикрепляем ответ к отчету
            allure.attach(
                response.text,
                name="Response Data",
                attachment_type=allure.attachment_type.JSON
            )

        # Assert
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200, \
                f"Expected status code 200, but got {response.status_code}"

            # Дополнительная информация для отчета
            allure.attach(
                f"Response Status Code: {response.status_code}",
                name="Status Code",
                attachment_type=allure.attachment_type.TEXT
            )
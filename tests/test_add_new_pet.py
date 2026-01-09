import allure
import pytest
from models.pet_model import Pet
from config.settings import settings


@allure.epic("PetStore API")
@allure.feature("Pet Management")
class TestPetAPI:

    @allure.story("Create Pet")
    @allure.title("Test create new pet")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user(self, pet_api, test_pet_data):
        """Test creating a new pet"""
        with allure.step("Step 1: Create new pet"):
            response = pet_api.create_pet(test_pet_data)

        with allure.step("Step 2: Verify response"):
            assert response.status_code == 200
            response_data = response.json()

            # Validate response structure
            pet_response = Pet(**response_data)
            assert pet_response.code == 200
            assert "id" in pet_response.message

            allure.attach(str(response.json()), "Create Pet Response", allure.attachment_type.JSON)

import pytest
from api.pet_api import PetAPI
from config.settings import settings
from data.pet_data import generate_pet_data


@pytest.fixture(scope="session")
def pet_api():
    """Fixture for PetAPI instance"""
    return PetAPI(settings.BASE_URL)


@pytest.fixture
def test_pet_data():
    """Fixture for test pet data"""
    return generate_pet_data()


@pytest.fixture
def created_pet(pet_api, test_pet_data):
    """Fixture to create test pet"""
    # Create pet
    response = pet_api.create_pet(test_pet_data)
    yield test_pet_data



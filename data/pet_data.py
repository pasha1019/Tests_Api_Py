import random



def generate_pet_data() -> dict:
    """Generate test pet data"""
    pet_id = random.randint(1000, 9999)
    category_id = random.randint(1000, 9999)
    return {
        "id": pet_id,
        "category": {
            "id": category_id,
            "name": "Test_category"
        },
    "name": f'Test_pet_{pet_id}',
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}
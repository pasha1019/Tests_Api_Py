import requests
from data.pet_data import generate_pet_data
from config.settings import Settings


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
# create pet
response_create_pet = requests.post(f'{Settings.BASE_URL}/pet',json=generate_pet_data(), headers=headers)
# get status
print(response_create_pet.status_code)
# get body
json_response = response_create_pet.json()
print(json_response)
# get pet id
pet_id = json_response["id"]
print(pet_id)
# get info about new pet
response_get_pet_info_by_id = requests.get(f'{Settings.BASE_URL}/pet/{pet_id}',headers=headers)
print(response_get_pet_info_by_id.status_code)
print(response_get_pet_info_by_id.json())
# update info about pet
new_data = {
        "id": pet_id,
        "category": {
            "id": 2,
            "name": f'Test_category_2'
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
response_update_pet_info = requests.put(f'{Settings.BASE_URL}/pet',json=new_data, headers=headers)
print(response_update_pet_info.status_code)
# delete pet
response_delete_pet = requests.delete(f'{Settings.BASE_URL}/pet/{pet_id}',headers=headers)
print(response_delete_pet.status_code)
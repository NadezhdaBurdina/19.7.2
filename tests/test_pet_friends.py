from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password = valid_password):

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result




def test_add_new_pet_with_valid_data(name='Барсик', animal_type='лев', age='4', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result ['name'] == name

def test_add_new_pet_with_valid_data_without_name(name='', animal_type='лев', age='4', pet_photo='images/cat1.jpg'):
    """Проверяем возможность добавления питомца без имени """

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result ['name'] == name



def test_add_pet_without_photo_with_valid_data(name='Тишка', animal_type = 'Перс', age = '2'):
    """Проверяем можно ли добавить питомца без загрузки фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


def test_neg_add_pet_without_photo_with_long_name(name='Проыгвнцицсшылоаыщвщвоагырфофлашырвдвранпыефрфдвтсрвпуегвшчочослырфпвналмчрвоылсоымфпвеаофраоалырааи', animal_type = 'Перс', age = '2'):
    """Проверяем можно ли добавить питомца без загрузки фото именем длинной болеее 50 символов """
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert result['name'] == name


def test_add_pet_without_photo_with_num_animal_type(name='Тиг', animal_type = '2', age = '2'):
    """Проверяем можно ли добавить питомца указав породу числом """
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

def test_add_pet_without_photo_with_age_in_letter(name='Тигр', animal_type = 'Тигр', age = 'Пять'):
    """Проверяем можно ли добавить питомца указав возраст буквами """
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert result['name'] == name


def test_add_pet_without_photo_with_big_age(name='Тигр', animal_type = 'Тигр', age = '123456'):
    """Проверяем можно ли добавить питомца указав возраст шестизначным числом """
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert result['name'] == name


def test_add_pet_without_photo_without_name_animal_type_age(name='', animal_type = '', age = ''):
    """Проверяем можно ли добавить питомца не указав имя, породу, возраст"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert result['name'] == name



def test_add_photo_of_pet(pet_id='5d53b5e1-8e88-40af-896d-35b0b96659e6', pet_photo='images/104104.jpg'):
    """Проверяем возможность добавления фото к существующему питомцу"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key=pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200


def test_add_photo_of_unreal_pet(pet_id='5d53b5e1-8e88-40af-896d-35b0b96659e5', pet_photo='images/104104.jpg'):
    """Проверяем возможность добавления фото к питомцу с несуществующим id"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 500


def test_add_photo_of_pet_without_name(pet_id='60730d2a-57da-42c7-acfe-986c3064dc05', pet_photo='images/104104.jpg'):
    """Проверяем возможность добавления фото к существующему питомцу без данных"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key=pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200



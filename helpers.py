import requests
from faker import Faker
import string
import random
import data


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_new_user_return_log_pass():
    log_pass = []
    fake = Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(data.REGISTER_URL, data=payload)
    if response.status_code == 200:
        log_pass.append(email)
        log_pass.append(password)
        log_pass.append(name)
    return log_pass


def generate_email():
    fake = Faker()
    test_email = fake.email()
    return test_email

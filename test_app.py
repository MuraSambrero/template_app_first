from database.fake_db import fake_db
import requests

# query_list_test = [
#     'http://localhost:8000/api/get_form?first_name=Nikita',
#     'http://localhost:8000/api/get_form?first_name=Nikita&last_name=Bratenkov',
#     'http://localhost:8000/api/get_form?color_name=red&opacity=max',
#     'http://localhost:8000/api/get_form?title=Nikita&content=video&from=neones@yandex.ru&to=alexander@yandex.ru&date=10.10.2023',
#     'http://localhost:8000/api/get_form?login=Nikita&first_name=Nikita&email=neones@yandex.ru&telephone=+79248200008&birthday=21.10.1991',
# ]

query = 'http://localhost:8000/api/get_form'
my_name = {
    'first_name': 'Nikita',
    'last_name': 'Bratenkov'
}
response = requests.post(query, params=my_name)
print(response.text)



# def check(elem):
#     pass
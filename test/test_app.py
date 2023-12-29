import requests
import os

host = os.environ.get("APP_HOST")
port = os.environ.get("APP_PORT")
query = f'http://{host}:{port}/api/get_form'

test_requests = [
    {
        "name": "Имя",
        "first_name": "text"
      },
      {
        "name": "Имя и фамилия",
        "first_name": "text",
        "last_name": "text"
      },
      {
        "name": "My color",
        "color_name": "text",
        "opacity": "text"
      },
      {
        "name": "email_template",
        "title": "text",
        "content": "text",
        "from": "email",
        "to": "email",
        "date": "date"
      },
      {
        "name": "person",
        "login": "text",
        "first_name": "text",
        "email": "email",
        "telephone": "phone",
        "birthday": "date"
      }
]

def check_templates(host, port, query, test_requests):
    for elem in test_requests:
        response = requests.post(query, params=elem)
        print(response.text)

check_templates(host, port, query, test_requests)
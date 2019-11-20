import requests


def user_name(name):
    response = requests.get('https://api.github.com/users/' + name)
    data = response.json()
    return data

print(user_name("redcartel"))


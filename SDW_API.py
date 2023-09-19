import pandas as pd
import requests
import json
import openai


df = pd.read_csv("SDW2023.csv")
user_ids = df["UserID"].tolist()
print(user_ids)

# openai.api_key = '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'
openai.api_key = "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"
sdw2023_api_url = "https://sdw-2023-prd.up.railway.app"


def get_user(id):
    response = requests.get(f"{sdw2023_api_url}/users/{id}")
    return response.json() if response.status_code == 200 else None


def generate_news(user):
    print(user["name"])
    mensage = f"Olá {user['name']}, isto é um teste para a transformação, já que não tenho como transformar atravez do chatGPT kkk"
    return mensage


def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

for user in users:
    news = generate_news(user)
    print(news)
    user["news"].append(
        {
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news,
        }
    )


for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")

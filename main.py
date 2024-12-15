import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_access_token():
    url = "https://api-performance.ozon.ru/api/client/token"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "client_id": os.getenv("client_id"),
        "client_secret": os.getenv("client_secret"),
        "grant_type": "client_credentials"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extract the access_token
        access_token = data.get("access_token")
        if access_token:
            print(f"Access Token: {access_token}")
            return access_token
        else:
            print("Failed to retrieve access token. Response:", data)
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def get_campaign_details(access_token, campaign_id=None, adv_object_type=None, state=None):
    url = "https://api-performance.ozon.ru/api/client/campaign"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    params = {}
    if campaign_id:
        params["campaignIds"] = campaign_id
    if adv_object_type:
        params["advObjectType"] = adv_object_type
    if state:
        params["state"] = state

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    access_token = get_access_token()
    campaign_id = None  # Optional
    adv_object_type = None  # Optional
    state = None  # Optional
    campaign_details = get_campaign_details(access_token, campaign_id, adv_object_type, state)
    if campaign_details:
        with open('data.json', 'w') as file:
            json.dump(campaign_details, file)

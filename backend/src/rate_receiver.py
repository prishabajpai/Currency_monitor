import requests 
import os
from dotenv import load_dotenv 

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/INR"

def return_rate():

    response = requests.get(url)
    data = response.json()

    inr = data['conversion_rate']
    print(inr)

    return inr
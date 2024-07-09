
import requests
from django.shortcuts import render


def fetch_json_data():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    return response.json()


def display_table(request):
    data = fetch_json_data()
    rates = data.get("Valute")
    return render(request, 'table.html', {"rates": rates})

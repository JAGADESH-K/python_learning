import os
import csv
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

FILENAME = 'weather_logs.csv'

def log_weather():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['date','city','condition','temprature'])

    date = datetime.now().strftime('%d-%m-%Y')
    city_name = input("Enter a city name: ").strip()

    with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader: 
            if date == row['date'] and city_name.lower() == row['city'].lower(): 
                print("Entry already exists")
                return
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}&units=metric'
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200: 
            print("API ERROR")
            return
        with open(FILENAME, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date, city_name, data['weather'][0]['main'], data['main']['temp']])
            print(f"\n{city_name} weather is logged.")
    except Exception as e: print("Failed to make the API call")
    return

def view_logs():
    with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print('\n----weather logs ----\n')
        for row in reader:
            print(f" - date: {row['date']} | city: {row['city']} | condition: {row['condition']} | temprature: {row['temprature']}")
    return

def main():    
    while True:
        print("\n🌞 Welcome to the weather app 🌞\n")
        print("To log the weather enter 1")
        print("To view the logs enter 2")
        print("To exit enter 3")
        
        option = input("\nEnter your option (1-3): ").strip()

        match option:
            case '1': log_weather()
            case '2': view_logs()
            case '3': break
            case _ : print("Enter the valid option")

if __name__ == '__main__':
    main()
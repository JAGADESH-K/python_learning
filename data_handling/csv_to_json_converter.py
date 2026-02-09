import json
import csv
import os

INPUT_FILE = 'converted_movies_data.csv'
OUTPUT_FILE = 'json_converted_data.json'

def load_csv(filename):
    if not os.path.exists(filename):
        print("CSV file not found")
        return []
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except:
        print("Invalid format")
        return
    
def csv_to_json_converter(data, output_file):
    if not data:
        print("no data to convert")
        return
    
    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        writer = json.dump(data, f, indent=2)
        
        return
    
def main():
    data = load_csv(INPUT_FILE)
    print(data)
    csv_to_json_converter(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
import os
import csv
import json

INPUT_FILE = 'movies.json'
OUTPUT_FILE = 'converted_movies_data.csv'

def load_json(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format")
            return
        
def convert_to_csv(data, output_file):
    if not data:
        print("no data to convert")
        return  
 
    field_name = list(data[0].keys())
    
    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=field_name)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

        print(f"Converted {len(data)} records into {output_file}")
        return

def main():
    print("\nConverting JSON to CSV...\n")
    data = load_json(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == '__main__':
    main()

    
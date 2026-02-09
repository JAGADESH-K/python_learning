import os
import json

INPUT_FILE = 'nested_json_data.json'
OUTPUT_FILE = 'flattened_json_data.json'

def json_flattener(data, parant_key='', sep='.'):
    items = {}

    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{parant_key}{sep}{k}" if parant_key else k
            print(f"parant key: {parant_key} | k: {k} | full key: {full_key}")
            print(full_key)
            items.update(json_flattener(v, full_key, sep=sep))

    elif isinstance(data, list):
        for idx, v in enumerate(data):
            full_key = f"{parant_key}{sep}{idx}" if parant_key else str(idx)
            print(f"parant key: {parant_key} | idx: {idx} | full key: {full_key}")
            print(full_key)
            items.update(json_flattener(v, full_key, sep=sep))
    else:
        items[parant_key] = data
    
    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print("No input file found!")
        return
    
    try:
        with open(INPUT_FILE, 'r', newline='', encoding='utf-8') as f:
            data = json.load(f)
        sep = input("Enter a seperator ('.' or '-'): ").strip() or '.'

        result = json_flattener(data, sep=sep)
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            json.dump(result,f, indent=2)

        print("Flattened JSON saved")

    except Exception as e:
        print("Failed to flatten the data", e)

if __name__ == '__main__':
    main()                


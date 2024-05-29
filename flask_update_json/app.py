from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Define the path to the sample JSON file
JSON_FILE_PATH = 'sample.json'

# Load the sample JSON data from the file
def load_json_data():
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save the updated JSON data to the file
def save_json_data(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

# API endpoint to update JSON data
@app.route('/update_json', methods=['POST'])
def update_json():
    # Get user input from the request
    user_input = request.json
    
    # Load existing JSON data
    json_data = load_json_data()
    
    # Update JSON data with user input
    for key, value in user_input.items():
        json_data[key] = value
    
    # Save the updated JSON data
    save_json_data(json_data)
    
    return jsonify({"message": "JSON file updated successfully", "updated_data": json_data})

if __name__ == '__main__':
    app.run(debug=True)

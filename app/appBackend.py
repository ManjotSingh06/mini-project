from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify-hospital', methods=['POST'])
def notify_hospital():
    # Checking if the content type is JSON
    if request.is_json:
        # Getting data from the request
        data = request.get_json()

        # Extracting the data from the JSON
        name = data.get('name')
        phone = data.get('phone')
        location = data.get('location')
        time = data.get('time')
        vehicle_details = data.get('vehicle_details')
        emergency_contact = data.get('emergency_contact')

        # Simulate sending alert to hospital 
        print(f"Alert received from {name} ({phone})!")
        print(f"Location: {location}, Time: {time}")
        print(f"Vehicle Details: {vehicle_details}")
        if emergency_contact:
            print(f"Emergency Contact: {emergency_contact}")
        
        
        # Return a success response
        return jsonify({"message": "Alert sent to the nearby hospital successfully!"}), 200

    # If the content is not JSON, return an error
    return jsonify({"error": "Invalid content type, JSON expected!"}), 400

if __name__ == '__main__':
    
    app.run(debug=True)

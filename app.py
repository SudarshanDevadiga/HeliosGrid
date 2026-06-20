from flask import Flask, jsonify
import random
import requests

app = Flask(__name__)

# Vault Configuration
VAULT_URL = "http://host.docker.internal:8200/v1/secret/data/helios-config"
VAULT_TOKEN = "my-super-secret-token"

def get_vault_secret():
    try:
        headers = {"X-Vault-Token": VAULT_TOKEN}
        response = requests.get(VAULT_URL, headers=headers, timeout=3)
        if response.status_code == 200:
            # Extracting the weather key from the Vault JSON payload
            secret_data = response.json()["data"]["data"]
            return secret_data.get("WEATHER_API_KEY", "Key Not Found")
    except Exception:
        return "Vault Connection Failed"
    return "Vault Unauthorized"

@app.route('/')
def home():
    return "<h1>Welcome to HeliosGrid Energy Monitor</h1><p>Go to /telemetry to see live data.</p>"

@app.route('/telemetry')
def get_telemetry():
    # Fetch the live secret from Vault
    weather_key = get_vault_secret()
    
    data = {
        "solar_output_megawatts": random.randint(100, 500),
        "wind_output_megawatts": random.randint(50, 300),
        "battery_storage_percent": random.randint(40, 100),
        "grid_status": "Stable",
        "active_weather_auth_token": weather_key  # Exhibiting secure integration to regulators
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
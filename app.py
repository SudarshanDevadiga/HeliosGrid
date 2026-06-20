from flask import Flask, jsonify, Response
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
            secret_data = response.json()["data"]["data"]
            return secret_data.get("WEATHER_API_KEY", "Key Not Found")
    except Exception:
        return "Vault Connection Failed"
    return "Vault Unauthorized"

@app.route('/')
def home():
    return "<h1>Welcome to HeliosGrid Energy Monitor</h1><p>Go to /telemetry or /metrics to see live data.</p>"

@app.route('/telemetry')
def get_telemetry():
    weather_key = get_vault_secret()
    data = {
        "solar_output_megawatts": random.randint(100, 500),
        "wind_output_megawatts": random.randint(50, 300),
        "battery_storage_percent": random.randint(40, 100),
        "grid_status": "Stable",
        "active_weather_auth_token": weather_key
    }
    return jsonify(data)

# NEW: The endpoint Prometheus will read
@app.route('/metrics')
def get_metrics():
    solar = random.randint(100, 500)
    wind = random.randint(50, 300)
    battery = random.randint(40, 100)
    
    prometheus_data = f"""# HELP solar_output_megawatts Live solar generation
# TYPE solar_output_megawatts gauge
solar_output_megawatts {solar}
# HELP wind_output_megawatts Live wind generation
# TYPE wind_output_megawatts gauge
wind_output_megawatts {wind}
# HELP battery_storage_percent Live battery capacity
# TYPE battery_storage_percent gauge
battery_storage_percent {battery}
"""
    return Response(prometheus_data, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
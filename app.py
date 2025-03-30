from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

# City-specific data profiles
CITY_DATA = {
    "Bengaluru": {
        "solar_hours": 2670,
        "peak_sun_hours": 5.2,
        "wind_speed": 4.8,
        "wind_consistency": "Moderate",
        "aqi": 87,
        "primary_pollutant": "PM2.5",
        "green_cover": 22,
        "tree_canopy": 15,
        "biodiversity_index": "High",
        "biodiversity_recommendations": "Protect lakes and urban forests to maintain Bengaluru's biodiversity hotspots."
    },
    "Delhi": {
        "solar_hours": 2910,
        "peak_sun_hours": 5.8,
        "wind_speed": 3.2,
        "wind_consistency": "Low",
        "aqi": 342,
        "primary_pollutant": "PM2.5",
        "green_cover": 12,
        "tree_canopy": 8,
        "biodiversity_index": "Low",
        "biodiversity_recommendations": "Urgent need for urban afforestation and pollution control to revive ecosystems."
    },
    "Mumbai": {
        "solar_hours": 2530,
        "peak_sun_hours": 5.0,
        "wind_speed": 5.6,
        "wind_consistency": "High",
        "aqi": 153,
        "primary_pollutant": "PM10",
        "green_cover": 18,
        "tree_canopy": 12,
        "biodiversity_index": "Medium",
        "biodiversity_recommendations": "Protect coastal ecosystems and mangroves while developing urban green spaces."
    }
}

@app.route('/predict', methods=['GET'])
def predict():
    city = request.args.get('city', 'Bengaluru')
    
    # Get base data or generate defaults
    data = CITY_DATA.get(city, {
        "solar_hours": random.randint(2000, 3000),
        "peak_sun_hours": round(random.uniform(4.0, 6.0), 1),
        "wind_speed": round(random.uniform(3.0, 6.5), 1),
        "wind_consistency": random.choice(["Low", "Moderate", "High"]),
        "aqi": random.randint(50, 300),
        "primary_pollutant": random.choice(["PM2.5", "PM10", "NO2", "O3"]),
        "green_cover": random.randint(10, 25),
        "tree_canopy": random.randint(5, 20),
        "biodiversity_index": random.choice(["Low", "Medium", "High"]),
        "biodiversity_recommendations": "Implement urban greening strategies tailored to local ecosystem needs."
    })
    
    # Calculate ratings
    data.update({
        "solar_potential_rating": (
            "Excellent" if data["solar_hours"] > 2800 else
            "Good" if data["solar_hours"] > 2400 else
            "Moderate"
        ),
        "wind_potential_rating": (
            "Excellent" if data["wind_speed"] > 6.0 else
            "Good" if data["wind_speed"] > 4.5 else
            "Moderate"
        ),
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
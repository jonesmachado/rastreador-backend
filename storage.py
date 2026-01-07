from datetime import datetime

users = {
    "admin@teste.com": {
        "password": "123456",
        "active": True,
        "devices": {}
    }
}


def update_device(user_email, device_id, lat, lng):
    users[user_email]["devices"][device_id] = {
        "lat": lat,
        "lng": lng,
        "last_update": datetime.utcnow()
    }

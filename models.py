from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class LocationUpdate(BaseModel):
    device_id: str
    lat: float
    lng: float

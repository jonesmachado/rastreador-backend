from fastapi import FastAPI, Depends, HTTPException
from models import LoginRequest, LocationUpdate
from storage import users, update_device
from security import create_token
from auth import get_current_user

app = FastAPI(title="Plataforma de Rastreamento")


@app.post("/auth/login")
def login(data: LoginRequest):
    user = users.get(data.email)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    if not user["active"]:
        raise HTTPException(status_code=403, detail="Usuário bloqueado")

    token = create_token({"sub": data.email})
    return {"token": token}


@app.post("/location/update")
def update_location(
    data: LocationUpdate,
    user_email: str = Depends(get_current_user)
):
    update_device(user_email, data.device_id, data.lat, data.lng)
    return {"status": "ok"}


@app.get("/devices")
def list_devices(user_email: str = Depends(get_current_user)):
    return users[user_email]["devices"]

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import smtplib

import os

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

@app.get("/homeserver")
def get_homeserver():
    return FileResponse("static/homeserver.html")

@app.get("/test")
async def root():
    return {"message": "Hello world"}

@app.post("/contact")
async def contact(name: str = Form(...), message: str = Form(...)):
    msg = MIMEText(f"Viesti kotisivulta:\n\nNimi: {name}\n\n{message}")
    msg["Subject"] = "Uusi yhteydenotto kotisivulta"
    msg["From"] = "oma_sähköposti@example.com"
    msg["To"] = "vastaanottaja@example.com"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("oma_sähköposti@example.com", "SOVELLUSKOHTAINEN_SALASANA")
            server.send_message(msg)
        return JSONResponse({"status": "ok", "message": "Viestisi lähetettiin onnistuneesti!"})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)})


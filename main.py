from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json, os, random

app = FastAPI()

DATA_FILE = "users.json"

bad_words = ["login", "verify", "secure", "bank"]

sessions = {}
logs = {}

# load users file
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        users = json.load(f)
else:
    users = []

def save_users():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)

# -------- models --------
class Signup(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class URLCheck(BaseModel):
    token: str
    url: str

# -------- routes --------
@app.get("/")
def home():
    return {"msg": "URL Safety Checker API Running"}

@app.post("/signup")
def signup(data: Signup):
    if len(data.password) < 5:
        raise HTTPException(400, "Weak password")

    users.append(data.dict())
    save_users()
    print("Signup:", data.email)

    return {"msg": "Signup successful"}

@app.post("/login")
def login(data: Login):
    for u in users:
        if u["email"] == data.email and u["password"] == data.password:
            token = str(random.randint(10000, 99999))
            sessions[token] = u["email"]
            logs[u["email"]] = 0
            print("Login:", u["email"])
            return {"msg": "Login success", "token": token}

    raise HTTPException(401, "Invalid credentials")

@app.post("/check-url")
def check_url(data: URLCheck):

    if data.token not in sessions:
        raise HTTPException(403, "Login required")

    email = sessions[data.token]
    logs[email] += 1
    print(f"{email} checked:", data.url)

    if logs[email] > 5:
        return {"status": "Blocked", "reason": "Too many requests"}

    url = data.url.lower()

    if not url.startswith("https"):
        return {"status": "Suspicious", "reason": "No HTTPS"}

    for word in bad_words:
        if word in url:
            return {"status": "Warning", "reason": "Phishing keyword"}

    if "@" in url or "--" in url or url.count(".") > 3:
        return {"status": "Danger", "reason": "Fake domain pattern"}

    return {"status": "Safe"}

@app.get("/admin-stats")
def stats():
    return {
        "total_users": len(users),
        "active_sessions": len(sessions),
        "url_checks": logs
    }

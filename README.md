# URL Safety Checker API

A **beginner-friendly FastAPI project** to check the safety of URLs with login authentication and phishing detection.  
Ideal for learning **FastAPI**, **API authentication**, and basic **cybersecurity concepts**.

---

## Features 

- ✅ Signup & Login system (token-based authentication)
- ✅ URL phishing detection (keywords, fake domains)
- ✅ HTTPS check
- ✅ Rate limiting (5 checks per login session)
- ✅ Admin stats endpoint
- ✅ Persistent user storage (JSON file)
- ✅ Beginner-friendly & fully functional

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/url-safety-checker-api.git
```
```
cd url-safety-checker-api
```

## Create a virtual environment (recommended):
```
python -m venv venv
```
```
source venv/bin/activate   # Linux/Mac
```
```
venv\Scripts\activate      # Windows
```

## Install dependencies:
```
pip install fastapi uvicorn
```
## Usage
Run the FastAPI server:
```
uvicorn main:app --reload
```
Open browser and navigate:
```
http://127.0.0.1:8000/docs
```
Use endpoints:

/signup → create account

/login → get session token

/check-url → submit URLs for safety check

/admin-stats → view stats

Example
```
POST /signup
{
  "username": "shayan",
  "email": "test@mail.com",
  "password": "12345"
}

POST /login
{
  "email": "test@mail.com",
  "password": "12345"
}
Response:

{
  "msg": "Login success",
  "token": "48291"
}
```
## Future Upgrades
🔹 JWT authentication

🔹 Real phishing dataset

🔹 HTML dashboard for frontend

🔹 Charts & analytics

🔹 Brute-force detection

🔹 Admin & user roles

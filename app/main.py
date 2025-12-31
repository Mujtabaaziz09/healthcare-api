from fastapi import FastAPI

app = FastAPI(title="Health Management System API")

@app.get("/")
def read_root():
    return {
        "status": "Active",
        "message": "Welcome to the Health API",
        "developer": "Mujtaba Al Saif"
    }

@app.get("/health-check")
def check_status():
    return {
        "status": "System is running smoothly"
    }
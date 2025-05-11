from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data once at startup
with open(os.path.join(os.path.dirname(__file__), '../data.json')) as f:
    students = json.load(f)

# Create a name -> marks dictionary for fast lookup
marks_dict = {student["name"]: student["marks"] for student in students}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_dict.get(name, None) for name in names]
    return JSONResponse(content={"marks": result})


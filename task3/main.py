from fastapi import FastAPI, APIRouter
from app.db import engine, metadata, database
from fastapi.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI()
router = APIRouter()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/events")
async def get_event():
    return [{
        "id": 1,
        "date": "Mon Aug 31 2020 02:56:23 GMT+0300 (Moscow Standard Time)",
        "description": 'test descriptions0',
        "persons": [
            {
                "id": 1,
                "name": "user 1",
            },
            {
                "id": 2,
                "name": 'user 2',
            }
        ]
    }]


@app.post("/events")
async def get_event():
    return {"result": "success"}


@app.get("/events/{event_id}")
async def get_event(event_id):
    return {"event_id": event_id}

from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.post("/events/", response_model=schemas.Event)
def create_user(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event_item(db=db, event=event)


@app.get("/events/{event_id}")
async def get_event(event_id):
    return {"event_id": event_id}

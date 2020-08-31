from pydantic import BaseModel


class EventBase(BaseModel):
    description: str
    date: str


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    class Config:
        orm_mode = True


class PersonBase(BaseModel):
    name: str


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int
    class Config:
        orm_mode = True

from enum import StrEnum

from pydantic import BaseModel


class Status(StrEnum):
    BACKLOG = "Backlog"
    TODO = "Todo"
    IN_PROGRESS = "In Progress"
    IN_REVIEW = "In Review"
    DONE = "Done"
    CANCELED = "Canceled"
    DUPLICATE = "Duplicate"


class State(BaseModel):
    name: Status


class Label(BaseModel):
    name: str


class Labels(BaseModel):
    nodes: list[Label]


class User(BaseModel):
    name: str


class Comment(BaseModel):
    body: str
    user: User


class Comments(BaseModel):
    nodes: list[Comment]


class Cycle(BaseModel):
    number: int


class Project(BaseModel):
    name: str

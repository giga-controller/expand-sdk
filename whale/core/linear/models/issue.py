from typing import Optional

from pydantic import BaseModel

from whale.core.linear.models.base import (Comments, Cycle, Labels, Project, State,
                                    Status, User)


class LinearIssue(BaseModel):
    id: Optional[str]
    number: Optional[int]
    title: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    estimate: Optional[
        int
    ]  # Assume T-Shirt sizes for now, which is represented as an integer in the API
    state: Optional[State]
    assignee: Optional[User]
    creator: Optional[User]
    labels: Optional[Labels]
    createdAt: Optional[str]  # Timezone but in string format
    updatedAt: Optional[str]  # Timezone but in string format
    dueDate: Optional[str]  # YYYY-MM-DD but in string format
    cycle: Optional[Cycle]
    project: Optional[Project]
    comments: Optional[Comments]

    url: Optional[str]


class LinearGetIssueRequest(BaseModel):
    id: Optional[str]
    state: Optional[Status]
    assignee: Optional[str]
    creator: Optional[str]
    project: Optional[str]
    cycle: Optional[int]

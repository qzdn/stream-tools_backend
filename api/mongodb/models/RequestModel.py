from typing import List
from pydantic import BaseModel, Field


class Request(BaseModel):
    requester: str = Field(description="Username of the person who requested the video")
    videoId: str = Field(description="ID of the requested video")
    title: str = Field(description="Title of the requested video")
    length: int = Field(description="Length of the video in seconds")
    url: str = Field(description="URL of the requested video")
    timestamp: int = Field(description="Timestamp of the request")


class User(BaseModel):
    user: str = Field(description="Username")
    requests: List[Request] = Field(description="List of video requests by the user")

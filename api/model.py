from typing import Optional, List

from pydantic import BaseModel, Field, validator


class ChatMessageTurbo(BaseModel):
    role: Optional[str] = Field(default="user", description="Role")
    content: str = Field(..., description="Content")


class MessageTurbo(BaseModel):
    model: Optional[str] = Field(default="gpt-3.5-turbo", description="Model name")
    messages: Optional[List[ChatMessageTurbo]] = Field(default=None, description="Messages")
    stop: Optional[list] = Field(default=None, description="Stop sequence")


class Message(BaseModel):
    model: Optional[str] = Field(default="text-davinci-003", description="Model name")
    prompt: str = Field(..., description="Prompt text")
    max_tokens: Optional[int] = Field(default=2048, description="Maximum number of tokens")
    temperature: Optional[float] = Field(default=0.5, description="Temperature")
    frequency_penalty: Optional[float] = Field(default=0.0, description="Frequency penalty")
    presence_penalty: Optional[float] = Field(default=0.0, description="Presence penalty")
    top_p: Optional[float] = Field(default=1.0, description="Top p")
    stop: Optional[list] = Field(default=None, description="Stop sequence")


class Token(BaseModel):
    api_key: Optional[str] = Field(default=None, description="API key")

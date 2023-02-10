from typing import Optional

from pydantic import BaseModel, Field


class Message(BaseModel):
    model: Optional[str] = Field(default="text-davinci-003", description="Model name")
    prompt: str = Field(..., description="Prompt text")
    max_tokens: Optional[int] = Field(default=2048, description="Maximum number of tokens")
    temperature: Optional[float] = Field(default=0.5, description="Temperature")
    frequency_penalty: Optional[float] = Field(default=0.0, description="Frequency penalty")
    presence_penalty: Optional[float] = Field(default=0.0, description="Presence penalty")
    top_p: Optional[float] = Field(default=1.0, description="Top p")
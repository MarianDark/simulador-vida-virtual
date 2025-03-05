from pydantic import BaseModel
from typing import Optional

class NPCBase(BaseModel):
    name: str
    role: str
    intelligence_level: int
    mood: str

class NPCModel(NPCBase):
    id: Optional[str] = None

    class Config:
        from_attributes = True

class NPCDecisionResponse(BaseModel):
    npc_id: str
    decision: str

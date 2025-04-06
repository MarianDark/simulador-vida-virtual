from pydantic import BaseModel
from typing import Optional, List

class NPCBase(BaseModel):
    name: str
    role: str
    intelligence_level: int
    mood: str

class NPCModel(NPCBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True

class NPCDecisionResponse(BaseModel):
    npc_id: str
    decision: str

class NPCUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    intelligence_level: Optional[int] = None
    mood: Optional[str] = None
    habilidades: Optional[List[str]] = None
    experiencia: Optional[int] = None
    equipo: Optional[List[str]] = None
    aliados: Optional[List[str]] = None
    enemigos: Optional[List[str]] = None
    objetivo: Optional[str] = None
    historia: Optional[str] = None
    personalidad: Optional[str] = None
    motivaciones: Optional[List[str]] = None
    debilidades: Optional[List[str]] = None
    fortalezas: Optional[List[str]] = None
    objetivos: Optional[List[str]] = None
    objetivos_secundarios: Optional[List[str]] = None
    objetivos_terciarios: Optional[List[str]] = None
    objetivos_cuaternarios: Optional[List[str]] = None
    objetivos_quintarios: Optional[List[str]] = None

        

from fastapi import APIRouter, HTTPException
from models.npc import NPCModel, NPCBase, NPCDecisionResponse
from db import npc_collection

router = APIRouter()

@router.post("/npc/create", response_model=NPCModel)
async def create_npc(npc: NPCBase):
    new_npc = npc.dict()
    result = await npc_collection.insert_one(new_npc)
    new_npc["id"] = str(result.inserted_id)
    return new_npc

@router.get("/npc/{npc_id}", response_model=NPCModel)
async def get_npc(npc_id: str):
    npc = await npc_collection.find_one({"_id": npc_id})
    if not npc:
        raise HTTPException(status_code=404, detail="NPC no encontrado")
    return npc

@router.get("/npc/decidir", response_model=NPCDecisionResponse)
async def decidir_npc():
    return {"npc_id": "1234", "decision": "Atacar"}


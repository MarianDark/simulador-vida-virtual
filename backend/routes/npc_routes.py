from fastapi import APIRouter, HTTPException
from models.npc import NPCModel, NPCBase, NPCDecisionResponse
from db import npc_collection
from services.npc_service import generate_npc_decision

router = APIRouter()

@router.post("/npc/create", response_model=NPCModel)
async def create_npc(npc: NPCBase):
    new_npc = npc.model_dump()
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
    """
    Endpoint para que un NPC tome una decisión usando OpenAI.
    """
    prompt = "El NPC está en una situación difícil. ¿Qué debería hacer?"
    decision = generate_npc_decision(prompt)
    return {"npc_id": "1234", "decision": decision}

@router.put("/npc/update/{npc_id}", response_model=NPCModel)
async def update_npc(npc_id: str, npc: NPCBase):
    existing_npc = await npc_collection.find_one({"_id": npc_id})
    if not existing_npc:
        raise HTTPException(status_code=404, detail="NPC no encontrado")

    updated_npc = npc.model_dump()
    result = await npc_collection.update_one({"_id": npc_id}, {"$set": updated_npc})
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el NPC")

    updated_npc["_id"] = npc_id
    return updated_npc

@router.delete("/npc/delete/{npc_id}", response_model=dict)
async def delete_npc(npc_id: str):
    result = await npc_collection.delete_one({"_id": npc_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="NPC no encontrado")

    return {"detail": "NPC eliminado correctamente"}

@router.get("/npc/funciones", response_model=dict)
async def obtener_funciones():
    """
    Endpoint para obtener una lista de las funciones disponibles en este módulo.
    """
    funciones = {
        "create_npc": "Crea un nuevo NPC.",
        "get_npc": "Obtiene un NPC por su ID.",
        "decidir_npc": "El NPC toma una decisión usando OpenAI.",
        "update_npc": "Actualiza un NPC existente.",
        "delete_npc": "Elimina un NPC por su ID."
    }
    return funciones

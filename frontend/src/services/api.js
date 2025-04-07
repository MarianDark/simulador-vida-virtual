import axios from "axios";

const API_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";

export const getNpcDecision = async () => {
  try {
    const response = await axios.get(`${API_URL}/npc/decidir`);
    return response.data.decision;
  } catch (error) {
    console.error("❌ Error al obtener la decisión del NPC:", error);
    return "Error";
  }
};

export const createNpc = async (npcData) => {
  try {
    const response = await axios.post(`${API_URL}/npc/create`, npcData);
    return response.data;
  } catch (error) {
    console.error("❌ Error al crear el NPC:", error);
    throw error;
  }
};

import axios from "axios";

const API_URL = "http://localhost:8000"; // Asegúrate de que esta URL es accesible desde el frontend

export const getNpcDecision = async () => {
  try {
    const response = await axios.get(`${API_URL}/npc/decidir`);
    return response.data?.decision || "Decisión no disponible"; // Manejo de caso en que no haya decisión
  } catch (error) {
    console.error("Error obteniendo la decisión del NPC:", error.message);
    return "Error al obtener la decisión";
  }
};

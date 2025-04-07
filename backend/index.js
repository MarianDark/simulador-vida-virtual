const express = require("express");
const cors = require("cors");

const app = express();
const PORT = process.env.PORT || 8000;

app.use(cors());
app.use(express.json());

// Ruta para crear NPC
app.post("/npc/create", (req, res) => {
  const npc = req.body;
  console.log("📥 NPC recibido:", npc);
  // Simulación de creación
  npc._id = Date.now().toString();
  res.status(201).json(npc);
});

// Ruta para decisión del NPC
app.get("/npc/decision", (req, res) => {
  res.json("Voy a entrenar mis habilidades 🧠💪");
});

app.listen(PORT, () => {
  console.log(`🚀 Servidor backend corriendo en http://localhost:${PORT}`);
});

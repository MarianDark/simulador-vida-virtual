import React, { useState } from "react";
import { createNpc } from "../services/api";

const NpcForm = ({ onCreated }) => {
  const [formData, setFormData] = useState({
    name: "",
    role: "",
    intelligence_level: 5,
    mood: "neutral",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === "intelligence_level" ? Number(value) : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newNpc = await createNpc(formData);
      setMessage("✅ NPC creado con éxito");
      setFormData({ name: "", role: "", intelligence_level: 5, mood: "neutral" });
      if (onCreated) onCreated(newNpc); // Notificar al padre si aplica
    } catch (error) {
      console.error("❌ Error al crear el NPC:", error);
      setMessage("❌ Error al crear el NPC");
    }
  };

  return (
    <div>
      <h2>Crear NPC</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Nombre"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="role"
          placeholder="Rol (Ej. Guerrero)"
          value={formData.role}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="intelligence_level"
          min="1"
          max="10"
          placeholder="Nivel de inteligencia"
          value={formData.intelligence_level}
          onChange={handleChange}
          required
        />
        <select name="mood" value={formData.mood} onChange={handleChange}>
          <option value="neutral">Neutral</option>
          <option value="feliz">Feliz</option>
          <option value="enojado">Enojado</option>
        </select>
        <button type="submit">Crear NPC</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default NpcForm;

import React, { useEffect, useState, useRef } from "react";
import * as PIXI from "pixi.js";
import anime from "animejs";
import { getNpcDecision, createNpc } from "../services/api";

const Game = () => {
  const [npcDecision, setNpcDecision] = useState("Cargando...");
  const [formData, setFormData] = useState({
    name: "",
    role: "",
    intelligence_level: 1,
    mood: "neutral",
  });
  const [npcResponse, setNpcResponse] = useState(null);

  const gameContainerRef = useRef(null);
  const appRef = useRef(null);

  useEffect(() => {
    const app = new PIXI.Application({
      width: 800,
      height: 600,
      backgroundColor: 0x1099bb,
      antialias: true,
      resolution: window.devicePixelRatio || 1,
    });

    appRef.current = app;

    if (gameContainerRef.current) {
      gameContainerRef.current.appendChild(app.view);
    }

    PIXI.Assets.add("npc", "/assets/npc.png");

    PIXI.Assets.load("npc").then((texture) => {
      const sprite = new PIXI.Sprite(texture);
      sprite.anchor.set(0.5);
      sprite.x = app.screen.width / 2;
      sprite.y = app.screen.height / 2;
      sprite.scale.set(0.5);
      app.stage.addChild(sprite);

      anime({
        targets: sprite,
        x: [200, 600],
        y: [150, 450],
        duration: 2000,
        easing: "easeInOutQuad",
        loop: true,
        direction: "alternate",
      });

      const fetchDecision = async () => {
        try {
          const decision = await getNpcDecision();
          setNpcDecision(decision);
        } catch (error) {
          console.error("❌ Error obteniendo la decisión del NPC:", error);
          setNpcDecision("Error al obtener la decisión");
        }
      };

      fetchDecision();
    });

    return () => {
      if (appRef.current) {
        appRef.current.destroy(true, {
          children: true,
          texture: true,
          baseTexture: true,
        });
      }
    };
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === "intelligence_level" ? parseInt(value, 10) : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newNpc = await createNpc(formData);
      setNpcResponse(`✅ NPC creado con ID: ${newNpc._id}`);
    } catch (error) {
      console.error("❌ Error al crear el NPC:", error);
      setNpcResponse("❌ Error al crear el NPC");
    }
  };

  return (
    <div>
      <h1>Simulador de Vida Virtual</h1>
      <p>Decisión del NPC: {npcDecision}</p>

      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <input
          name="name"
          placeholder="Nombre"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          name="role"
          placeholder="Rol (ej: Guerrero)"
          value={formData.role}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="intelligence_level"
          placeholder="Nivel de inteligencia"
          value={formData.intelligence_level}
          onChange={handleChange}
          required
        />
        <select name="mood" value={formData.mood} onChange={handleChange}>
          <option value="feliz">Feliz</option>
          <option value="enojado">Enojado</option>
          <option value="neutral">Neutral</option>
        </select>
        <button type="submit">Crear NPC</button>
      </form>

      {npcResponse && <p>{npcResponse}</p>}
      <div ref={gameContainerRef} id="game-container"></div>
    </div>
  );
};

export default Game;


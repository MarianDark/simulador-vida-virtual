import React, { useEffect, useState } from "react";
import { Application, Sprite } from "pixi.js";
import anime from "animejs";
import { getNpcDecision } from "./services/api";

const App = () => {
  const [npcDecision, setNpcDecision] = useState("Cargando...");

  useEffect(() => {
    const app = new Application({
      width: 800,
      height: 600,
      backgroundColor: 0x1099bb,
      antialias: true,
      resolution: window.devicePixelRatio || 1,
      powerPreference: "high-performance",
    });

    document.getElementById("game-container").appendChild(app.view);

    const sprite = Sprite.from("npc.png");
    sprite.x = 100;
    sprite.y = 100;
    app.stage.addChild(sprite);

    anime({
      targets: sprite,
      x: 400,
      y: 300,
      duration: 2000,
      easing: "easeInOutQuad",
      loop: true,
      direction: "alternate",
    });

    async function fetchDecision() {
      try {
        const decision = await getNpcDecision();
        setNpcDecision(decision);
      } catch (error) {
        console.error("Error obteniendo la decisión del NPC:", error);
        setNpcDecision("Error al obtener la decisión");
      }
    }

    fetchDecision();

    return () => app.destroy(true);
  }, []);

  return (
    <div>
      <h1>Simulador de Vida Virtual</h1>
      <p>Decisión del NPC: {npcDecision}</p>
      <div id="game-container"></div>
    </div>
  );
};

export default App;

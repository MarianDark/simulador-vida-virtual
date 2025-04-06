import React, { useEffect, useState, useRef } from "react";
import { Application, Sprite, Loader } from "pixi.js";
import anime from "animejs";
import { getNpcDecision } from "../services/api";

const Game = () => {
  const [npcDecision, setNpcDecision] = useState("Cargando...");
  const gameContainerRef = useRef(null);
  const appRef = useRef(null); // Mantiene referencia a la instancia de PixiJS

  useEffect(() => {
    // ⚡ Crear la aplicación PixiJS
    const app = new Application({
      width: 800,
      height: 600,
      backgroundColor: 0x1099bb,
      antialias: true,
      resolution: window.devicePixelRatio || 1,
    });

    // Guardar referencia de la instancia de PixiJS
    appRef.current = app;

    // Agregar el canvas dentro del contenedor
    if (gameContainerRef.current) {
      gameContainerRef.current.appendChild(app.view);
    }

    // ⚡ Cargar los assets
    const loader = new Loader();
    loader.add("npc", "/assets/npc.png").load(() => {
      // Crear el sprite una vez cargado
      const sprite = new Sprite(loader.resources["npc"].texture);
      sprite.anchor.set(0.5);
      sprite.x = app.screen.width / 2;
      sprite.y = app.screen.height / 2;
      sprite.scale.set(0.5);
      app.stage.addChild(sprite);

      // ⚡ Animación con Anime.js
      anime({
        targets: sprite,
        x: [200, 600],
        y: [150, 450],
        duration: 2000,
        easing: "easeInOutQuad",
        loop: true,
        direction: "alternate",
      });

      // ⚡ Obtener la decisión del NPC desde el backend
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

    // ⚡ Limpiar PixiJS cuando el componente se desmonte
    return () => {
      if (appRef.current) {
        appRef.current.destroy(true, { children: true, texture: true, baseTexture: true });
      }
    };
  }, []);

  return (
    <div>
      <h1>Simulador de Vida Virtual</h1>
      <p>Decisión del NPC: {npcDecision}</p>
      <div ref={gameContainerRef} id="game-container"></div>
    </div>
  );
};

export default Game;


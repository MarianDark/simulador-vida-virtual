import React from "react";
import Game from "./components/Game";
import NpcForm from "./components/NpcForm";

const App = () => {
  return (
    <div>
      <h1>Simulador de Vida Virtual con IA</h1>
      <NpcForm />
      <Game />
    </div>
  );
};

export default App;

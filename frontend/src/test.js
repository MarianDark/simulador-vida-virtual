import { getNpcDecision } from "./services/api.js";

(async () => {
  const decision = await getNpcDecision();
  console.log("Decisión del NPC:", decision);
})();

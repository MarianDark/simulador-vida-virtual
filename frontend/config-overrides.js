const { override, addWebpackAlias, addWebpackModuleRule, addBabelPlugin } = require("customize-cra");
const path = require("path");

module.exports = override(
  // Alias para PixiJS
  addWebpackAlias({
    "pixi.js": path.resolve(__dirname, "node_modules/pixi.js")
  }),

  // Soporte para módulos .mjs en node_modules (necesario para PixiJS ESM)
  addWebpackModuleRule({
    test: /\.mjs$/,
    include: /node_modules/,
    type: "javascript/auto"
  }),

  // Añadir plugin de Babel
  addBabelPlugin("babel-plugin-styled-components")
);

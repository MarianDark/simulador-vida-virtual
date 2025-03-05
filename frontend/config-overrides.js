const { override, addWebpackAlias } = require("customize-cra");
const path = require("path");

module.exports = override(
  addWebpackAlias({
    "pixi.js": path.resolve(__dirname, "node_modules/pixi.js")
  })
);

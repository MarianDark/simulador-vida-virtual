🎮 Simulador de Vida Virtual con IA 🤖
Un mini juego donde los personajes virtuales aprenden, interactúan y evolucionan utilizando Inteligencia Artificial. Los NPCs toman decisiones en tiempo real, aprenden de su entorno y cambian su comportamiento según las interacciones del usuario. 🌍✨

🚀 Tecnologías Utilizadas
Frontend 🖥️
⚛ React – Framework de JavaScript para interfaces interactivas.
🎨 PixiJS – Renderizado 2D basado en WebGL para gráficos de alto rendimiento.
🎭 Anime.js – Animaciones suaves y transiciones fluidas.
Backend 🔥
🐍 FastAPI – API rápida y eficiente con Python.
🧠 TensorFlow – Machine Learning para el aprendizaje de los NPCs.
🗄️ MongoDB – Base de datos NoSQL para almacenar la evolución del juego.
🔐 OAuth – Sistema de autenticación segura.
APIs ⚡
🤖 OpenAI API – Permite a los NPCs tomar decisiones más inteligentes y realistas.
Gráficos y Animaciones 🎨
🕹 WebGL – Renderizado gráfico eficiente con PixiJS.
✨ Anime.js – Movimientos suaves en personajes y entornos.
Seguridad 🔐
🏰 OAuth – Autenticación de usuarios segura y controlada.
📥 Instalación y Ejecución
1️⃣ Clonar el repositorio
sh
Copiar
Editar
git clone https://github.com/tu-usuario/simulador-vida-virtual.git
cd simulador-vida-virtual
2️⃣ Configurar el Backend
📦 Instalar dependencias

sh
Copiar
Editar
pip install -r backend/requirements.txt
🚀 Ejecutar FastAPI

sh
Copiar
Editar
uvicorn backend.main:app --reload
3️⃣ Configurar el Frontend
📦 Instalar dependencias

sh
Copiar
Editar
cd frontend
npm install
🚀 Ejecutar el frontend

sh
Copiar
Editar
npm start
4️⃣ Configurar la Base de Datos
Asegúrate de que MongoDB está corriendo en MongoDB Atlas y actualiza la cadena de conexión en el backend.

5️⃣ Configurar la OpenAI API
Crea un archivo .env en el backend y agrega tu clave:

sh
Copiar
Editar
OPENAI_API_KEY=tu_clave_aqui
🤝 Contribuciones
Las contribuciones son bienvenidas 🎉. Si deseas mejorar el proyecto, por favor abre un pull request o crea un issue para discutirlo.

📌 Desarrollado con ❤️ por
Marian Molina López ✨

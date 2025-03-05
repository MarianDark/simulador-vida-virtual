# Usa una imagen oficial de Node.js como base
FROM node:18

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia package.json y package-lock.json primero (para optimizar la caché de Docker)
COPY package.json package-lock.json ./

# Instala solo las dependencias necesarias
RUN npm install --legacy-peer-deps

# Copia el resto del código después de instalar las dependencias
COPY . .

# Desactivar OpenSSL para evitar el error "ERR_OSSL_EVP_UNSUPPORTED"
ENV NODE_OPTIONS=--openssl-legacy-provider

# Expone el puerto 3000 (React usa este puerto por defecto)
EXPOSE 3000

# Comando para ejecutar React en modo producción
CMD ["npx", "react-app-rewired", "start"]

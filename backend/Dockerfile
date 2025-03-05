# Usar una imagen base de Python
FROM python:3.10

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del backend al contenedor
COPY . .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000 para FastAPI
EXPOSE 8000

# Comando para iniciar el backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

from pymongo import MongoClient

# 🔹 Reemplaza esto con tu conexión de MongoDB Atlas
MONGO_URI = "mongodb+srv://marianmolina29:Hola1234@cluster1.oupgs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

try:
    client = MongoClient(MONGO_URI)
    db = client["SIMULADOR-VIDA-VIRTUAL"]
    print("✅ Conexión exitosa a MongoDB!")
    
    # 🔹 Probar si hay colecciones en la base de datos
    collections = db.list_collection_names()
    print("Colecciones en la base de datos:", collections)

except Exception as e:
    print(f"❌ Error de conexión: {e}")

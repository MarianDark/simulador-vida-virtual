from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Cambia esto por el dominio del frontend si lo deseas restringir
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

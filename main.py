from fastapi import FastAPI

app = FastAPI(
    title="API de Demostración",
    description="Una API simple para demostrar pruebas automatizadas.",
    version="1.0.0",
)

@app.get("/")
def read_root():
    """Devuelve un saludo de bienvenida."""
    return {"message": "Hola, Mundo!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """Devuelve un item específico, con una query opcional."""
    return {"item_id": item_id, "q": q}

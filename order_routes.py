from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def lista_pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}

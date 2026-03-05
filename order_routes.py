from fastapi import APIRouter, Depends, HTTPException
from dependencies import pegar_sessao
from sqlalchemy.orm import Session
from schemas import PedidoSchema
from models import Pedido


order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def lista_pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}


@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}
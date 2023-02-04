from fastapi import APIRouter
from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from .containers import Container
from .services import ShoppingCartService

router = APIRouter()



@router.get("/test")
def test():
    return {"data": "testtttttttttttttttttttt"}

@router.get("/cart/user/{user_id}")
@inject
def get_cart_by_user_id(user_id: int,
                   cart_service: ShoppingCartService =
                   Depends(Provide[Container.cart_service])):
    return cart_service.get_cart_by_user_id(user_id)

@router.delete("/cart/user/{user_id}")
@inject
def delete_cart_by_user_id(user_id: int,
                           cart_service: ShoppingCartService =
                           Depends(Provide[Container.cart_service])):
    return cart_service.delete_cart_by_user_id(user_id)

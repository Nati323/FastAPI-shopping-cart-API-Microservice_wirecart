from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from dependency_injector.wiring import inject, Provide
from .containers import Container
from .services import ShoppingCartService
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/test")
def test(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request, 'id': 'Test'})

@router.get("/cart/user/{user_id}")
@inject
def get_cart_by_user_id(user_id: int,
                   cart_service: ShoppingCartService =
                   Depends(Provide[Container.cart_service])):
    return cart_service.get_cart_by_user_id(user_id)

@router.get("/cart/user/{user_id}/html", response_class=HTMLResponse)
@inject
def get_cart_by_user_id_html(request: Request, user_id: int,
                   cart_service: ShoppingCartService =
                   Depends(Provide[Container.cart_service])):
    data = cart_service.get_cart_by_user_id(user_id)
    return templates.TemplateResponse("cart.html", {"request": request, "user_id": user_id, "data": data})

@router.delete("/cart/user/{user_id}")
@inject
def delete_cart_by_user_id(user_id: int,
                           cart_service: ShoppingCartService =
                           Depends(Provide[Container.cart_service])):
    return cart_service.delete_cart_by_user_id(user_id)

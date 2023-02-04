from .repositories import ShoppingCartRepository


class ShoppingCartService:
    def __init__(self, cart_repository: ShoppingCartRepository):
        self.cart_repo: ShoppingCartRepository = cart_repository

    def get_cart_by_user_id(self, user_id):
        try:
            r = self.cart_repo.get_by_user_id(user_id)
        except Exception as e:
            return {"status": "error", "status_code": 402, "message": str(e)}
        
        return r


    def delete_cart_by_user_id(self, user_id):
        try:
            r = self.cart_repo.delete_by_user_id(user_id)
        except Exception as e:
            return {"status": "error", "status_code": 402, "message": str(e)}
        
        return r

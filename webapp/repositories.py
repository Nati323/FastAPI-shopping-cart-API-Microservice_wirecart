from .models import ShoppingCart


class ShoppingCartRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory


    def get_by_user_id(self, user_id):
        with self.session_factory() as s:
            rec: ShoppingCart = s.query(ShoppingCart).filter(ShoppingCart.user_id == user_id).all()
            
            if not rec:
                raise Exception(f"User #{user_id} doesn't have a cart!")
            
            return rec


    def delete_by_user_id(self, user_id):
        try:
            with self.session_factory() as s:
                rec: ShoppingCart = s.query(ShoppingCart).filter(ShoppingCart.user_id == user_id).all()
                if not rec:
                    raise Exception(f"User #{user_id} doesn't have a cart!")
                for o in rec:
                    s.delete(o)
                s.commit()
        except Exception as e:
            raise Exception(str(e))




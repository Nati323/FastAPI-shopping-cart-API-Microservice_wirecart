from dependency_injector import containers, providers

from .database import Database
from .repositories import ShoppingCartRepository
from .services import ShoppingCartService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(Database, db_url=config.db.url)

    cart_repository = providers.Factory(
        ShoppingCartRepository,
        session_factory=db.provided.session)
    
    cart_service = providers.Factory(
        ShoppingCartService,
        cart_repository=cart_repository)
    
    

from .model import Author
from ..base_repository import BaseRepository


class Repository(BaseRepository):
    model = Author

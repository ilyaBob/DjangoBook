from dataclasses import asdict
from typing import TypeVar, Generic, Type

T = TypeVar("T")


class BaseRepository(Generic[T]):
    model: Type[T] = None

    def __init__(self):
        if not self.model:
            raise NotImplementedError("Укажите self.model в наследнике")

    def create(self, data) -> None:
        data = asdict(data)
        model = self.model(**data)
        model.save()

    def get_or_create_by_name(self, value) -> T:
        model = self.model.objects.filter(title=value).first()
        if not model:
            model = self.model(title=value)
            model.save()

        return model